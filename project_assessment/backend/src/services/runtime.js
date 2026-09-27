const { FileQuestionRepository } = require('./fileQuestionRepository');
const { createWorkflowService } = require('./questionWorkflow');
const { assertQuestionRepository } = require('./questionRepositoryPort');

const repository = assertQuestionRepository(new FileQuestionRepository());
const workflow = createWorkflowService(repository);

module.exports = { repository, workflow };
