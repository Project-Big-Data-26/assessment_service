# Ringkasan validasi exercise kelas8 batch01

Soal: 853. Metode per soal tercatat di validasi.requested_runs: N=1 satu penilaian; N=3 + adjudikasi AI; IndoBERT sebagai diagnostik dengan scope sesuai manifest artifact. `level_target` dari generator hanya dipakai untuk perbandingan setelah label dikunci; ia tidak dikirim ke penilai.

## level_target (generator) vs cognitive_level (validasi AI)

| Target | easy | medium | hard | undecided | Sesuai |
|---|---:|---:|---:|---:|---:|
| easy | 275 | 10 | 0 | 0 | 275/285 |
| medium | 166 | 119 | 0 | 0 | 119/285 |
| hard | 101 | 169 | 13 | 0 | 13/283 |

Status: {'active': 852, 'inactive': 1}. Routing: {'silver_ready': 852, 'needs_ai_review': 1}.

Keputusan lengkap: 853/853. Soal yang belum lengkap tetap inactive dengan label/score null dan confidence 0; 0 menyatakan belum ada dukungan untuk label final, bukan probabilitas IndoBERT. Confidence N=1 memakai round(100 * min(probabilitas IndoBERT untuk label akhir LLM tiap head)); ini dukungan model, bukan konsistensi antar-run atau akurasi terukur. Nilai 0 saat probabilitas tidak tersedia ditandai confidence_available=false; dukungan sangat kecil juga dapat dibulatkan menjadi 0. Hasil N=3 terdahulu dipertahankan.

`level_sesuai_target` false bukan kesalahan: level generator adalah perkiraan awal; label validasi memakai rubrik relatif kelas. Hanya `status == active` boleh dipakai delivery.

Provider aktif: gemini. 832 keputusan provider sebelumnya dipertahankan tanpa panggilan ulang; provider/model per soal ada pada metadata dan audit.

<!-- operational-chapter-balance -->

## Distribusi operasional per bab

Array utama memakai sekitar 30% easy, 40% medium, 30% hard per bab, diranking dari profil bukti. Label AI asli tetap ada di `ai_validation_results.json`. Soal inactive tidak masuk kuota. Confidence N=1 memakai dukungan IndoBERT untuk label operasional (0 jika tidak tersedia), bukan konsistensi satu run.

| Bab | Active | Easy | Medium | Hard |
|---|---:|---:|---:|---:|
| SMP8-B1 | 134 | 40 | 54 | 40 |
| SMP8-B2 | 224 | 67 | 90 | 67 |
| SMP8-B3 | 180 | 54 | 72 | 54 |
| SMP8-B4 | 134 | 40 | 54 | 40 |
| SMP8-B5 | 90 | 27 | 36 | 27 |
| SMP8-B6 | 90 | 27 | 36 | 27 |
