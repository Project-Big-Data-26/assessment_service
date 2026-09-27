const express = require('express');
const { validateQuestion } = require('../services/questionValidation');
const { repository, workflow } = require('../services/runtime');

const router = express.Router();
const owner = () => process.env.LOCAL_TEACHER_ID || 'local-teacher';

function requireIdempotency(req) {
  const key = req.get('Idempotency-Key');
  if (!key || !/^[a-zA-Z0-9-]{8,100}$/.test(key)) {
    const error = new Error('Idempotency-Key wajib diisi.'); error.code = 'idempotency_key_required'; error.status = 400; throw error;
  }
  return key;
}

function requireValid(body) {
  const result = validateQuestion(body);
  if (!result.valid) {
    const error = new Error('Konten soal tidak valid.'); error.code = 'validation_failed'; error.status = 422; error.details = result.errors; throw error;
  }
}

router.post('/validate', (req, res) => res.json(validateQuestion(req.body)));

router.post('/', async (req, res, next) => {
  try { requireValid(req.body); res.status(201).json(await repository.create(req.body, owner(), requireIdempotency(req))); }
  catch (error) { next(error); }
});

router.get('/', async (req, res, next) => {
  try { res.json({ items: await repository.list(owner(), req.query.status), nextCursor: null }); }
  catch (error) { next(error); }
});

router.get('/:questionId', async (req, res, next) => {
  try {
    const question = await repository.get(req.params.questionId, owner());
    if (!question) return res.status(404).json({ error: { code: 'question_not_found', message: 'Soal tidak ditemukan.', traceId: req.traceId } });
    res.json(question);
  } catch (error) { next(error); }
});

router.put('/:questionId/draft', async (req, res, next) => {
  try {
    requireValid(req.body);
    const match = req.get('If-Match');
    if (!match || !/^"?\d+"?$/.test(match)) return res.status(400).json({ error: { code: 'if_match_required', message: 'If-Match harus berisi contentVersion.', traceId: req.traceId } });
    res.json(await repository.replace(req.params.questionId, owner(), Number(match.replaceAll('"', '')), req.body, requireIdempotency(req)));
  } catch (error) { next(error); }
});

router.post('/:questionId/submit', async (req, res, next) => {
  try {
    const result = await repository.submit(req.params.questionId, owner(), requireIdempotency(req));
    workflow.enqueue(result.workflowRunId);
    res.status(202).json(result);
  } catch (error) { next(error); }
});

router.get('/:questionId/ai-decisions', async (req, res, next) => {
  try {
    const question = await repository.get(req.params.questionId, owner());
    if (!question) return res.status(404).json({ error: { code: 'question_not_found', message: 'Soal tidak ditemukan.', traceId: req.traceId } });
    res.json({ questionId: question.questionId, contentVersion: question.contentVersion, workflowSummary: question.workflowSummary });
  } catch (error) { next(error); }
});

module.exports = router;
