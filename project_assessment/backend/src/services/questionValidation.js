const Ajv2020 = require('ajv/dist/2020');
const schemaBundle = require('../../../../API_DOCUMENTATION/schemas/nalar-api.schema.json');

const ajv = new Ajv2020({ allErrors: true, strict: false });
const validateShape = ajv.compile({
  ...schemaBundle.$defs.QuestionAuthoringContent,
  $defs: schemaBundle.$defs,
});

function validateQuestion(content) {
  const shapeValid = validateShape(content);
  const errors = shapeValid ? [] : validateShape.errors.map((error) => ({
    path: error.instancePath || '/',
    code: error.keyword,
    message: error.message || 'Nilai tidak valid.',
  }));
  if (!shapeValid) return { valid: false, errors, warnings: [] };

  for (const field of ['topic', 'subtopic', 'learningObjective', 'questionText']) {
    if (!content[field].trim()) errors.push({ path: `/${field}`, code: 'blank_text', message: 'Teks tidak boleh hanya berisi spasi.' });
  }

  if (['multiple_choice', 'multiple_response', 'true_false'].includes(content.questionType)) {
    const ids = content.options?.map((option) => option.id) || [];
    if (new Set(ids).size !== ids.length) errors.push({ path: '/options', code: 'duplicate_option_id', message: 'ID opsi harus unik.' });
    if (content.answerSpec.kind !== 'option_ids') errors.push({ path: '/answerSpec', code: 'answer_type', message: 'Tipe soal ini memerlukan kunci berupa ID opsi.' });
    const optionTexts = content.options?.map((option) => option.text.normalize('NFKC').trim().toLowerCase()) || [];
    if (optionTexts.some((text) => !text)) errors.push({ path: '/options', code: 'blank_option', message: 'Teks opsi tidak boleh kosong.' });
    if (new Set(optionTexts).size !== optionTexts.length) errors.push({ path: '/options', code: 'duplicate_option_text', message: 'Teks opsi harus berbeda.' });
    const selected = content.answerSpec.optionIds || [];
    selected.forEach((id, index) => {
      if (!ids.includes(id)) errors.push({ path: `/answerSpec/optionIds/${index}`, code: 'unknown_option_id', message: 'Jawaban harus merujuk pada opsi yang tersedia.' });
    });
    if (content.questionType !== 'multiple_response' && selected.length !== 1) {
      errors.push({ path: '/answerSpec/optionIds', code: 'answer_count', message: 'Tipe soal ini memerlukan tepat satu jawaban.' });
    }
    if (content.questionType === 'multiple_response' && selected.length < 2) {
      errors.push({ path: '/answerSpec/optionIds', code: 'answer_count', message: 'Pilih sedikitnya dua jawaban.' });
    }
  }
  if (content.questionType === 'numeric' && content.answerSpec.kind !== 'numeric') {
    errors.push({ path: '/answerSpec', code: 'answer_type', message: 'Soal numerik memerlukan jawaban numerik.' });
  }
  if (['short_answer', 'essay'].includes(content.questionType) && content.answerSpec.kind !== 'text') {
    errors.push({ path: '/answerSpec', code: 'answer_type', message: 'Tipe ini memerlukan spesifikasi jawaban teks.' });
  }
  if (content.questionType === 'matching') {
    errors.push({ path: '/questionType', code: 'unsupported_type', message: 'Tipe matching belum didukung pada tahap ini.' });
  }
  return { valid: errors.length === 0, errors, warnings: [] };
}

module.exports = { validateQuestion };
