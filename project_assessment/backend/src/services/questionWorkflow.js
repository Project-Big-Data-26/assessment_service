const { validateQuestion } = require('./questionValidation');
const { indobertAdapter, llmAdapter } = require('./aiAdapters');
const { createHash } = require('node:crypto');
const { assertQuestionRepository } = require('./questionRepositoryPort');
const fs = require('node:fs');
const path = require('node:path');

const HEADS = ['bloom', 'knowledgeDimension', 'intendedDifficulty'];
function loadRiskPolicy() {
  return JSON.parse(fs.readFileSync(path.resolve(__dirname, '../../../../configs/ai_risk_policy.json'), 'utf8'));
}

function requireApprovedRiskPolicy(policy) {
  const calibrated = policy?.approved_for_provisional === true && typeof policy.policyVersion === 'string'
    && HEADS.every((head) => typeof policy.indobertConfidenceMin?.[head] === 'number'
      && Number.isFinite(policy.indobertConfidenceMin[head]) && policy.indobertConfidenceMin[head] > 0
      && policy.indobertConfidenceMin[head] <= 1 && typeof policy.llmConsistencyMin?.[head] === 'number'
      && Number.isFinite(policy.llmConsistencyMin[head]) && policy.llmConsistencyMin[head] > 0
      && policy.llmConsistencyMin[head] <= 1);
  if (!calibrated) throw Object.assign(new Error('Kebijakan risiko belum disetujui atau ambang per-head belum dikalibrasi.'), { code: 'risk_policy_unapproved' });
}

function normalizeContent(content) {
  const trim = (value) => typeof value === 'string' ? value.normalize('NFKC').trim() : value;
  return { ...content, topic: trim(content.topic), subtopic: trim(content.subtopic), questionText: trim(content.questionText),
    learningObjective: trim(content.learningObjective), explanation: trim(content.explanation),
    options: (content.options || []).map((option) => ({ ...option, text: trim(option.text) })) };
}

function answerMatches(content, answer) {
  if (content.answerSpec.kind === 'option_ids') {
    return JSON.stringify([...content.answerSpec.optionIds].sort()) === JSON.stringify([...answer.answerOptionIds].sort());
  }
  if (content.answerSpec.kind === 'numeric' && typeof answer.numericAnswer === 'number') {
    return Math.abs(content.answerSpec.value - answer.numericAnswer) <= (content.answerSpec.tolerance || 0);
  }
  return false;
}

