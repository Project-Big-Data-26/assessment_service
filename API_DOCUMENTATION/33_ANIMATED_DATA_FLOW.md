# Animasi aliran data silver

[Buka animasi interaktif](33_ANIMATED_DATA_FLOW.html). Alur dimulai dari JSON ekstraksi, validasi blind AI N=3, qualification silver, snapshot, model, delivery siswa, scoring, CTT/IRT dan feedback otomatis.

Sistem memakai label silver AI tanpa persetujuan pelabel manusia. Operator mengelola data dan pekerjaan sistem; tidak menentukan label pedagogis. Hanya `silver_ready` masuk snapshot delivery. Soal dengan blocker ditahan untuk revisi dan revalidation AI.

Halaman menampilkan peta bercabang dengan kartu input/output, kondisi, sumber kode dan rumus. Tiga run Gemini dan tiga head IndoBERT memiliki kartu terpisah. Kalkulator softmax/confidence/entropy, Wilson CI, ordinal difficulty, probabilitas IRT, informasi tes dan EAP tetap berupa contoh pembelajaran. Halaman tidak memanggil LLM atau memuat respons siswa nyata.

Peta memakai lebar halaman dengan kartu berukuran besar; detail tahap berada di bawah peta. Tampilan awal langsung memperlihatkan **N=3**, tiga kartu penilaian dan garis bergabung, kemudian cabang konsensus/adjudikasi/checkpoint. Tombol **Lihat percabangan** juga membuka keputusan validasi, tiga head IndoBERT, serta CTT/syarat IRT. Pilih **Alur lengkap dari awal** atau **Ulang** untuk kembali ke awal perjalanan. Di layar kecil, geser peta ke samping; ukuran teks dan kartu dipertahankan agar terbaca.

Pilih **Contoh jalur** untuk mengikuti alur bank operasional, adjudikasi, checkpoint, revisi konten, training, training tertunda, IRT siap, atau IRT belum cukup. Filter bagian menyederhanakan peta; klik tujuan di panel kondisi untuk masuk ke cabang yang sesuai. Garis hijau menandai kelanjutan yang lolos, kuning review/tunggu, merah penahanan, dan garis putus-putus job eksplisit atau jalur opsional. Panah serta label kondisi tetap terlihat tanpa memilih kartu. Animasi membaca kartu dalam contoh jalur, bukan menjalankan pekerjaan backend.

N=3 berarti tiga penilaian independen dari model Gemini yang sama. Runner saat ini memakai satu worker, sehingga fork kartu tidak menyatakan tiga request paralel. Run belum lengkap menuju checkpoint; 429 pertama menghentikan seluruh panggilan API. Tiga run sukses dengan 3–0 pada setiap head dan konten/kunci yang sesuai menuju qualification; ketidaksepakatan/abstain/masalah konten menuju adjudikasi. Adjudikasi bukan suara keempat.

Buka HTML langsung atau jalankan:

```powershell
.\.venv\Scripts\python.exe -m http.server 8765 --bind 127.0.0.1
```

Lalu buka `http://127.0.0.1:8765/API_DOCUMENTATION/33_ANIMATED_DATA_FLOW.html`. Folder `interactive/` dan KaTeX lokal harus berdampingan dengan HTML. Tombol putar, jeda, langkah, penjelasan, salin JSON/rumus dan ringkasan PPT tersedia.

Tombol **Lihat percabangan** memilih peta teknis dan membuka input, proses, output, serta aturan implementasi tahap terpilih. **Buka detail teknis tahap ↓** membawa pembaca langsung ke panel tersebut. Checklist dapat menutup detail teknis untuk membaca penjelasan ringkas. Aset aplikasi memakai parameter versi yang sama agar HTML baru tidak memakai script alur lama dari cache; naikkan versi pada seluruh referensi aset aplikasi saat perilaku UI diperbarui.

| Tahap | Arti |
|---|---|
| Validasi AI | N=3 dan adjudikasi menghasilkan label silver |
| Qualification | Kunci/solusi/visual, coverage dan hash tetap diperiksa |
| Snapshot | Versi immutable dengan provenance `ai_silver` |
| Delivery | Snapshot silver qualified, grade/track tepat, opsi opaque |
| CTT/IRT | Bukti empiris terpisah dari label awal |
| Feedback | Sistem mempertahankan, mengumpulkan data, atau menahan versi untuk AI review |
| Training berikutnya | Snapshot baru dan gate teknis; tidak auto-retrain |

`implemented` berarti fungsi kode tersedia, `conditional` memerlukan data/artifact/kredensial yang sesuai, dan `planned` belum menjadi fitur runtime. Rubrik **v8** dan prompt **v10** mencakup kelas 1–12 reguler dan TL 11–12 melalui sembilan YAML. Hard menilai tuntutan perencanaan/integrasi dan sedikitnya bantuan; prosedur familiar dapat Hard. Panjang soal, jumlah operasi, angka besar atau topik lanjut saja tidak menetapkan Hard.

Config IndoBERT baru memakai `grade-aware-ordinal-v2`, embedding 12 kelas, penanda teks TL, dan representation `solution`. Runtime mengikuti scope/representation manifest; artifact SD lama tetap memakai scope aslinya. KKO adalah ablation, confidence/entropy merupakan keluaran, profil difficulty merupakan evidence Gemini, dan parameter IRT bukan fitur input classifier saat ini. Tabel fitur tersedia pada tab detail teknis.

Arsip **ai_validation_results.json** dan keputusan AI asli menjadi sumber training serta persiapan IRT. **validation_results.json** yang dipublikasikan menyimpan kategori bank relatif `relative_bank_quota`, mengikuti schema `soal_pretest_db.json`. Pembagian mendekati ⅓ adalah distribusi seragam, bukan normal statistik. Confidence dukungan AI terhadap label operasional dapat 0; ini berbeda dari probabilitas IndoBERT. Soal inactive tidak diaktifkan untuk memenuhi kuota.

Kelas belum lengkap tetap memakai bundle aktif sebelumnya; manifest mencatat `newRubricValidationComplete`. Training ditunda ketika seluruh 14 bundle atau gate label/split belum memenuhi syarat. Artifact tidak servable menghasilkan HTTP 503; input di luar scope/provenance menghasilkan abstain. IRT menunggu respons nyata dan bukti asumsi; gate gagal menyimpan alasan dan CTT yang tersedia, bukan parameter atau theta buatan.

Lihat [34 ringkasan PPT](34_PPT_SUMMARY.md), [36 integrasi](36_SILVER_OPERATIONAL_INTEGRATION.md), dan [37 rubrik v8](37_RUBRIC_V8_REVALIDATION.md). Prompt/rubrik dan checkpoint lama tetap immutable sebagai bukti penilaian; policy operasional berada di luar teks prompt historis.
