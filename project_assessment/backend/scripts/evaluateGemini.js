const fs = require('node:fs/promises');
const path = require('node:path');
const { randomUUID } = require('node:crypto');
require('dotenv').config({ quiet: true });
// The smoke test intentionally favors reliability over speed on low-quota projects.
// Override this in the environment after checking the project's active AI Studio quota.
process.env.LLM_MIN_REQUEST_INTERVAL_MS ||= '31000';
const { getLlmConfig, llmAdapter } = require('../src/services/aiAdapters');
const fixtures = require('../test/fixtures/gemini-smoke-cases.json');

const HEADS = ['bloom', 'knowledgeDimension', 'intendedDifficulty'];

function contentById(caseId) {
  return fixtures.solverCases.find((item) => item.caseId === caseId)?.content;
}

function percentile(values, ratio) {
  if (!values.length) return null;
  const sorted = [...values].sort((a, b) => a - b);
  return sorted[Math.min(sorted.length - 1, Math.ceil(sorted.length * ratio) - 1)];
}

function solverPass(expected, result) {
  if (expected.abstain) return result.samples.every((sample) => sample.abstain === true) && result.stable === false;
  if (!result.stable || result.samples.some((sample) => sample.abstain)) return false;
  if (expected.answerOptionIds) {
    const wanted = JSON.stringify([...expected.answerOptionIds].sort());
    return result.samples.every((sample) => JSON.stringify([...sample.answerOptionIds].sort()) === wanted);
  }
  return result.samples.every((sample) => typeof sample.numericAnswer === 'number'
    && Math.abs(sample.numericAnswer - expected.numericAnswer) <= expected.tolerance);
}

function candidateBound(adjudication, source) {
  if (!adjudication.resolved) return true;
  return HEADS.every((head) => [source.indobert.labels[head], source.llm.labels[head]].includes(adjudication.labels[head]));
}

async function measured(action) {
  const started = performance.now();
  try {
    const value = await action();
    return { ok: true, latencyMs: Math.round(performance.now() - started), value };
  }
  catch (error) { return { ok: false, latencyMs: Math.round(performance.now() - started), error: { code: error.code || 'unknown', message: error.message } }; }
}

async function atomicJson(file, value) {
  await fs.mkdir(path.dirname(file), { recursive: true });
  const temporary = `${file}.${randomUUID()}.tmp`;
  try {
    await fs.writeFile(temporary, JSON.stringify(value, null, 2), { encoding: 'utf8', flag: 'wx' });
    await fs.rename(temporary, file);
  } finally { await fs.rm(temporary, { force: true }); }
}

