# Validasi blind silver -> kelas10, kelas11, kelas12

Status aktif 3 Oktober 2026. Seluruh soal dinilai tiga kali melalui Gemini blind dan adjudikasi AI bila diperlukan. Label, prompt, rubrik dan respons terkunci; label operasional tetap ai_silver tanpa persetujuan pelabel manusia.

| Kelas | Soal | Run sukses | Easy | Medium | Hard | Routing |
|---|---:|---:|---:|---:|---:|---|
| [kelas10](../output/pretest/kelas10/hasil_validasi/README.md) | 46 | 138 | 29 | 17 | 0 | {'silver_ready': 46} |
| [kelas11](../output/pretest/kelas11/hasil_validasi/README.md) | 22 | 66 | 15 | 6 | 1 | {'silver_ready': 21, 'revision_required': 1} |
| [kelas12](../output/pretest/kelas12/hasil_validasi/README.md) | 32 | 96 | 19 | 13 | 0 | {'silver_ready': 31, 'revision_required': 1} |

Hanya silver_ready masuk snapshot operasional. Revision_required dan needs_ai_review tetap ditahan. Difficulty yang tidak terisi tidak dipaksakan untuk memenuhi kuota. Kelas 7-12/TL tetap di luar scope IndoBERT SD dan diagnostiknya abstain; label mengikuti penilaian AI.

Gunakan laporan aktif untuk data sekarang; snapshot parsial dan laporan terdahulu adalah histori. Label silver dan bukti siswa/CTT/IRT berbeda. Audit training yang belum lolos tidak dianggap selesai hanya karena semua run AI sukses. [Integrasi silver](36_SILVER_OPERATIONAL_INTEGRATION.md).
