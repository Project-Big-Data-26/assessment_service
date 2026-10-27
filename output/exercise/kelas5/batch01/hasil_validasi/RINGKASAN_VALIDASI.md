# Ringkasan validasi exercise kelas5 batch01

Soal: 916. Metode per soal tercatat di validasi.requested_runs: N=1 satu penilaian; N=3 + adjudikasi AI; IndoBERT sebagai diagnostik dengan scope sesuai manifest artifact. `level_target` dari generator hanya dipakai untuk perbandingan setelah label dikunci; ia tidak dikirim ke penilai.

## level_target (generator) vs cognitive_level (validasi AI)

| Target | easy | medium | hard | undecided | Sesuai |
|---|---:|---:|---:|---:|---:|
| easy | 288 | 30 | 0 | 0 | 288/318 |
| medium | 173 | 140 | 1 | 0 | 140/314 |
| hard | 71 | 191 | 22 | 0 | 22/284 |

Status: {'active': 912, 'inactive': 4}. Routing: {'silver_ready': 912, 'needs_ai_review': 1, 'revision_required': 3}.

Keputusan lengkap: 916/916. Soal yang belum lengkap tetap inactive dengan label/score null dan confidence 0; 0 menyatakan belum ada dukungan untuk label final, bukan probabilitas IndoBERT. Confidence N=1 memakai round(100 * min(probabilitas IndoBERT untuk label akhir Gemini tiap head)); ini dukungan model, bukan konsistensi antar-run atau akurasi terukur. Nilai 0 saat probabilitas tidak tersedia ditandai confidence_available=false; dukungan sangat kecil juga dapat dibulatkan menjadi 0. Hasil N=3 terdahulu dipertahankan.

`level_sesuai_target` false bukan kesalahan: level generator adalah perkiraan awal; label validasi memakai rubrik relatif kelas. Hanya `status == active` boleh dipakai delivery.

<!-- operational-chapter-balance -->

## Distribusi operasional per bab

Array utama memakai sekitar 30% easy, 40% medium, 30% hard per bab, diranking dari profil bukti. Label AI asli tetap ada di `ai_validation_results.json`. Soal inactive tidak masuk kuota. Confidence N=1 memakai dukungan IndoBERT untuk label operasional (0 jika tidak tersedia), bukan konsistensi satu run.

| Bab | Active | Easy | Medium | Hard |
|---|---:|---:|---:|---:|
| SD5-B1 | 119 | 36 | 47 | 36 |
| SD5-B2 | 149 | 45 | 59 | 45 |
| SD5-B3 | 89 | 27 | 35 | 27 |
| SD5-B4 | 124 | 37 | 50 | 37 |
| SD5-B5 | 111 | 33 | 45 | 33 |
| SD5-B6 | 94 | 28 | 38 | 28 |
| SD5-B7 | 54 | 16 | 22 | 16 |
| SD5-B8 | 83 | 25 | 33 | 25 |
| SD5-B9 | 89 | 27 | 35 | 27 |
