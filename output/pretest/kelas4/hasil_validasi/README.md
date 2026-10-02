# Hasil validasi kelas 4

Folder ini adalah satu-satunya hasil validasi aktif untuk kelas ini.

Jumlah soal: **18**. Easy: **14**, Medium: **4**, Hard: **0**, belum diputuskan: **0**.

Mulai dari [LAPORAN_VALIDASI.md](LAPORAN_VALIDASI.md) untuk penjelasan per soal. Label hasil ada di `items[].llmAdvisory.advisoryLabels` pada [validation_results.json](validation_results.json); periksa juga `finalRouting`.

| Isi | Kegunaan |
|---|---|
| [questions.json](questions.json) | Soal, opsi, dan spesifikasi jawaban |
| [indobert_predictions.json](indobert_predictions.json) | Diagnostik model setelah label blind dikunci |
| [difficulty_groups.json](difficulty_groups.json) | Semua kelompok kesulitan |
| [Easy](difficulty/Easy.json), [Medium](difficulty/Medium.json), [Hard](difficulty/Hard.json), [undecided](difficulty/undecided.json) | Subset soal per kesulitan |
| [Checkpoint](bukti_validasi/silver_labels.json) | Tiga run Gemini dan adjudikasi final, byte tetap |
| [Audit](bukti_validasi/PILOT_AUDIT.md) | Gate validasi dan hash checkpoint |
| [manifest.json](manifest.json) | Lokasi sumber dan SHA-256 seluruh berkas hasil |

Metode: Gemini blind N=3, rubrik kelas sasaran, verifikasi kunci dan solusi, adjudikasi AI bila diperlukan, lalu diagnostik IndoBERT. Seluruh label tetap silver/advisory; gold ahli null dan review ahli wajib. Tidak ada training ulang atau pengiriman ke siswa.

Routing: `{"pending_expert_review": 18}`. `readyForExpansion=false`.

Sumber ekstraksi dan gambar berada satu tingkat di atas folder ini. Checkpoint dan audit disalin tanpa mengubah byte; path di dalam audit mencatat lokasi historis saat penilaian. Lokasi berkas yang berlaku saat ini mengikuti manifest. Hasil lama, checkpoint sementara, dan salinan bundle telah dibersihkan.
