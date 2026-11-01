# Ringkasan validasi exercise kelas12_tl batch01

Soal: 1060. Metode per soal tercatat di validasi.requested_runs: N=1 satu penilaian; N=3 + adjudikasi AI; IndoBERT sebagai diagnostik dengan scope sesuai manifest artifact. `level_target` dari generator hanya dipakai untuk perbandingan setelah label dikunci; ia tidak dikirim ke penilai.

## level_target (generator) vs cognitive_level (validasi AI)

| Target | easy | medium | hard | undecided | Sesuai |
|---|---:|---:|---:|---:|---:|
| easy | 323 | 1 | 0 | 36 | 323/360 |
| medium | 289 | 26 | 0 | 40 | 26/355 |
| hard | 93 | 212 | 2 | 38 | 2/345 |

Status: {'active': 936, 'inactive': 124}. Routing: {'silver_ready': 936, 'needs_ai_review': 121, 'revision_required': 3}.

Keputusan lengkap: 946/1060. Soal yang belum lengkap tetap inactive dengan label/score null dan confidence 0; 0 menyatakan belum ada dukungan untuk label final, bukan probabilitas IndoBERT. Confidence N=1 memakai round(100 * min(probabilitas IndoBERT untuk label akhir LLM tiap head)); ini dukungan model, bukan konsistensi antar-run atau akurasi terukur. Nilai 0 saat probabilitas tidak tersedia ditandai confidence_available=false; dukungan sangat kecil juga dapat dibulatkan menjadi 0. Hasil N=3 terdahulu dipertahankan.

`level_sesuai_target` false bukan kesalahan: level generator adalah perkiraan awal; label validasi memakai rubrik relatif kelas. Hanya `status == active` boleh dipakai delivery.

Provider aktif: gemini. 74 keputusan provider sebelumnya dipertahankan tanpa panggilan ulang; provider/model per soal ada pada metadata dan audit.
