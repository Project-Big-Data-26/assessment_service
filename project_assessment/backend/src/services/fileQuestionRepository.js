const fs = require('node:fs/promises');
const path = require('node:path');
const { randomUUID, createHash } = require('node:crypto');

const DEFAULT_ROOT = path.resolve(__dirname, '../../../../data/local');

class DomainError extends Error {
  constructor(code, status = 409, message = code) {
    super(message);
    this.code = code;
    this.status = status;
  }
}

async function readJson(file) {
  try { return JSON.parse(await fs.readFile(file, 'utf8')); }
  catch (error) { if (error.code === 'ENOENT') return null; throw error; }
}

async function atomicJson(file, value) {
  await fs.mkdir(path.dirname(file), { recursive: true });
  const temporary = `${file}.${randomUUID()}.tmp`;
  try {
    await fs.writeFile(temporary, JSON.stringify(value, null, 2), { encoding: 'utf8', flag: 'wx' });
    await fs.rename(temporary, file);
  } finally { await fs.rm(temporary, { force: true }); }
}

function hash(value) { return createHash('sha256').update(JSON.stringify(value)).digest('hex'); }
function safeId(value, prefix) {
  if (typeof value !== 'string' || !new RegExp(`^${prefix}-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`, 'i').test(value)) {
    throw new DomainError('invalid_resource_id', 400);
  }
  return value;
}

class FileQuestionRepository {
  constructor(root = process.env.QUESTION_DATA_DIR || DEFAULT_ROOT) {
    this.root = path.resolve(root);
    this.pending = Promise.resolve();
  }

  locked(action) {
    const result = this.pending.then(action);
    this.pending = result.catch(() => {});
    return result;
  }

  identityFile(id) { return path.join(this.root, 'questions', safeId(id, 'Q'), 'identity.json'); }
  versionFile(id, version) { return path.join(this.root, 'questions', safeId(id, 'Q'), 'versions', `${String(version).padStart(6, '0')}.json`); }
  runFile(id) { return path.join(this.root, 'workflow-runs', `${safeId(id, 'WF')}.json`); }
  decisionFile(id) { return path.join(this.root, 'ai-decisions', `${safeId(id, 'AID')}.json`); }
  idempotencyFile(scope, key) { return path.join(this.root, 'idempotency', `${hash(`${scope}:${key}`)}.json`); }

  async idempotent(scope, key, input, action) {
    const file = this.idempotencyFile(scope, key);
    const existing = await readJson(file);
    const requestHash = hash(input);
    if (existing) {
      if (existing.requestHash !== requestHash) throw new DomainError('idempotency_conflict');
      return existing.result;
    }
    const result = await action();
    await atomicJson(file, { requestHash, result });
    return result;
  }

  async create(content, ownerId, key) {
    return this.locked(() => this.idempotent(`create:${ownerId}`, key, content, async () => {
      const questionId = `Q-${randomUUID()}`;
      const now = new Date().toISOString();
      const identity = { questionId, ownerUserId: ownerId, contentVersion: 1, status: 'author_draft', activeWorkflowRunId: null, activeDecisionId: null, createdAt: now, updatedAt: now };
      await atomicJson(this.versionFile(questionId, 1), { questionId, contentVersion: 1, authoringContent: content, contentHash: hash(content), createdBy: ownerId, createdAt: now });
      await atomicJson(this.identityFile(questionId), identity);
      const { ownerUserId, activeWorkflowRunId, activeDecisionId, ...publicIdentity } = identity;
      return { ...publicIdentity, workflowRunId: null, authoringContent: content, workflowSummary: null };
    }));
  }

  async get(questionId, ownerId) {
    const identity = await readJson(this.identityFile(questionId));
    if (!identity || identity.ownerUserId !== ownerId) return null;
    const version = await readJson(this.versionFile(questionId, identity.contentVersion));
    if (!version) throw new DomainError('content_version_missing', 500);
    const decision = identity.activeDecisionId ? await readJson(this.decisionFile(identity.activeDecisionId)) : null;
    const { ownerUserId, activeWorkflowRunId, activeDecisionId, ...safeIdentity } = identity;
    return { ...safeIdentity, workflowRunId: activeWorkflowRunId, authoringContent: version.authoringContent, workflowSummary: decision?.summary || null };
  }

  async list(ownerId, status) {
    const directory = path.join(this.root, 'questions');
    let entries;
    try { entries = await fs.readdir(directory, { withFileTypes: true }); }
    catch (error) { if (error.code === 'ENOENT') return []; throw error; }
    const questions = await Promise.all(entries.filter((item) => item.isDirectory()).map((item) => this.get(item.name, ownerId)));
    return questions.filter((item) => item && (!status || item.status === status)).sort((a, b) => b.updatedAt.localeCompare(a.updatedAt));
  }

