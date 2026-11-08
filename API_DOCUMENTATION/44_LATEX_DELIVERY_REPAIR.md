# Perbaikan tampilan LaTeX pretest dan exercise

Normalisasi ada di `app/presentation/latex.py`. Pemeriksaan nyata memakai KaTeX
lokal 0.19.0 melalui `scripts/latex_render_check.cjs`; tidak menggunakan API.

Audit mencakup master pretest/exercise semua kelas, kandidat bab/subbab, serta
array hasil validasi dan metadata aktif. Formula yang sudah sesuai tetap sama.
Perbaikan terbatas pada transport/pembatas: karakter kontrol akibat escape JSON
yang salah, backslash command ganda, command terpisah spasi, `ight)` yang
terpotong pada pasangan `\left`, dan formula pecahan/akar tanpa delimiter.
Tidak mengubah nilai, operasi, jawaban, label, atau membuat distraktor salah
menjadi benar. Baris matriks `\\` yang sah dipertahankan.

```powershell
# Audit read-only terhadap data soal; laporan ditulis di runs/latex_audit/.
.\.venv\Scripts\python.exe -X utf8 scripts/audit_question_latex.py

# Buat paket tampilan setelah seluruh pemeriksaan render lolos.
.\.venv\Scripts\python.exe -X utf8 scripts/audit_question_latex.py --write-delivery

# Opsional: arsip siap serah-terima dan patch teks berdasarkan ID soal/opsi.
.\.venv\Scripts\python.exe -X utf8 scripts/package_latex_delivery.py
```

File siap impor tersedia di `output/latex_ready/`, dengan struktur kelas dan
nama JSON yang sama dengan ekspor sebelumnya, termasuk
`hasil_validasi/validation_results.json`. Master siap impor mencakup 580 pretest
dan 8.332 exercise berdasarkan inventaris audit. `manifest.json` paket memuat
checksum sumber dan hasil setiap file serta versi kebijakan format.
`repair_patches.json` hanya memuat field teks yang berubah pada master, dengan
`_id`, `option_id`, nilai sebelum dan sesudah; gunakan ini untuk pembaruan sempit
tanpa menimpa status, jawaban, atau label backend. Jika nilai saat ini berbeda
dari `before` maupun `after`, laporkan konflik, jangan overwrite diam-diam.
`runs/latex_audit/changes.json` mencatat path JSON dan teks sebelum/sesudah;
`report.json` berisi cakupan dan error renderer.

Paket ini adalah turunan presentation dari data tervalidasi, bukan checkpoint
validasi AI baru. Master/evidence berbayar asli, sourceHash, responseHash, ID,
kunci, label dan arsip tidak ditulis ulang agar bukti tetap dapat diverifikasi.
Gunakan JSON paket `latex_ready` ketika menyerahkan data untuk import ke aplikasi.
Jangan menyalin manifest delivery sebagai manifest validasi AI.

API assessment lokal memformat teks respons `next_item` untuk pengiriman pertama
maupun retry. Mapping opsi/scoring tetap memakai snapshot asli. Generator dan
ekspor baru juga menerapkan normalisasi supaya kerusakan yang sama tidak berulang.
Backend eksternal di screenshot tidak terdapat dalam repo ini; paket belum
diimpor otomatis ke server tersebut.

## Renderer aplikasi

Jika data JSON sudah dibaca dengan `response.json()`, **jangan decode escape lagi**:
tidak menggunakan `unicode_escape`, `JSON.parse` untuk string yang sudah terurai,
atau `.replace(/\\r/g, '')`. Yang terakhir dapat merusak `\right` menjadi `ight`.
Jangan menghapus backslash global; itu merusak `\frac`, `\times` dan baris matriks.

Perbaikan data saja belum memasang renderer di aplikasi lain. Untuk frontend
vanilla, contoh yang dapat dipakai ada di `API_DOCUMENTATION/interactive/question_math.js`:

```javascript
const question = await response.json();
// Muat KaTeX JS, CSS, serta fonts di frontend.
QuestionMath.render(stemElement, question.soal_text, katex);
for (const option of question.options) {
  QuestionMath.render(optionElements[option.option_id], option.text, katex);
}
```

Terapkan renderer pada stem, stimulus, SEMUA opsi, dan pembahasan. Jangan hanya
pada soal utama. Formula inline memakai `$...$` atau `\(...\)`, display memakai
`$$...$$` atau `\[...\]`. Helper mempertahankan teks biasa sebagai text node dan
memanggil KaTeX dengan `trust:false`; tidak menyisipkan HTML dari soal.

Untuk React/Vue, gunakan komponen yang memisahkan teks dan segmen matematika
dengan aturan delimiter sama, lalu panggil KaTeX pada isi segmen tanpa delimiter.
Jangan mengirim satu paragraf berbahasa Indonesia seluruhnya ke parser matematika.

Preview hasil KaTeX tersedia di `runs/latex_audit/preview.html`. Lulus parse
berarti sintaks ter-render pada versi renderer yang diuji, bukan verifikasi ulang
kebenaran matematika atau bukti frontend eksternal sudah terdeploy.
