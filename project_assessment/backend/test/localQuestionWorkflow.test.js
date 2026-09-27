const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const os = require('node:os');
const path = require('node:path');
const { randomUUID } = require('node:crypto');
const { FileQuestionRepository } = require('../src/services/fileQuestionRepository');
const { createWorkflowService } = require('../src/services/questionWorkflow');
const { validateQuestion } = require('../src/services/questionValidation');

const owner = 'local-teacher';
const testRiskPolicy = {
  policyVersion: 'test-only', approved_for_provisional: true,
  indobertConfidenceMin: { bloom: 0.7, knowledgeDimension: 0.7, intendedDifficulty: 0.7 },
  llmConsistencyMin: { bloom: 2 / 3, knowledgeDimension: 2 / 3, intendedDifficulty: 2 / 3 },
};
const content = () => ({
  subject: 'Matematika', grade: 8, topic: 'Aljabar', subtopic: 'Persamaan',
  learningObjective: 'Menyelesaikan persamaan sederhana', questionType: 'multiple_choice',
  questionText: 'Hitung hasil dari 2 + 3 dengan tepat.',
  options: [{ id: 'a', text: '5' }, { id: 'b', text: '6' }],
  answerSpec: { kind: 'option_ids', optionIds: ['a'] },
  explanation: '2 + 3 = 5', source: { origin: 'manual' },
});

async function fixture(t) {
  const directory = await fs.mkdtemp(path.join(os.tmpdir(), 'nalar-questions-'));
  t.after(() => fs.rm(directory, { recursive: true, force: true }));
  return new FileQuestionRepository(directory);
}

function adapters({ disagree = false, abstain = false, lowConfidence = false, unavailable = false, llmUnavailable = false } = {}) {
  const labels = { bloom: 'C3', knowledgeDimension: 'procedural', intendedDifficulty: 'Easy' };
  return {
    indobert: { classify: async () => {
      if (unavailable) throw Object.assign(new Error('Artefak tidak tersedia'), { code: 'indobert_artifact_missing' });
      return { labels, confidences: { bloom: lowConfidence ? 0.3 : 0.9, knowledgeDimension: 0.9, intendedDifficulty: 0.9 }, modelVersion: 'test-only' };
    } },
    llm: {
      solve: async () => ({ stable: true, answer: { answerOptionIds: ['a'] }, sampleCount: 3, modelVersion: 'test-only' }),
      screen: async () => {
        if (llmUnavailable) throw Object.assign(new Error('LLM tidak tersedia'), { code: 'llm_not_configured' });
        return { labels: disagree ? { ...labels, bloom: 'C4' } : labels,
          consistency: { bloom: 1, knowledgeDimension: 1, intendedDifficulty: 1 }, modelVersion: 'test-only' };
      },
      adjudicate: async () => ({ resolved: !abstain, labels, modelVersion: 'test-only' }),
    },
  };
}

test('validation reports the exact unknown answer option', () => {
  const invalid = content(); invalid.answerSpec.optionIds = ['missing'];
  assert.deepEqual(validateQuestion(invalid).errors[0].path, '/answerSpec/optionIds/0');
});

test('numeric question validates without multiple-choice options', () => {
  const numeric = content();
  numeric.questionType = 'numeric';
  numeric.answerSpec = { kind: 'numeric', value: 5, tolerance: 0, unit: null };
  delete numeric.options;
  assert.equal(validateQuestion(numeric).valid, true);
});

test('file repository persists across instances and versions are immutable', async (t) => {
  const repo = await fixture(t);
  const first = await repo.create(content(), owner, randomUUID());
  const repeated = await repo.get(first.questionId, owner);
  assert.equal(repeated.contentVersion, 1);
  const old = await repo.getVersion(first.questionId, 1);
  const nextContent = content(); nextContent.questionText = 'Hitung hasil dari 4 + 5 dengan tepat.';
  const second = await repo.replace(first.questionId, owner, 1, nextContent, randomUUID());
  assert.equal(second.contentVersion, 2);
  assert.equal((await repo.getVersion(first.questionId, 1)).contentHash, old.contentHash);
  await assert.rejects(repo.replace(first.questionId, owner, 1, content(), randomUUID()), { code: 'content_version_conflict' });
  const reopened = new FileQuestionRepository(repo.root);
  assert.equal((await reopened.get(first.questionId, owner)).authoringContent.questionText, nextContent.questionText);
});

for (const [name, config, expectedStatus, expectedDecision] of [
  ['agreement', {}, 'provisional', 'ai_consensus'],
  ['resolved disagreement', { disagree: true }, 'provisional', 'ai_adjudicated'],
  ['unresolved disagreement', { disagree: true, abstain: true }, 'quarantined', 'quarantined'],
  ['high uncertainty', { lowConfidence: true }, 'quarantined', 'quarantined'],
]) {
  test(`workflow ${name}`, async (t) => {
    const repo = await fixture(t);
    const question = await repo.create(content(), owner, randomUUID());
    const accepted = await repo.submit(question.questionId, owner, randomUUID());
    const worker = createWorkflowService(repo, adapters(config), testRiskPolicy);
    await worker.enqueue(accepted.workflowRunId);
    const saved = await repo.get(question.questionId, owner);
    assert.equal(saved.status, expectedStatus);
    assert.equal(saved.workflowSummary.decisionType, expectedDecision);
    assert.equal((await repo.getRun(accepted.workflowRunId, owner)).status, 'succeeded');
  });
}

