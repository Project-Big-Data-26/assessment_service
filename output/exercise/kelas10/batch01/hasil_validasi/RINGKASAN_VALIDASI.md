# Ringkasan validasi exercise kelas10 batch01

Soal: 1037. Metode per soal tercatat di validasi.requested_runs: N=1 satu penilaian; N=3 + adjudikasi AI; IndoBERT sebagai diagnostik dengan scope sesuai manifest artifact. `level_target` dari generator hanya dipakai untuk perbandingan setelah label dikunci; ia tidak dikirim ke penilai.

## level_target (generator) vs cognitive_level (validasi AI)

| Target | easy | medium | hard | undecided | Sesuai |
|---|---:|---:|---:|---:|---:|
| easy | 351 | 19 | 0 | 0 | 351/370 |
| medium | 214 | 149 | 0 | 0 | 149/363 |
| hard | 59 | 240 | 5 | 0 | 5/304 |

Status: {'active': 1012, 'inactive': 25}. Routing: {'silver_ready': 1012, 'needs_ai_review': 22, 'revision_required': 3}.

Keputusan lengkap: 1037/1037. Soal yang belum lengkap tetap inactive dengan label/score null dan confidence 0; 0 menyatakan belum ada dukungan untuk label final, bukan probabilitas IndoBERT. Confidence N=1 memakai round(100 * min(probabilitas IndoBERT untuk label akhir LLM tiap head)); ini dukungan model, bukan konsistensi antar-run atau akurasi terukur. Nilai 0 saat probabilitas tidak tersedia ditandai confidence_available=false; dukungan sangat kecil juga dapat dibulatkan menjadi 0. Hasil N=3 terdahulu dipertahankan.

`level_sesuai_target` false bukan kesalahan: level generator adalah perkiraan awal; label validasi memakai rubrik relatif kelas. Hanya `status == active` boleh dipakai delivery.

Provider aktif: gemini. 927 keputusan provider sebelumnya dipertahankan tanpa panggilan ulang; provider/model per soal ada pada metadata dan audit.

<!-- operational-chapter-balance -->

## Distribusi operasional per bab

Array utama memakai sekitar 30% easy, 40% medium, 30% hard per bab, diranking dari profil bukti. Label AI asli tetap ada di `ai_validation_results.json`. Soal inactive tidak masuk kuota. Confidence N=1 memakai dukungan IndoBERT untuk label operasional (0 jika tidak tersedia), bukan konsistensi satu run.

| Bab | Active | Easy | Medium | Hard |
|---|---:|---:|---:|---:|
| SMA10-B1 | 211 | 63 | 85 | 63 |
| SMA10-B2 | 147 | 44 | 59 | 44 |
| SMA10-B3 | 119 | 36 | 47 | 36 |
| SMA10-B4 | 99 | 30 | 39 | 30 |
| SMA10-B5 | 120 | 36 | 48 | 36 |
| SMA10-B6 | 142 | 43 | 57 | 42 |
| SMA10-B7 | 174 | 52 | 70 | 52 |
