# Ringkasan validasi exercise kelas11_tl batch01

Soal: 264. Metode: Gemini blind N=3 + adjudikasi AI; IndoBERT sebagai diagnostik dengan scope sesuai manifest artifact. `level_target` dari generator hanya dipakai untuk perbandingan setelah label dikunci; ia tidak dikirim ke penilai.

## level_target (generator) vs cognitive_level (validasi AI)

| Target | easy | medium | hard | undecided | Sesuai |
|---|---:|---:|---:|---:|---:|
| easy | 1 | 0 | 0 | 99 | 1/100 |
| medium | 1 | 0 | 0 | 99 | 0/100 |
| hard | 0 | 1 | 0 | 63 | 0/64 |

Status: {'inactive': 261, 'active': 3}. Routing: {'needs_ai_review': 261, 'silver_ready': 3}.

Keputusan lengkap: 3/264. Soal yang belum lengkap tetap inactive dengan label/score null dan confidence 0; 0 menyatakan belum ada dukungan untuk label final, bukan probabilitas IndoBERT.

`level_sesuai_target` false bukan kesalahan: level generator adalah perkiraan awal; label validasi memakai rubrik relatif kelas. Hanya `status == active` boleh dipakai delivery.
