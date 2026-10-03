# Hasil validasi kelas 1–12

Gunakan `kelasN/hasil_validasi/` sebagai laporan aktif untuk versi soal saat ini. Label AI tetap silver/advisory dan membutuhkan pemeriksaan ahli.

Pembaruan 3 Oktober 2026: validasi kelas 8–12 dilanjutkan dari checkpoint setelah reset kuota. Run sukses lama dipertahankan; audit dan laporan aktif diperbarui setelah setiap batch.

**Koreksi sumber kelas 1–5:** 102 soal berubah setelah penilaian sebelumnya, termasuk perubahan gambar. Hanya run dengan input, prompt, dan byte gambar yang masih cocok dipertahankan. Soal yang berubah ditandai `undecided` dan masuk checkpoint baru `revalidasi_blind_20261003_v2/`; snapshot penilaian sebelumnya tetap utuh.

| Kelas | Soal | Run sukses / target | Easy | Medium | Hard | Undecided | Soal perlu AI | Status |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| [1](kelas1/hasil_validasi/README.md) | 50 | 72/150 | 22 | 2 | 0 | 26 | 26 | Revalidasi koreksi sumber; menunggu kuota |
| [2](kelas2/hasil_validasi/README.md) | 44 | 57/132 | 15 | 4 | 0 | 25 | 25 | Revalidasi koreksi sumber; menunggu kuota |
| [3](kelas3/hasil_validasi/README.md) | 42 | 93/126 | 22 | 9 | 0 | 11 | 11 | Revalidasi koreksi sumber; menunggu kuota |
| [4](kelas4/hasil_validasi/README.md) | 18 | 36/54 | 9 | 3 | 0 | 6 | 6 | Revalidasi koreksi sumber; menunggu kuota |
| [5](kelas5/hasil_validasi/README.md) | 72 | 114/216 | 23 | 13 | 2 | 34 | 34 | Revalidasi koreksi sumber; menunggu kuota |
| [6](kelas6/hasil_validasi/README.md) | 25 | 75/75 | 16 | 9 | 0 | 0 | 0 | Validasi AI lengkap |
| [7](kelas7/hasil_validasi/README.md) | 49 | 147/147 | 28 | 20 | 1 | 0 | 0 | Validasi AI lengkap |
| [8](kelas8/hasil_validasi/README.md) | 42 | 126/126 | 24 | 17 | 1 | 0 | 0 | Validasi AI lengkap |
| [9](kelas9/hasil_validasi/README.md) | 42 | 126/126 | 28 | 14 | 0 | 0 | 0 | Validasi AI lengkap |
| [10](kelas10/hasil_validasi/README.md) | 46 | 138/138 | 29 | 17 | 0 | 0 | 0 | Validasi AI lengkap |
| [11](kelas11/hasil_validasi/README.md) | 22 | 62/66 | 15 | 4 | 1 | 2 | 2 | Belum lengkap; menunggu kuota |
| [12](kelas12/hasil_validasi/README.md) | 32 | 0/96 | 0 | 0 | 0 | 32 | 32 | Belum lengkap; menunggu kuota |

Sisa: **136 soal**, **406 run awal**, ditambah adjudikasi yang diperlukan. [Daftar tepat per kelas, ID soal, dan run yang belum ada](PENDING_AI_VALIDATION.json). [Ringkasan checkpoint](resume_20261003_v1_execution.json). [Petunjuk resume](RESUME_AI_VALIDATION.md).

Kelas 1–5 menggunakan batch `revalidasi_blind_20261003_v2/`. Kelas 6 mempertahankan bukti di `hasil_validasi/bukti_validasi/`. Kelas 7–12 menggunakan `revalidasi_blind_20261002_v1/`. Semua checkpoint kerja dapat dilanjutkan; snapshot di folder audit dan laporan tidak di-resume.

`undecided` tidak disamakan dengan kegagalan konten. Lihat `finalRouting`: soal yang sudah dinilai AI dapat tetap membutuhkan revisi atau pemeriksaan ahli. Nol Easy/Medium/Hard pada batch belum lengkap bukan distribusi akhir.

Model penilai tetap Gemini yang sama, metode blind N=3, verifikasi kunci/solusi/visual, dan adjudikasi AI bila diperlukan. Sumber soal dan opsi dipertahankan; satu gambar kelas 1 yang hilang dipulihkan dari salinan yang tersedia di proyek, dengan [provenance](kelas1/revalidasi_blind_20261003_v2/asset_recovery.json).

IndoBERT lama hanya mendukung kelas 1–6; seluruh diagnostik kelas 7–12 tetap `out_of_scope`/`abstain`. Kelengkapan validasi AI tidak otomatis meloloskan gate training. Gold ahli tetap null; tidak ada training, publikasi soal, CTT, atau IRT dalam pembaruan ini.
