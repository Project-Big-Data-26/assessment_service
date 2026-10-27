# Ringkasan validasi exercise kelas7 batch01

Soal: 842. Metode per soal tercatat di validasi.requested_runs: N=1 satu penilaian; N=3 + adjudikasi AI; IndoBERT sebagai diagnostik dengan scope sesuai manifest artifact. `level_target` dari generator hanya dipakai untuk perbandingan setelah label dikunci; ia tidak dikirim ke penilai.

## level_target (generator) vs cognitive_level (validasi AI)

| Target | easy | medium | hard | undecided | Sesuai |
|---|---:|---:|---:|---:|---:|
| easy | 274 | 18 | 0 | 0 | 274/292 |
| medium | 188 | 102 | 0 | 0 | 102/290 |
| hard | 26 | 224 | 10 | 0 | 10/260 |

Status: {'active': 831, 'inactive': 11}. Routing: {'silver_ready': 831, 'needs_ai_review': 9, 'revision_required': 2}.

Keputusan lengkap: 842/842. Soal yang belum lengkap tetap inactive dengan label/score null dan confidence 0; 0 menyatakan belum ada dukungan untuk label final, bukan probabilitas IndoBERT. Confidence N=1 memakai round(100 * min(probabilitas IndoBERT untuk label akhir Gemini tiap head)); ini dukungan model, bukan konsistensi antar-run atau akurasi terukur. Nilai 0 saat probabilitas tidak tersedia ditandai confidence_available=false; dukungan sangat kecil juga dapat dibulatkan menjadi 0. Hasil N=3 terdahulu dipertahankan.

`level_sesuai_target` false bukan kesalahan: level generator adalah perkiraan awal; label validasi memakai rubrik relatif kelas. Hanya `status == active` boleh dipakai delivery.

<!-- operational-chapter-balance -->

## Distribusi operasional per bab

Array utama memakai sekitar 30% easy, 40% medium, 30% hard per bab, diranking dari profil bukti. Label AI asli tetap ada di `ai_validation_results.json`. Soal inactive tidak masuk kuota. Confidence N=1 memakai dukungan IndoBERT untuk label operasional (0 jika tidak tersedia), bukan konsistensi satu run.

| Bab | Active | Easy | Medium | Hard |
|---|---:|---:|---:|---:|
| SMP7-B1 | 129 | 39 | 51 | 39 |
| SMP7-B2 | 125 | 38 | 50 | 37 |
| SMP7-B3 | 135 | 41 | 54 | 40 |
| SMP7-B4 | 132 | 40 | 53 | 39 |
| SMP7-B5 | 87 | 26 | 35 | 26 |
| SMP7-B6 | 223 | 67 | 89 | 67 |
