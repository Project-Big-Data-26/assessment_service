# Ringkasan validasi exercise kelas9 batch01

Soal: 270. Metode: Gemini blind N=3 + adjudikasi AI; IndoBERT sebagai diagnostik dengan scope sesuai manifest artifact. `level_target` dari generator hanya dipakai untuk perbandingan setelah label dikunci; ia tidak dikirim ke penilai.

## level_target (generator) vs cognitive_level (validasi AI)

| Target | easy | medium | hard | undecided | Sesuai |
|---|---:|---:|---:|---:|---:|
| easy | 1 | 0 | 0 | 89 | 1/90 |
| medium | 1 | 0 | 0 | 89 | 0/90 |
| hard | 0 | 1 | 0 | 89 | 0/90 |

Status: {'inactive': 267, 'active': 3}. Routing: {'needs_ai_review': 267, 'silver_ready': 3}.

Keputusan lengkap: 3/270. Soal yang belum lengkap tetap inactive dengan label/score null dan confidence 0; 0 menyatakan belum ada dukungan untuk label final, bukan probabilitas IndoBERT.

`level_sesuai_target` false bukan kesalahan: level generator adalah perkiraan awal; label validasi memakai rubrik relatif kelas. Hanya `status == active` boleh dipakai delivery.
