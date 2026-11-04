# Ringkasan validasi exercise kelas9 batch01

Soal: 860. Metode per soal tercatat di validasi.requested_runs: N=1 satu penilaian; N=3 + adjudikasi AI; IndoBERT sebagai diagnostik dengan scope sesuai manifest artifact. `level_target` dari generator hanya dipakai untuk perbandingan setelah label dikunci; ia tidak dikirim ke penilai.

## level_target (generator) vs cognitive_level (validasi AI)

| Target | easy | medium | hard | undecided | Sesuai |
|---|---:|---:|---:|---:|---:|
| easy | 253 | 5 | 0 | 42 | 253/300 |
| medium | 176 | 83 | 0 | 5 | 83/264 |
| hard | 38 | 207 | 9 | 42 | 9/296 |

Status: {'active': 767, 'inactive': 93}. Routing: {'silver_ready': 767, 'revision_required': 1, 'needs_ai_review': 92}.

Keputusan lengkap: 771/860. Soal yang belum lengkap tetap inactive dengan label/score null dan confidence 0; 0 menyatakan belum ada dukungan untuk label final, bukan probabilitas IndoBERT. Confidence N=1 memakai round(100 * min(probabilitas IndoBERT untuk label akhir LLM tiap head)); ini dukungan model, bukan konsistensi antar-run atau akurasi terukur. Nilai 0 saat probabilitas tidak tersedia ditandai confidence_available=false; dukungan sangat kecil juga dapat dibulatkan menjadi 0. Hasil N=3 terdahulu dipertahankan.

`level_sesuai_target` false bukan kesalahan: level generator adalah perkiraan awal; label validasi memakai rubrik relatif kelas. Hanya `status == active` boleh dipakai delivery.

Provider aktif: gemini. 422 keputusan provider sebelumnya dipertahankan tanpa panggilan ulang; provider/model per soal ada pada metadata dan audit.
