const API_BASE = import.meta.env.VITE_API_URL || "/api/v1";

async function request(path, options = {}) {
  const response = await fetch(`${API_BASE}${path}`, options);
  const payload = await response.json().catch(() => ({}));
  if (!response.ok) {
    const error = new Error(payload.error?.message || payload.message || payload.detail || `Request failed (${response.status})`);
    error.code = payload.error?.code || payload.error || "unknown";
    error.details = payload.error?.details || payload.details || [];
    throw error;
  }
  return payload;
}

export function saveQuestion(payload) {
  return request("/questions", { method: "POST", headers: { "content-type": "application/json", "Idempotency-Key": crypto.randomUUID() }, body: JSON.stringify(payload) });
}
export function validateQuestion(payload) {
  return request("/questions/validate", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(payload) });
}
export function listQuestions() { return request("/questions"); }
export function getQuestion(questionId) { return request(`/questions/${encodeURIComponent(questionId)}`); }
export function replaceDraft(questionId, version, payload) {
  return request(`/questions/${encodeURIComponent(questionId)}/draft`, { method: "PUT", headers: { "content-type": "application/json", "If-Match": `"${version}"`, "Idempotency-Key": crypto.randomUUID() }, body: JSON.stringify(payload) });
}
export function submitQuestion(questionId) {
  return request(`/questions/${encodeURIComponent(questionId)}/submit`, { method: "POST", headers: { "Idempotency-Key": crypto.randomUUID() } });
}
export function getWorkflowRun(runId) { return request(`/workflow-runs/${encodeURIComponent(runId)}`); }
export function classifyQuestion(payload) {
  return request("/ai/classify-question", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(payload) });
}
export function extractSource(file) {
  const body = new FormData(); body.append("file", file);
  return request("/ai/extract", { method: "POST", body });
}
export function recordStudentResponse(payload) {
  return request("/responses", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(payload) });
}
