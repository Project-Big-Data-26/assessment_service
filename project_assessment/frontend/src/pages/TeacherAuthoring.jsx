import { useEffect, useState } from "react";
import MathText from "../components/MathText";
import { getQuestion, getWorkflowRun, listQuestions, replaceDraft, saveQuestion, submitQuestion, validateQuestion } from "../services/api";

const blankOptions = () => [1, 2, 3, 4].map((number) => ({ id: `opt-${number}`, text: "" }));

const blank = () => ({
  subject: "Matematika", grade: 8, topic: "", subtopic: "", learningObjective: "",
  questionType: "multiple_choice", questionText: "",
  options: blankOptions(),
  answerSpec: { kind: "option_ids", optionIds: ["opt-1"] }, explanation: "", source: { origin: "manual" },
});

export default function TeacherAuthoring() {
  const [form, setForm] = useState(blank);
  const [question, setQuestion] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [run, setRun] = useState(null);
  const [errors, setErrors] = useState([]);
  const [notice, setNotice] = useState("");
  const [busy, setBusy] = useState(false);
  const hasUnsavedChanges = question && JSON.stringify(form) !== JSON.stringify(question.authoringContent);

  async function refreshList() {
    try { setQuestions((await listQuestions()).items); }
    catch (error) { setNotice(error.message); }
  }

  useEffect(() => {
    let active = true;
    listQuestions().then((result) => { if (active) setQuestions(result.items); })
      .catch((error) => { if (active) setNotice(error.message); });
    return () => { active = false; };
  }, []);

  useEffect(() => {
    if (!run?.workflowRunId || !["queued", "running"].includes(run.status)) return undefined;
    const timer = setInterval(async () => {
      try {
        const next = await getWorkflowRun(run.workflowRunId);
        setRun(next);
        if (!["queued", "running"].includes(next.status)) {
          const saved = await getQuestion(next.questionId);
          setQuestion(saved);
          refreshList();
        }
      } catch (error) { setNotice(error.message); }
    }, 1500);
    return () => clearInterval(timer);
  }, [run?.workflowRunId, run?.status]);

  function setField(field, value) { setForm((current) => ({ ...current, [field]: value })); }
  function changeType(type) {
    setForm((current) => {
      if (type === "numeric") {
        const withoutOptions = { ...current };
        delete withoutOptions.options;
        return { ...withoutOptions, questionType: type, answerSpec: { kind: "numeric", value: 0, tolerance: 0, unit: null } };
      }
      const options = current.options?.length ? current.options : blankOptions();
      return { ...current, questionType: type, options, answerSpec: { kind: "option_ids", optionIds: [options[0].id] } };
    });
  }
  function changeOption(index, text) {
    setForm((current) => ({ ...current, options: current.options.map((option, position) => position === index ? { ...option, text } : option) }));
  }

  async function selectQuestion(id) {
    try {
      const saved = await getQuestion(id);
      setQuestion(saved); setForm(saved.authoringContent); setErrors([]); setNotice("");
      setRun(saved.workflowRunId ? await getWorkflowRun(saved.workflowRunId) : null);
    } catch (error) { setNotice(error.message); }
  }

  async function save() {
    setBusy(true); setErrors([]); setNotice("");
    try {
      const validation = await validateQuestion(form);
      if (!validation.valid) { setErrors(validation.errors); return; }
      const saved = question ? await replaceDraft(question.questionId, question.contentVersion, form) : await saveQuestion(form);
      setQuestion(saved); setForm(saved.authoringContent); setRun(null); setNotice(`Draft tersimpan sebagai versi ${saved.contentVersion}.`);
      await refreshList();
    } catch (error) { setErrors(error.details || []); setNotice(error.message); }
    finally { setBusy(false); }
  }

  async function submit() {
    if (!question) { setNotice("Simpan draft sebelum submit."); return; }
    setBusy(true); setNotice("");
    try {
      const accepted = await submitQuestion(question.questionId);
      setRun({ ...accepted, status: "queued", stage: "queued" });
      setQuestion((current) => ({ ...current, status: "submitted", workflowRunId: accepted.workflowRunId }));
      setNotice("Workflow dimulai. Status akan diperbarui otomatis.");
      await refreshList();
    } catch (error) { setNotice(error.message); }
    finally { setBusy(false); }
  }

  function newQuestion() { setQuestion(null); setForm(blank()); setRun(null); setErrors([]); setNotice(""); }

  return <main className="teacher-authoring">
    <div className="teacher-heading">
      <div><span className="teacher-eyebrow">INPUT SOAL SAMPEL</span><h1>Studio penulisan soal</h1><p>Isi dan simpan soal sebagai draft. Klasifikasi otomatis berjalan setelah kamu menekan Submit.</p></div>
      <button type="button" className="teacher-secondary" onClick={newQuestion}>Soal baru</button>
    </div>
    <div className="teacher-layout">
      <section className="teacher-form" aria-label="Form soal">
        <div className="teacher-form-top"><h2>{question ? `Edit ${question.questionId}` : "Draft baru"}</h2>{question && <span>Versi {question.contentVersion} · {question.status}</span>}</div>
        <div className="teacher-two"><label>Kelas<input type="number" min="1" max="12" value={form.grade} onChange={(event) => setField("grade", Number(event.target.value))} /></label>
          <label>Tipe soal<select value={form.questionType} onChange={(event) => changeType(event.target.value)}><option value="multiple_choice">Pilihan ganda</option><option value="numeric">Jawaban numerik</option></select></label></div>
        <div className="teacher-two"><label>Topik<input value={form.topic} onChange={(event) => setField("topic", event.target.value)} /></label><label>Subtopik<input value={form.subtopic} onChange={(event) => setField("subtopic", event.target.value)} /></label></div>
        <label>Tujuan pembelajaran<textarea rows="2" value={form.learningObjective} onChange={(event) => setField("learningObjective", event.target.value)} /></label>
        <label>Teks soal<textarea rows="5" value={form.questionText} onChange={(event) => setField("questionText", event.target.value)} placeholder="Gunakan $...$ untuk rumus LaTeX" /></label>
        {form.questionType === "multiple_choice" ? <div className="teacher-options"><h3>Opsi dan kunci</h3>
          {form.options.map((option, index) => <div className="teacher-option" key={option.id}><input type="radio" name="correct-option" aria-label={`Jadikan opsi ${index + 1} kunci`} checked={form.answerSpec.optionIds[0] === option.id} onChange={() => setField("answerSpec", { kind: "option_ids", optionIds: [option.id] })} /><span>{index + 1}</span><input value={option.text} aria-label={`Teks opsi ${index + 1}`} onChange={(event) => changeOption(index, event.target.value)} /></div>)}
        </div> : <div className="teacher-two"><label>Jawaban angka<input type="number" value={form.answerSpec.value} onChange={(event) => setField("answerSpec", { ...form.answerSpec, value: Number(event.target.value) })} /></label><label>Toleransi<input type="number" min="0" value={form.answerSpec.tolerance || 0} onChange={(event) => setField("answerSpec", { ...form.answerSpec, tolerance: Number(event.target.value) })} /></label></div>}
        <label>Penjelasan / penyelesaian<textarea rows="3" value={form.explanation || ""} onChange={(event) => setField("explanation", event.target.value)} /></label>
        {errors.length > 0 && <div className="teacher-errors" role="alert">{errors.map((error, index) => <p key={`${error.path}-${index}`}><code>{error.path}</code> {error.message}</p>)}</div>}
        {notice && <p className="teacher-notice" role="status">{notice}</p>}
        <div className="teacher-actions"><button type="button" className="teacher-primary" disabled={busy} onClick={save}>{busy ? "Memproses..." : "Simpan draft"}</button><button type="button" className="teacher-secondary" disabled={busy || !question || hasUnsavedChanges || ["queued", "running"].includes(run?.status) || !["author_draft", "submitted"].includes(question.status)} onClick={submit}>Submit ke workflow</button></div>
        {hasUnsavedChanges && <p className="teacher-warning">Simpan perubahan draft sebelum submit.</p>}
      </section>
      <aside className="teacher-side">
        <section><h2>Pratinjau</h2><div className="teacher-preview"><MathText>{form.questionText || "Teks soal akan muncul di sini."}</MathText>{form.questionType === "multiple_choice" && form.options.map((option) => <p key={option.id}><MathText>{option.text || "—"}</MathText></p>)}</div></section>
        <section><h2>Status workflow</h2>{run ? <><p><strong>{run.status}</strong> · {run.stage}</p>{run.error && <p className="teacher-warning">{run.error.code}: {run.error.message}</p>}</> : <p>Belum ada workflow aktif pada tampilan ini.</p>}
          {question?.workflowSummary && <p>Keputusan: {question.workflowSummary.decisionType}{question.workflowSummary.taxonomy && ` · ${question.workflowSummary.taxonomy.bloom} / ${question.workflowSummary.taxonomy.knowledgeDimension} / ${question.workflowSummary.taxonomy.intendedDifficulty}`}</p>}
        </section>
        <section><h2>Draft tersimpan</h2>{questions.length === 0 ? <p>Belum ada soal.</p> : <ul>{questions.map((item) => <li key={item.questionId}><button type="button" onClick={() => selectQuestion(item.questionId)}><strong>{item.authoringContent.topic || item.questionId}</strong><span>{item.questionId} · v{item.contentVersion} · {item.status}</span></button></li>)}</ul>}</section>
      </aside>
    </div>
  </main>;
}
