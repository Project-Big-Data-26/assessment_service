# Validasi blind silver -> kelas11_tl, kelas12_tl

Status aktif 3 Oktober 2026. Seluruh soal dinilai tiga kali melalui Gemini blind dan adjudikasi AI bila diperlukan. Label, prompt, rubrik dan respons terkunci; label operasional tetap ai_silver tanpa persetujuan pelabel manusia.

| Kelas | Soal | Run sukses | Easy | Medium | Hard | Routing |
|---|---:|---:|---:|---:|---:|---|
| [kelas11_tl](../output/pretest/kelas11_tl/hasil_validasi/README.md) | 55 | 165 | 44 | 11 | 0 | {'silver_ready': 54, 'revision_required': 1} |
| [kelas12_tl](../output/pretest/kelas12_tl/hasil_validasi/README.md) | 41 | 123 | 30 | 11 | 0 | {'revision_required': 1, 'silver_ready': 40} |

Hanya silver_ready masuk snapshot operasional. Revision_required dan needs_ai_review tetap ditahan. Difficulty yang tidak terisi tidak dipaksakan untuk memenuhi kuota. Kelas 7-12/TL tetap di luar scope IndoBERT SD dan diagnostiknya abstain; label mengikuti penilaian AI.

Gunakan laporan aktif untuk data sekarang; snapshot parsial dan laporan terdahulu adalah histori. Label silver dan bukti siswa/CTT/IRT berbeda. Audit training yang belum lolos tidak dianggap selesai hanya karena semua run AI sukses. [Integrasi silver](36_SILVER_OPERATIONAL_INTEGRATION.md).
