# Ringkasan validasi exercise kelas12 batch01

Soal: 836. Metode per soal tercatat di validasi.requested_runs: N=1 satu penilaian; N=3 + adjudikasi AI; IndoBERT sebagai diagnostik dengan scope sesuai manifest artifact. `level_target` dari generator hanya dipakai untuk perbandingan setelah label dikunci; ia tidak dikirim ke penilai.

## level_target (generator) vs cognitive_level (validasi AI)

| Target | easy | medium | hard | undecided | Sesuai |
|---|---:|---:|---:|---:|---:|
| easy | 258 | 29 | 0 | 0 | 258/287 |
| medium | 149 | 138 | 1 | 0 | 138/288 |
| hard | 76 | 180 | 5 | 0 | 5/261 |

Status: {'active': 809, 'inactive': 27}. Routing: {'silver_ready': 809, 'needs_ai_review': 23, 'revision_required': 4}.

Keputusan lengkap: 836/836. Soal yang belum lengkap tetap inactive dengan label/score null dan confidence 0; 0 menyatakan belum ada dukungan untuk label final, bukan probabilitas IndoBERT. Confidence N=1 memakai round(100 * min(probabilitas IndoBERT untuk label akhir LLM tiap head)); ini dukungan model, bukan konsistensi antar-run atau akurasi terukur. Nilai 0 saat probabilitas tidak tersedia ditandai confidence_available=false; dukungan sangat kecil juga dapat dibulatkan menjadi 0. Hasil N=3 terdahulu dipertahankan.

`level_sesuai_target` false bukan kesalahan: level generator adalah perkiraan awal; label validasi memakai rubrik relatif kelas. Hanya `status == active` boleh dipakai delivery.

Provider aktif: gemini. 337 keputusan provider sebelumnya dipertahankan tanpa panggilan ulang; provider/model per soal ada pada metadata dan audit.

<!-- operational-chapter-balance -->

## Distribusi operasional per bab

Array utama memakai sekitar 30% easy, 40% medium, 30% hard per bab, diranking dari profil bukti. Label AI asli tetap ada di `ai_validation_results.json`. Soal inactive tidak masuk kuota. Confidence N=1 memakai dukungan IndoBERT untuk label operasional (0 jika tidak tersedia), bukan konsistensi satu run.

| Bab | Active | Easy | Medium | Hard |
|---|---:|---:|---:|---:|
| SMA12U-B1 | 156 | 47 | 62 | 47 |
| SMA12U-B2 | 319 | 96 | 127 | 96 |
| SMA12U-B3 | 216 | 65 | 86 | 65 |
| SMA12U-B4 | 118 | 36 | 47 | 35 |
