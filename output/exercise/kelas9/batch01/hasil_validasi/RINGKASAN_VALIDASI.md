# Ringkasan validasi exercise kelas9 batch01

Soal: 764. Metode per soal tercatat di validasi.requested_runs: N=1 satu penilaian; N=3 + adjudikasi AI; IndoBERT sebagai diagnostik dengan scope sesuai manifest artifact. `level_target` dari generator hanya dipakai untuk perbandingan setelah label dikunci; ia tidak dikirim ke penilai.

## level_target (generator) vs cognitive_level (validasi AI)

| Target | easy | medium | hard | undecided | Sesuai |
|---|---:|---:|---:|---:|---:|
| easy | 250 | 5 | 0 | 0 | 250/255 |
| medium | 172 | 83 | 0 | 0 | 83/255 |
| hard | 38 | 207 | 9 | 0 | 9/254 |

Status: {'active': 760, 'inactive': 4}. Routing: {'silver_ready': 760, 'revision_required': 1, 'needs_ai_review': 3}.

Keputusan lengkap: 764/764. Soal yang belum lengkap tetap inactive dengan label/score null dan confidence 0; 0 menyatakan belum ada dukungan untuk label final, bukan probabilitas IndoBERT. Confidence N=1 memakai round(100 * min(probabilitas IndoBERT untuk label akhir LLM tiap head)); ini dukungan model, bukan konsistensi antar-run atau akurasi terukur. Nilai 0 saat probabilitas tidak tersedia ditandai confidence_available=false; dukungan sangat kecil juga dapat dibulatkan menjadi 0. Hasil N=3 terdahulu dipertahankan.

`level_sesuai_target` false bukan kesalahan: level generator adalah perkiraan awal; label validasi memakai rubrik relatif kelas. Hanya `status == active` boleh dipakai delivery.

Provider aktif: gemini. 422 keputusan provider sebelumnya dipertahankan tanpa panggilan ulang; provider/model per soal ada pada metadata dan audit.

<!-- operational-chapter-balance -->

## Distribusi operasional per bab

Array utama memakai sekitar 30% easy, 40% medium, 30% hard per bab, diranking dari profil bukti. Label AI asli tetap ada di `ai_validation_results.json`. Soal inactive tidak masuk kuota. Confidence N=1 memakai dukungan IndoBERT untuk label operasional (0 jika tidak tersedia), bukan konsistensi satu run.

| Bab | Active | Easy | Medium | Hard |
|---|---:|---:|---:|---:|
| SMP9-B1 | 90 | 27 | 36 | 27 |
| SMP9-B2 | 270 | 81 | 108 | 81 |
| SMP9-B3 | 222 | 67 | 89 | 66 |
| SMP9-B4 | 178 | 54 | 71 | 53 |
