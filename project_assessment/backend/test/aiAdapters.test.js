const test = require('node:test');
const assert = require('node:assert/strict');
const { getLlmConfig, indobertAdapter, llmAdapter } = require('../src/services/aiAdapters');

const LLM_ENV_KEYS = ['LLM_PROVIDER', 'LLM_BASE_URL', 'GEMINI_API_KEY', 'LLM_API_KEY', 'LLM_SCREEN_MODEL',
  'LLM_SOLVER_MODEL', 'LLM_ADJUDICATOR_MODEL', 'LLM_REASONING_EFFORT', 'LLM_MIN_REQUEST_INTERVAL_MS',
  'LLM_MAX_ATTEMPTS', 'LLM_RETRY_BASE_MS'];
function snapshotEnv() { return Object.fromEntries(LLM_ENV_KEYS.map((key) => [key, process.env[key]])); }
function restoreEnv(snapshot) {
  for (const key of LLM_ENV_KEYS) {
    if (snapshot[key] === undefined) delete process.env[key]; else process.env[key] = snapshot[key];
  }
}

test('rules baseline and unapproved artifact cannot enter real IndoBERT screening', async () => {
  const originalFetch = global.fetch;
  let calls = 0;
  try {
    global.fetch = async () => {
      calls += 1;
      return { ok: true, json: async () => ({ classifier: 'RuleBasedBaselineClassifier', artifact_ready: false }) };
    };
    await assert.rejects(indobertAdapter.classify({ questionText: 'Hitung 2 + 3.', options: [] }, 'Q-test'), { code: 'indobert_artifact_missing' });
    global.fetch = async () => {
      calls += 1;
      return { ok: true, json: async () => ({ classifier: 'IndoBERTClassifier', artifact_ready: true, provisional_eligible: false }) };
    };
    await assert.rejects(indobertAdapter.classify({ questionText: 'Hitung 2 + 3.', options: [] }, 'Q-test'), { code: 'indobert_artifact_unapproved' });
    assert.equal(calls, 2);
  } finally { global.fetch = originalFetch; }
});

test('screening LLM refuses to run without provider configuration', async () => {
  const previous = snapshotEnv();
  try {
    for (const key of LLM_ENV_KEYS) delete process.env[key];
    await assert.rejects(llmAdapter.screen({ questionText: 'Hitung 2 + 3.' }), { code: 'llm_not_configured' });
  } finally { restoreEnv(previous); }
});

test('Gemini provider supplies safe defaults and sends strict JSON schema', async () => {
  const previous = snapshotEnv();
  const originalFetch = global.fetch;
  let request;
  try {
    for (const key of LLM_ENV_KEYS) delete process.env[key];
    process.env.LLM_PROVIDER = 'gemini';
    process.env.GEMINI_API_KEY = 'test-only-secret';
    global.fetch = async (url, options) => {
      request = { url, options, body: JSON.parse(options.body) };
      return { ok: true, json: async () => ({ choices: [{ message: { content: '{"status":"ok"}' } }] }) };
    };
    const config = getLlmConfig();
    assert.equal(config.screenModel, 'gemini-3.8-flash');
    const result = await llmAdapter.healthCheck();
    assert.equal(result.provider, 'gemini');
    assert.equal(request.url, 'https://generativelanguage.googleapis.com/v1beta/openai/chat/completions');
    assert.equal(request.options.headers.authorization, 'Bearer test-only-secret');
    assert.equal(request.body.response_format.type, 'json_schema');
    assert.equal(request.body.response_format.json_schema.strict, true);
    assert.equal(request.body.reasoning_effort, 'low');
  } finally {
    global.fetch = originalFetch;
    restoreEnv(previous);
  }
});

test('daily Gemini quota is identified and is not retried immediately', async () => {
  const previous = snapshotEnv();
  const originalFetch = global.fetch;
  let calls = 0;
  try {
    for (const key of LLM_ENV_KEYS) delete process.env[key];
    process.env.LLM_PROVIDER = 'gemini';
    process.env.GEMINI_API_KEY = 'test-only-secret';
    global.fetch = async () => {
      calls += 1;
      return {
        ok: false, status: 429, headers: { get: () => null },
        json: async () => ({ error: { status: 'RESOURCE_EXHAUSTED', message: 'Requests per day quota exhausted.' } }),
      };
    };
    await assert.rejects(llmAdapter.healthCheck(), (error) => {
      assert.equal(error.code, 'llm_rate_limited');
      assert.equal(error.providerStatus, 'RESOURCE_EXHAUSTED');
      assert.equal(error.rateLimitScope, 'daily');
      return true;
    });
    assert.equal(calls, 1);
  } finally {
    global.fetch = originalFetch;
    restoreEnv(previous);
  }
});
