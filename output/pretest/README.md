# Hasil validasi kelas 1–12

Gunakan `kelasN/hasil_validasi/` sebagai laporan aktif untuk versi soal saat ini. Label AI tetap silver/advisory dan membutuhkan pemeriksaan ahli.

Pembaruan 3 Oktober 2026: backlog kuota untuk kelas 1?5, 11, dan 12 selesai. Seluruh **484 soal kelas reguler 1?12** telah memperoleh penilaian blind N=3 (**1452/1452 run awal sukses**), dan seluruh adjudikasi yang diperlukan selesai. Hasil sukses lama dipertahankan; audit, kelompok difficulty, dan laporan aktif diperbarui.

**Koreksi sumber kelas 1?5:** 102 soal berubah setelah penilaian sebelumnya, termasuk perubahan gambar. Hanya run dengan input, prompt, dan byte gambar yang masih cocok dipertahankan. Seluruh soal yang berubah telah dinilai ulang melalui checkpoint `revalidasi_blind_20261003_v2/`; snapshot penilaian sebelumnya tetap utuh.

| Kelas | Soal | Run sukses / target | Easy | Medium | Hard | Undecided | Soal perlu AI | Status |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| [1](kelas1/hasil_validasi/README.md) | 50 | 150/150 | 48 | 2 | 0 | 0 | 0 | Validasi AI lengkap |
| [2](kelas2/hasil_validasi/README.md) | 44 | 132/132 | 38 | 6 | 0 | 0 | 0 | Validasi AI lengkap |
| [3](kelas3/hasil_validasi/README.md) | 42 | 126/126 | 33 | 9 | 0 | 0 | 0 | Validasi AI lengkap |
| [4](kelas4/hasil_validasi/README.md) | 18 | 54/54 | 14 | 4 | 0 | 0 | 0 | Validasi AI lengkap |
| [5](kelas5/hasil_validasi/README.md) | 72 | 216/216 | 48 | 22 | 2 | 0 | 0 | Validasi AI lengkap |
| [6](kelas6/hasil_validasi/README.md) | 25 | 75/75 | 16 | 9 | 0 | 0 | 0 | Validasi AI lengkap |
| [7](kelas7/hasil_validasi/README.md) | 49 | 147/147 | 28 | 20 | 1 | 0 | 0 | Validasi AI lengkap |
| [8](kelas8/hasil_validasi/README.md) | 42 | 126/126 | 24 | 17 | 1 | 0 | 0 | Validasi AI lengkap |
| [9](kelas9/hasil_validasi/README.md) | 42 | 126/126 | 28 | 14 | 0 | 0 | 0 | Validasi AI lengkap |
| [10](kelas10/hasil_validasi/README.md) | 46 | 138/138 | 29 | 17 | 0 | 0 | 0 | Validasi AI lengkap |
| [11](kelas11/hasil_validasi/README.md) | 22 | 66/66 | 15 | 6 | 1 | 0 | 0 | Validasi AI lengkap |
| [12](kelas12/hasil_validasi/README.md) | 32 | 96/96 | 19 | 13 | 0 | 0 | 0 | Validasi AI lengkap |

Sisa backlog kuota: **0 soal**, **0 run awal**, **0 adjudikasi**. [Bukti verifikasi akhir](resume_20261003_final_execution.json). [Daftar tepat per kelas, ID soal, dan run yang belum ada](PENDING_AI_VALIDATION.json). [Petunjuk resume](RESUME_AI_VALIDATION.md).

Kelas 1–5 menggunakan batch `revalidasi_blind_20261003_v2/`. Kelas 6 mempertahankan bukti di `hasil_validasi/bukti_validasi/`. Kelas 7–12 menggunakan `revalidasi_blind_20261002_v1/`. Semua checkpoint kerja dapat dilanjutkan; snapshot di folder audit dan laporan tidak di-resume.

`undecided` tidak disamakan dengan kegagalan konten. Lihat `finalRouting`: soal yang sudah dinilai AI dapat tetap membutuhkan revisi atau pemeriksaan ahli. Nol Easy/Medium/Hard pada batch belum lengkap bukan distribusi akhir.

Model penilai tetap Gemini yang sama, metode blind N=3, verifikasi kunci/solusi/visual, dan adjudikasi AI bila diperlukan. Sumber soal dan opsi dipertahankan; satu gambar kelas 1 yang hilang dipulihkan dari salinan yang tersedia di proyek, dengan [provenance](kelas1/revalidasi_blind_20261003_v2/asset_recovery.json).

IndoBERT lama hanya mendukung kelas 1–6; seluruh diagnostik kelas 7–12 tetap `out_of_scope`/`abstain`. Kelengkapan validasi AI tidak otomatis meloloskan gate training. Gold ahli tetap null; tidak ada training, publikasi soal, CTT, atau IRT dalam pembaruan ini.

Dua adjudikasi sempat gagal karena respons klasifikasi tidak memuat bukti. Schema yang dikirim ke provider kini mewajibkan bukti untuk `classify`, sambil tetap mengizinkan `abstain` tanpa bukti. Validator lokal, model, rubrik, dan hash prompt tetap sama. Kedua adjudikasi telah diulang dengan hasil valid; 63 tes terkait lulus.

**Di luar backlog kuota ini:** `kelas11_tl` (55 soal) dan `kelas12_tl` (41 soal) belum pernah mendapat validasi AI. Keduanya belum dimasukkan ke batch kelas reguler ini.
