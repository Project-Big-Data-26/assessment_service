# Ringkasan validasi exercise kelas11_tl batch01

Soal: 1191. Metode per soal tercatat di validasi.requested_runs: N=1 satu penilaian; N=3 + adjudikasi AI; IndoBERT sebagai diagnostik dengan scope sesuai manifest artifact. `level_target` dari generator hanya dipakai untuk perbandingan setelah label dikunci; ia tidak dikirim ke penilai.

## level_target (generator) vs cognitive_level (validasi AI)

| Target | easy | medium | hard | undecided | Sesuai |
|---|---:|---:|---:|---:|---:|
| easy | 434 | 26 | 0 | 0 | 434/460 |
| medium | 300 | 131 | 2 | 0 | 131/433 |
| hard | 70 | 215 | 13 | 0 | 13/298 |

Status: {'active': 1182, 'inactive': 9}. Routing: {'silver_ready': 1182, 'needs_ai_review': 5, 'revision_required': 4}.

Keputusan lengkap: 1191/1191. Soal yang belum lengkap tetap inactive dengan label/score null dan confidence 0; 0 menyatakan belum ada dukungan untuk label final, bukan probabilitas IndoBERT. Confidence N=1 memakai round(100 * min(probabilitas IndoBERT untuk label akhir LLM tiap head)); ini dukungan model, bukan konsistensi antar-run atau akurasi terukur. Nilai 0 saat probabilitas tidak tersedia ditandai confidence_available=false; dukungan sangat kecil juga dapat dibulatkan menjadi 0. Hasil N=3 terdahulu dipertahankan.

`level_sesuai_target` false bukan kesalahan: level generator adalah perkiraan awal; label validasi memakai rubrik relatif kelas. Hanya `status == active` boleh dipakai delivery.

Provider aktif: gemini. 1089 keputusan provider sebelumnya dipertahankan tanpa panggilan ulang; provider/model per soal ada pada metadata dan audit.

<!-- operational-chapter-balance -->

## Distribusi operasional per bab

Array utama memakai sekitar 30% easy, 40% medium, 30% hard per bab, diranking dari profil bukti. Label AI asli tetap ada di `ai_validation_results.json`. Soal inactive tidak masuk kuota. Confidence N=1 memakai dukungan IndoBERT untuk label operasional (0 jika tidak tersedia), bukan konsistensi satu run.

| Bab | Active | Easy | Medium | Hard |
|---|---:|---:|---:|---:|
| SMA11L-B1 | 261 | 78 | 105 | 78 |
| SMA11L-B2 | 255 | 77 | 102 | 76 |
| SMA11L-B3 | 230 | 69 | 92 | 69 |
| SMA11L-B4 | 155 | 47 | 62 | 46 |
| SMA11L-B5 | 165 | 50 | 66 | 49 |
| SMA11L-B6 | 116 | 35 | 46 | 35 |