  async replace(questionId, ownerId, expectedVersion, content, key) {
    return this.locked(() => this.idempotent(`replace:${questionId}:${ownerId}`, key, { expectedVersion, content }, async () => {
      const identity = await readJson(this.identityFile(questionId));
      if (!identity || identity.ownerUserId !== ownerId) throw new DomainError('question_not_found', 404);
      if (identity.contentVersion !== expectedVersion) throw new DomainError('content_version_conflict');
      const version = expectedVersion + 1;
      const now = new Date().toISOString();
      const versionPath = this.versionFile(questionId, version);
      const orphanedVersion = await readJson(versionPath);
      if (orphanedVersion && orphanedVersion.contentHash !== hash(content)) throw new DomainError('immutable_version_conflict');
      if (!orphanedVersion) await atomicJson(versionPath, { questionId, contentVersion: version, authoringContent: content, contentHash: hash(content), createdBy: ownerId, createdAt: now });
      await atomicJson(this.identityFile(questionId), { ...identity, contentVersion: version, status: 'author_draft', activeWorkflowRunId: null, activeDecisionId: null, updatedAt: now });
      return this.get(questionId, ownerId);
    }));
  }

  async submit(questionId, ownerId, key) {
    return this.locked(async () => {
      const identity = await readJson(this.identityFile(questionId));
      if (!identity || identity.ownerUserId !== ownerId) throw new DomainError('question_not_found', 404);
      return this.idempotent(`submit:${questionId}:${identity.contentVersion}`, key, { questionId, contentVersion: identity.contentVersion }, async () => {
        if (!['author_draft', 'submitted'].includes(identity.status)) throw new DomainError('invalid_question_state');
        if (identity.activeWorkflowRunId) {
          const prior = await readJson(this.runFile(identity.activeWorkflowRunId));
          if (prior && !['failed'].includes(prior.status)) throw new DomainError('workflow_already_submitted');
        }
        const workflowRunId = `WF-${randomUUID()}`;
        const now = new Date().toISOString();
        await atomicJson(this.runFile(workflowRunId), { workflowRunId, questionId, contentVersion: identity.contentVersion, ownerUserId: ownerId, status: 'queued', stage: 'queued', error: null, createdAt: now, updatedAt: now });
        await atomicJson(this.identityFile(questionId), { ...identity, status: 'submitted', activeWorkflowRunId: workflowRunId, updatedAt: now });
        return { questionId, contentVersion: identity.contentVersion, status: 'submitted', workflowRunId, statusUrl: `/api/v1/workflow-runs/${workflowRunId}` };
      });
    });
  }

  async getRun(runId, ownerId) {
    const run = await readJson(this.runFile(runId));
    if (!run || run.ownerUserId !== ownerId) return null;
    const { ownerUserId, ...safeRun } = run;
    return safeRun;
  }

  async allRecoverableRuns() {
    let names;
    try { names = await fs.readdir(path.join(this.root, 'workflow-runs')); }
    catch (error) { if (error.code === 'ENOENT') return []; throw error; }
    const runs = await Promise.all(names.filter((name) => name.endsWith('.json')).map((name) => readJson(path.join(this.root, 'workflow-runs', name))));
    return runs.filter((run) => run && ['queued', 'running'].includes(run.status));
  }

  async updateRun(runId, patch) {
    return this.locked(async () => {
      const run = await readJson(this.runFile(runId));
      if (!run) throw new DomainError('workflow_not_found', 404);
      const updated = { ...run, ...patch, updatedAt: new Date().toISOString() };
      await atomicJson(this.runFile(runId), updated);
      return updated;
    });
  }

  async finish(runId, questionStatus, decision) {
    return this.locked(async () => {
      const run = await readJson(this.runFile(runId));
      if (!run) throw new DomainError('workflow_not_found', 404);
      const identity = await readJson(this.identityFile(run.questionId));
      if (!identity || identity.contentVersion !== run.contentVersion || identity.activeWorkflowRunId !== runId) {
        await atomicJson(this.runFile(runId), { ...run, status: 'failed', error: { code: 'workflow_superseded', message: 'Versi soal berubah saat workflow berjalan.' }, updatedAt: new Date().toISOString() });
        return;
      }
      let decisionId = null;
      if (decision) {
        decisionId = `AID-${runId.slice(3)}`;
        if (!await readJson(this.decisionFile(decisionId))) {
          await atomicJson(this.decisionFile(decisionId), { decisionId, questionId: run.questionId, contentVersion: run.contentVersion, workflowRunId: runId, ...decision, createdAt: new Date().toISOString() });
        }
      }
      await atomicJson(this.identityFile(run.questionId), { ...identity, status: questionStatus, activeDecisionId: decisionId, updatedAt: new Date().toISOString() });
      await atomicJson(this.runFile(runId), { ...run, status: 'succeeded', stage: 'completed', decisionId, updatedAt: new Date().toISOString() });
    });
  }

  async fail(runId, code, message, details = null) {
    return this.locked(async () => {
      const run = await readJson(this.runFile(runId));
      if (!run) return;
      const identity = await readJson(this.identityFile(run.questionId));
      if (identity?.activeWorkflowRunId === runId && identity.contentVersion === run.contentVersion) {
        await atomicJson(this.identityFile(run.questionId), { ...identity, status: 'submitted', updatedAt: new Date().toISOString() });
      }
      await atomicJson(this.runFile(runId), { ...run, status: 'failed', stage: run.stage, error: { code, message, details }, updatedAt: new Date().toISOString() });
    });
  }

  async getVersion(questionId, version) { return readJson(this.versionFile(questionId, version)); }
}

module.exports = { FileQuestionRepository, DomainError };