async function main() {
  const config = getLlmConfig();
  if (!llmAdapter.configured()) throw Object.assign(new Error('Gemini belum dikonfigurasi. Isi GEMINI_API_KEY pada .env.'), { code: 'llm_not_configured' });
  const evaluationId = `GEMINI-SMOKE-${new Date().toISOString().replace(/[:.]/g, '-')}`;
  const report = {
    evaluationId, fixtureVersion: fixtures.fixtureVersion, startedAt: new Date().toISOString(),
    configuration: { provider: config.provider, screenModel: config.screenModel, solverModel: config.solverModel,
      adjudicatorModel: config.adjudicatorModel, sampleCount: Number(process.env.LLM_SAMPLE_COUNT || 3),
      reasoningEffort: config.reasoningEffort, minRequestIntervalMs: Number(process.env.LLM_MIN_REQUEST_INTERVAL_MS) },
    solver: [], screening: [], adjudication: [], summary: null,
  };

  const initialCooldownMs = Number(process.env.LLM_SMOKE_INITIAL_COOLDOWN_MS || 65000);
  if (!Number.isFinite(initialCooldownMs) || initialCooldownMs < 0) {
    throw Object.assign(new Error('LLM_SMOKE_INITIAL_COOLDOWN_MS harus berupa angka non-negatif.'), { code: 'llm_invalid_configuration' });
  }
  if (initialCooldownMs > 0) {
    console.log(`[cooldown] menunggu ${initialCooldownMs}ms sebelum request pertama`);
    await new Promise((resolve) => setTimeout(resolve, initialCooldownMs));
  }

  for (const fixture of fixtures.solverCases) {
    console.log(`[solver] ${fixture.caseId} dimulai`);
    const measuredResult = await measured(() => llmAdapter.solve(fixture.content));
    const entry = { caseId: fixture.caseId, description: fixture.description, expected: fixture.expected,
      ok: measuredResult.ok, latencyMs: measuredResult.latencyMs };
    if (measuredResult.ok) Object.assign(entry, { passed: solverPass(fixture.expected, measuredResult.value), result: measuredResult.value });
    else Object.assign(entry, { passed: false, error: measuredResult.error });
    report.solver.push(entry);
    console.log(`[solver] ${fixture.caseId} ${entry.passed ? 'PASS' : 'FAIL'} (${entry.latencyMs}ms)`);
  }

  for (const fixture of fixtures.screeningCases) {
    console.log(`[screening] ${fixture.caseId} dimulai`);
    const content = contentById(fixture.contentRef);
    const measuredResult = await measured(() => llmAdapter.screen(content));
    const entry = { caseId: fixture.caseId, description: fixture.description, expected: fixture.expected,
      ok: measuredResult.ok, latencyMs: measuredResult.latencyMs };
    if (measuredResult.ok) {
      const headMatches = Object.fromEntries(HEADS.map((head) => [head, measuredResult.value.labels[head] === fixture.expected[head]]));
      Object.assign(entry, { passed: HEADS.every((head) => headMatches[head]), headMatches, result: measuredResult.value });
    } else Object.assign(entry, { passed: false, error: measuredResult.error });
    report.screening.push(entry);
    console.log(`[screening] ${fixture.caseId} ${entry.passed ? 'PASS' : 'FAIL'} (${entry.latencyMs}ms)`);
  }

  for (const fixture of fixtures.adjudicationCases) {
    console.log(`[adjudication] ${fixture.caseId} dimulai`);
    const content = contentById(fixture.contentRef);
    const measuredResult = await measured(() => llmAdapter.adjudicate(content, fixture.indobert, fixture.llm));
    const entry = { caseId: fixture.caseId, description: fixture.description, preferred: fixture.preferred,
      ok: measuredResult.ok, latencyMs: measuredResult.latencyMs };
    if (measuredResult.ok) {
      const bounded = candidateBound(measuredResult.value, fixture);
      const preferredOrSafeAbstain = !measuredResult.value.resolved
        || HEADS.every((head) => measuredResult.value.labels[head] === fixture.preferred[head]);
      Object.assign(entry, { passed: bounded && preferredOrSafeAbstain, candidateBound: bounded,
        preferredOrSafeAbstain, result: measuredResult.value });
    } else Object.assign(entry, { passed: false, error: measuredResult.error });
    report.adjudication.push(entry);
    console.log(`[adjudication] ${fixture.caseId} ${entry.passed ? 'PASS' : 'FAIL'} (${entry.latencyMs}ms)`);
  }

  const entries = [...report.solver, ...report.screening, ...report.adjudication];
  const successfulLatencies = entries.filter((entry) => entry.ok).map((entry) => entry.latencyMs);
  const requests = llmAdapter.getTelemetry();
  const successfulProviderLatencies = requests.filter((item) => item.outcome === 'ok').map((item) => item.providerLatencyMs);
  const screeningConsistency = report.screening.flatMap((entry) => entry.result ? HEADS.map((head) => entry.result.consistency[head]) : []);
  const passed = entries.filter((entry) => entry.passed).length;
  report.completedAt = new Date().toISOString();
  report.summary = {
    totalCases: entries.length, passedCases: passed, failedCases: entries.length - passed,
    solverPassed: report.solver.filter((entry) => entry.passed).length,
    screeningPassed: report.screening.filter((entry) => entry.passed).length,
    adjudicationPassed: report.adjudication.filter((entry) => entry.passed).length,
    minimumScreeningConsistency: screeningConsistency.length ? Math.min(...screeningConsistency) : null,
    operationLatencyMs: { min: successfulLatencies.length ? Math.min(...successfulLatencies) : null,
      median: percentile(successfulLatencies, 0.5), p95: percentile(successfulLatencies, 0.95),
      max: successfulLatencies.length ? Math.max(...successfulLatencies) : null,
      total: entries.reduce((sum, entry) => sum + entry.latencyMs, 0) },
    providerLatencyMs: { min: successfulProviderLatencies.length ? Math.min(...successfulProviderLatencies) : null,
      median: percentile(successfulProviderLatencies, 0.5), p95: percentile(successfulProviderLatencies, 0.95),
      max: successfulProviderLatencies.length ? Math.max(...successfulProviderLatencies) : null,
      average: successfulProviderLatencies.length
        ? Math.round(successfulProviderLatencies.reduce((sum, value) => sum + value, 0) / successfulProviderLatencies.length) : null },
    requests: { total: requests.length, successful: requests.filter((item) => item.outcome === 'ok').length,
      rateLimited: requests.filter((item) => item.outcome === 'llm_rate_limited').length,
      totalQueueWaitMs: requests.reduce((sum, item) => sum + item.queueWaitMs, 0) },
    verdict: passed === entries.length ? 'promising_for_continued_evaluation' : 'requires_revision_before_continuing',
    limitation: 'Smoke evaluation kecil ini bukan bukti akurasi produksi dan tidak menghasilkan gold label.',
  };
  report.requestTelemetry = requests;

  const root = path.resolve(process.env.QUESTION_DATA_DIR || path.resolve(__dirname, '../../../../data/local'));
  const output = path.join(root, 'evaluations', `${evaluationId}.json`);
  await atomicJson(output, report);
  console.log(`Hasil tersimpan: ${output}`);
  console.log(`Verdict: ${report.summary.verdict}; pass=${passed}/${entries.length}; total=${report.summary.operationLatencyMs.total}ms`);
  if (passed !== entries.length) process.exitCode = 2;
}

main().catch((error) => {
  console.error(`Evaluasi gagal [${error.code || 'unknown'}]: ${error.message}`);
  process.exitCode = 1;
});
