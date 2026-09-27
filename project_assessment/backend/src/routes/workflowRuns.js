const express = require('express');
const { repository } = require('../services/runtime');

const router = express.Router();
router.get('/:runId', async (req, res, next) => {
  try {
    const run = await repository.getRun(req.params.runId, process.env.LOCAL_TEACHER_ID || 'local-teacher');
    if (!run) return res.status(404).json({ error: { code: 'workflow_not_found', message: 'Workflow tidak ditemukan.', traceId: req.traceId } });
    res.json(run);
  } catch (error) { next(error); }
});
module.exports = router;