test('unavailable model fails workflow without provisional promotion and permits retry', async (t) => {
  const repo = await fixture(t);
  const question = await repo.create(content(), owner, randomUUID());
  const accepted = await repo.submit(question.questionId, owner, randomUUID());
  await createWorkflowService(repo, adapters({ unavailable: true }), testRiskPolicy).enqueue(accepted.workflowRunId);
  assert.equal((await repo.get(question.questionId, owner)).status, 'submitted');
  assert.equal((await repo.getRun(accepted.workflowRunId, owner)).error.code, 'indobert_artifact_missing');
  const retried = await repo.submit(question.questionId, owner, randomUUID());
  assert.notEqual(retried.workflowRunId, accepted.workflowRunId);
});

test('missing IndoBERT and LLM are reported together', async (t) => {
  const repo = await fixture(t);
  const question = await repo.create(content(), owner, randomUUID());
  const accepted = await repo.submit(question.questionId, owner, randomUUID());
  await createWorkflowService(repo, adapters({ unavailable: true, llmUnavailable: true }), testRiskPolicy).enqueue(accepted.workflowRunId);
  const run = await repo.getRun(accepted.workflowRunId, owner);
  assert.equal(run.error.code, 'ai_dependencies_unavailable');
  assert.deepEqual(run.error.details.map((item) => item.component), ['indobert', 'llm']);
  assert.equal((await repo.get(question.questionId, owner)).workflowSummary, null);
});

test('unapproved risk thresholds block provisional even when test classifiers agree', async (t) => {
  const repo = await fixture(t);
  const question = await repo.create(content(), owner, randomUUID());
  const accepted = await repo.submit(question.questionId, owner, randomUUID());
  await createWorkflowService(repo, adapters()).enqueue(accepted.workflowRunId);
  assert.equal((await repo.getRun(accepted.workflowRunId, owner)).error.code, 'risk_policy_unapproved');
  assert.equal((await repo.get(question.questionId, owner)).status, 'submitted');
});

test('a verified answer conflict is quarantined before taxonomy screening', async (t) => {
  const repo = await fixture(t);
  const question = await repo.create(content(), owner, randomUUID());
  const accepted = await repo.submit(question.questionId, owner, randomUUID());
  const simulated = adapters();
  simulated.indobert.verifyAnswer = async () => ({ status: 'conflict', method: 'test-verifier' });
  simulated.llm.screen = async () => { throw new Error('Screening should not run after answer conflict'); };
  await createWorkflowService(repo, simulated, testRiskPolicy).enqueue(accepted.workflowRunId);
  const result = await repo.get(question.questionId, owner);
  assert.equal(result.status, 'quarantined');
  assert.equal(result.workflowSummary.answerVerified, false);
});

test('idempotency returns the same draft and rejects a different payload', async (t) => {
  const repo = await fixture(t); const key = randomUUID();
  const first = await repo.create(content(), owner, key);
  assert.equal((await repo.create(content(), owner, key)).questionId, first.questionId);
  const changed = content(); changed.topic = 'Geometri';
  await assert.rejects(repo.create(changed, owner, key), { code: 'idempotency_conflict' });
});

test('draft revision is idempotent even after its original If-Match version is stale', async (t) => {
  const repo = await fixture(t);
  const first = await repo.create(content(), owner, randomUUID());
  const key = randomUUID();
  const changed = content(); changed.topic = 'Geometri';
  const revised = await repo.replace(first.questionId, owner, 1, changed, key);
  assert.equal(revised.contentVersion, 2);
  assert.deepEqual(await repo.replace(first.questionId, owner, 1, changed, key), revised);
  await assert.rejects(repo.replace(first.questionId, owner, 1, content(), key), { code: 'idempotency_conflict' });
});

test('a run superseded by an edit cannot promote an older question version', async (t) => {
  const repo = await fixture(t);
  const question = await repo.create(content(), owner, randomUUID());
  const accepted = await repo.submit(question.questionId, owner, randomUUID());
  const changed = content(); changed.topic = 'Geometri';
  await repo.replace(question.questionId, owner, 1, changed, randomUUID());
  await repo.finish(accepted.workflowRunId, 'provisional', { summary: { decisionType: 'ai_consensus' } });
  assert.equal((await repo.get(question.questionId, owner)).status, 'author_draft');
  assert.equal((await repo.getRun(accepted.workflowRunId, owner)).error.code, 'workflow_superseded');
});

test('queued run is recovered from disk after a worker restart', async (t) => {
  const repo = await fixture(t);
  const question = await repo.create(content(), owner, randomUUID());
  const accepted = await repo.submit(question.questionId, owner, randomUUID());
  const restarted = createWorkflowService(new FileQuestionRepository(repo.root), adapters(), testRiskPolicy);
  await restarted.recover();
  await restarted.drain();
  assert.equal((await repo.getRun(accepted.workflowRunId, owner)).status, 'succeeded');
  assert.equal((await repo.get(question.questionId, owner)).status, 'provisional');
});
