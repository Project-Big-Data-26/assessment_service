const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const os = require('node:os');
const path = require('node:path');
const { randomUUID } = require('node:crypto');

const directory = require('node:fs').mkdtempSync(path.join(os.tmpdir(), 'nalar-http-'));
process.env.QUESTION_DATA_DIR = directory;
process.env.AI_SERVICE_URL = 'http://127.0.0.1:1';
const app = require('../src/app');

const content = () => ({
  subject: 'Matematika', grade: 8, topic: 'Aritmetika', subtopic: 'Penjumlahan',
  learningObjective: 'Menghitung penjumlahan bilangan', questionType: 'multiple_choice',
  questionText: 'Hitung hasil dari 2 + 3.',
  options: [{ id: 'a', text: '5' }, { id: 'b', text: '6' }],
  answerSpec: { kind: 'option_ids', optionIds: ['a'] },
  explanation: '2 + 3 = 5', source: { origin: 'manual' },
});

test('HTTP teacher authoring survives reload and reports missing AI dependency', async (t) => {
  const server = app.listen(0, '127.0.0.1');
  await new Promise((resolve) => server.once('listening', resolve));
  t.after(async () => {
    await new Promise((resolve) => server.close(resolve));
    await fs.rm(directory, { recursive: true, force: true });
  });
  const base = `http://127.0.0.1:${server.address().port}/api/v1`;
  async function call(route, method = 'GET', body, headers = {}) {
    const response = await fetch(`${base}${route}`, {
      method, headers: { ...(body ? { 'content-type': 'application/json' } : {}), ...headers },
      ...(body ? { body: JSON.stringify(body) } : {}),
    });
    return { status: response.status, data: await response.json() };
  }

  const invalid = content(); invalid.answerSpec.optionIds = ['missing'];
  const validation = await call('/questions/validate', 'POST', invalid);
  assert.equal(validation.status, 200);
  assert.equal(validation.data.valid, false);
  assert.equal(validation.data.errors[0].path, '/answerSpec/optionIds/0');
  const rejected = await call('/questions', 'POST', invalid, { 'Idempotency-Key': randomUUID() });
  assert.equal(rejected.status, 422);
  assert.equal(rejected.data.error.code, 'validation_failed');

  const createKey = randomUUID();
  const created = await call('/questions', 'POST', content(), { 'Idempotency-Key': createKey });
  assert.equal(created.status, 201);
  assert.equal(created.data.status, 'author_draft');
  const repeated = await call('/questions', 'POST', content(), { 'Idempotency-Key': createKey });
  assert.equal(repeated.data.questionId, created.data.questionId);

  const id = created.data.questionId;
  const edited = content(); edited.topic = 'Bilangan';
  const changed = await call(`/questions/${id}/draft`, 'PUT', edited, { 'If-Match': '"1"', 'Idempotency-Key': randomUUID() });
  assert.equal(changed.status, 200);
  assert.equal(changed.data.contentVersion, 2);
  const stale = await call(`/questions/${id}/draft`, 'PUT', content(), { 'If-Match': '"1"', 'Idempotency-Key': randomUUID() });
  assert.equal(stale.status, 409);
  assert.equal(stale.data.error.code, 'content_version_conflict');
  const loaded = await call(`/questions/${id}`);
  assert.equal(loaded.data.authoringContent.topic, 'Bilangan');
  const list = await call('/questions');
  assert.equal(list.data.items.length, 1);

  const accepted = await call(`/questions/${id}/submit`, 'POST', undefined, { 'Idempotency-Key': randomUUID() });
  assert.equal(accepted.status, 202);
  assert.match(accepted.data.workflowRunId, /^WF-/);
  let run;
  for (let attempt = 0; attempt < 30; attempt += 1) {
    run = (await call(`/workflow-runs/${accepted.data.workflowRunId}`)).data;
    if (run.status === 'failed') break;
    await new Promise((resolve) => setTimeout(resolve, 50));
  }
  assert.equal(run.status, 'failed');
  assert.equal(run.error.code, 'answer_verifier_unavailable');
  const after = await call(`/questions/${id}`);
  assert.equal(after.data.status, 'submitted');
  assert.equal(after.data.workflowSummary, null);
  assert.equal(after.data.workflowRunId, accepted.data.workflowRunId);
});
