// Contract shared by the local file store and a future MongoDB implementation.
// The worker receives this port; it never imports a storage driver directly.
const METHODS = [
  'create', 'get', 'list', 'replace', 'submit', 'getRun', 'allRecoverableRuns',
  'updateRun', 'finish', 'fail', 'getVersion',
];

function assertQuestionRepository(repository) {
  const missing = METHODS.filter((method) => typeof repository?.[method] !== 'function');
  if (missing.length) throw new TypeError(`QuestionRepository missing methods: ${missing.join(', ')}`);
  return repository;
}

module.exports = { assertQuestionRepository };
