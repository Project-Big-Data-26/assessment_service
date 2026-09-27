import { useState } from "react";
import PdfQuestionAnalyzer from "./pages/PdfQuestionAnalyzer";
import TeacherAuthoring from "./pages/TeacherAuthoring";
import "katex/dist/katex.min.css";
import "./App.css";
import "./TeacherAuthoring.css";

export default function App() {
  const [surface, setSurface] = useState("authoring");
  return <>
    <nav className="surface-nav" aria-label="Pilih fitur">
      <strong>Nalar</strong>
      <div>
        <button type="button" className={surface === "authoring" ? "active" : ""} onClick={() => setSurface("authoring")}>Tulis soal</button>
        <button type="button" className={surface === "pdf" ? "active" : ""} onClick={() => setSurface("pdf")}>Analisis PDF</button>
      </div>
    </nav>
    {surface === "authoring" ? <TeacherAuthoring /> : <PdfQuestionAnalyzer />}
  </>;
}