function createWorkflowService(repository, adapters = { indobert: indobertAdapter, llm: llmAdapter }, riskPolicy = loadRiskPolicy()) {
  assertQuestionRepository(repository);
  let queue = Promise.resolve();

  async function execute(runId) {
    const run = await repository.getRun(runId, process.env.LOCAL_TEACHER_ID || 'local-teacher');
    if (!run || ['succeeded', 'failed'].includes(run.status)) return;
    try {
      await repository.updateRun(runId, { status: 'running', stage: 'canonicalization' });
      const version = await repository.getVersion(run.questionId, run.contentVersion);
      if (!version) throw Object.assign(new Error('Versi soal tidak ditemukan.'), { code: 'content_version_missing' });
      const content = normalizeContent(version.authoringContent);
      const canonicalAudit = { canonicalizationVersion: 'nfkc-trim-v1', canonicalContentHash: createHash('sha256').update(JSON.stringify(content)).digest('hex') };
      await repository.updateRun(runId, { stage: 'structural_validation' });
      const validation = validateQuestion(content);
      if (!validation.valid) {
        await repository.finish(runId, 'revision_required', { ...canonicalAudit, summary: { answerVerified: false, decisionType: 'quarantined', taxonomy: null, warnings: validation.errors.map((item) => item.message) }, validation });
        return;
      }
      await repository.updateRun(runId, { stage: 'answer_verification' });
      const deterministic = adapters.indobert.verifyAnswer ? await adapters.indobert.verifyAnswer(content) : { status: 'unsupported' };
      const solved = deterministic.status === 'unsupported' ? await adapters.llm.solve(content) : null;
      const answerVerified = deterministic.status === 'passed' || (solved?.stable && answerMatches(content, solved.answer));
      if (!answerVerified) {
        await repository.finish(runId, 'quarantined', { ...canonicalAudit, summary: { answerVerified: false, decisionType: 'quarantined', taxonomy: null, warnings: ['answer_conflict'] }, answerVerification: deterministic.status === 'unsupported' ? solved : deterministic });
        return;
      }
      await repository.updateRun(runId, { stage: 'taxonomy_screening' });
      const screening = await Promise.allSettled([adapters.indobert.classify(content, run.questionId), adapters.llm.screen(content)]);
      const failures = screening.flatMap((result, index) => result.status === 'rejected' ? [{
        component: index === 0 ? 'indobert' : 'llm',
        code: result.reason?.code || 'screening_failed',
        message: result.reason?.message || 'Screening gagal.',
      }] : []);
      if (failures.length) {
        const error = new Error(failures.map((failure) => `${failure.component}: ${failure.message}`).join(' '));
        error.code = failures.length > 1 ? 'ai_dependencies_unavailable' : failures[0].code;
        error.details = failures;
        throw error;
      }
      const [indobert, llm] = screening.map((result) => result.value);
      const keys = HEADS;
      const agreement = Object.fromEntries(keys.map((key) => [key, indobert.labels[key] === llm.labels[key]]));
      const allAgreement = keys.every((key) => agreement[key]);
      let labels = indobert.labels;
      let adjudication = null;
      if (!allAgreement) {
        await repository.updateRun(runId, { stage: 'adjudication' });
        adjudication = await adapters.llm.adjudicate(content, indobert, llm);
        if (!adjudication.resolved || keys.some((key) => ![indobert.labels[key], llm.labels[key]].includes(adjudication.labels?.[key]))) {
          await repository.finish(runId, 'quarantined', { ...canonicalAudit, summary: { answerVerified: true, decisionType: 'quarantined', taxonomy: null, warnings: ['ai_disagreement'] }, indobert, llm, agreement, adjudication });
          return;
        }
        labels = adjudication.labels;
      }
      await repository.updateRun(runId, { stage: 'risk_evaluation' });
      requireApprovedRiskPolicy(riskPolicy);
      const lowRisk = keys.every((key) => Number.isFinite(indobert.confidences[key])
        && indobert.confidences[key] >= riskPolicy.indobertConfidenceMin[key]
        && Number.isFinite(llm.consistency[key]) && llm.consistency[key] >= riskPolicy.llmConsistencyMin[key]);
      if (!lowRisk) {
        await repository.finish(runId, 'quarantined', { ...canonicalAudit, summary: { answerVerified: true, decisionType: 'quarantined', taxonomy: null, warnings: ['high_uncertainty'] }, indobert, llm, agreement, adjudication, risk: { policyVersion: riskPolicy.policyVersion, accepted: false } });
        return;
      }
      await repository.finish(runId, 'provisional', {
        ...canonicalAudit,
        summary: { answerVerified: true, decisionType: allAgreement ? 'ai_consensus' : 'ai_adjudicated', taxonomy: labels, warnings: [] },
        answerVerification: deterministic.status === 'passed' ? deterministic : { status: 'passed', method: 'llm_solver_ensemble',
          sampleCount: solved.sampleCount, modelVersion: solved.modelVersion, promptVersion: solved.promptVersion, samples: solved.samples },
        indobert, llm, agreement, adjudication, risk: { policyVersion: riskPolicy.policyVersion, accepted: true,
          indobertConfidenceMin: riskPolicy.indobertConfidenceMin, llmConsistencyMin: riskPolicy.llmConsistencyMin },
      });
    } catch (error) {
      await repository.fail(runId, error.code || 'workflow_failed', error.message || 'Workflow gagal.', error.details);
    }
  }

  function enqueue(runId) {
    queue = queue.then(() => execute(runId)).catch((error) => { console.error('Workflow queue error', error); });
    return queue;
  }

  async function recover() {
    const runs = await repository.allRecoverableRuns();
    for (const run of runs) enqueue(run.workflowRunId);
  }

  return { enqueue, recover, execute, drain: () => queue };
}

module.exports = { createWorkflowService };
