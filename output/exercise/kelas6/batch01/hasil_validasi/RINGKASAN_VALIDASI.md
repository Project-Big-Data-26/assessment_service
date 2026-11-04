# Ringkasan validasi exercise kelas6 batch01

Soal: 382. Metode per soal tercatat di validasi.requested_runs: N=1 satu penilaian; N=3 + adjudikasi AI; IndoBERT sebagai diagnostik dengan scope sesuai manifest artifact. `level_target` dari generator hanya dipakai untuk perbandingan setelah label dikunci; ia tidak dikirim ke penilai.

## level_target (generator) vs cognitive_level (validasi AI)

| Target | easy | medium | hard | undecided | Sesuai |
|---|---:|---:|---:|---:|---:|
| easy | 101 | 16 | 1 | 17 | 101/135 |
| medium | 79 | 29 | 2 | 6 | 29/116 |
| hard | 54 | 59 | 3 | 15 | 3/131 |

Status: {'active': 341, 'inactive': 41}. Routing: {'silver_ready': 341, 'revision_required': 2, 'needs_ai_review': 39}.

Keputusan lengkap: 344/382. Soal yang belum lengkap tetap inactive dengan label/score null dan confidence 0; 0 menyatakan belum ada dukungan untuk label final, bukan probabilitas IndoBERT. Confidence N=1 memakai round(100 * min(probabilitas IndoBERT untuk label akhir LLM tiap head)); ini dukungan model, bukan konsistensi antar-run atau akurasi terukur. Nilai 0 saat probabilitas tidak tersedia ditandai confidence_available=false; dukungan sangat kecil juga dapat dibulatkan menjadi 0. Hasil N=3 terdahulu dipertahankan.

`level_sesuai_target` false bukan kesalahan: level generator adalah perkiraan awal; label validasi memakai rubrik relatif kelas. Hanya `status == active` boleh dipakai delivery.

Provider aktif: groq. 343 keputusan provider sebelumnya dipertahankan tanpa panggilan ulang; provider/model per soal ada pada metadata dan audit.
