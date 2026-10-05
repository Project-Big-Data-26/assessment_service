# Ringkasan validasi exercise kelas7 batch01

Soal: 617. Metode: Gemini blind N=3 + adjudikasi AI; IndoBERT sebagai diagnostik dengan scope sesuai manifest artifact. `level_target` dari generator hanya dipakai untuk perbandingan setelah label dikunci; ia tidak dikirim ke penilai.

## level_target (generator) vs cognitive_level (validasi AI)

| Target | easy | medium | hard | undecided | Sesuai |
|---|---:|---:|---:|---:|---:|
| easy | 1 | 0 | 0 | 216 | 1/217 |
| medium | 0 | 1 | 0 | 214 | 1/215 |
| hard | 0 | 1 | 0 | 184 | 0/185 |

Status: {'inactive': 614, 'active': 3}. Routing: {'needs_ai_review': 614, 'silver_ready': 3}.

Keputusan lengkap: 3/617. Soal yang belum lengkap tetap inactive dengan label/score null dan confidence 0; 0 menyatakan belum ada dukungan untuk label final, bukan probabilitas IndoBERT.

`level_sesuai_target` false bukan kesalahan: level generator adalah perkiraan awal; label validasi memakai rubrik relatif kelas. Hanya `status == active` boleh dipakai delivery.
