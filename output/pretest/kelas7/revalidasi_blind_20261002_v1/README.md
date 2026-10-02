# Batch validasi blind SMP kelas 7 — 2 Oktober 2026

Batch selesai: 49 soal, 147 run awal sukses, 16 adjudikasi AI, tidak ada run gagal atau adjudikasi tertunda pada hasil akhir. Model penilai `gemini-3.1-flash-lite`; prompt v5 SMP7 dan rubrik `math-rubric-3x4x3-v3-smp7-grade-aware`. Sumber soal/gambar tidak diubah.

| Difficulty | Jumlah |
|---|---:|
| Easy | 28 |
| Medium | 20 |
| Hard | 1 |
| Undecided | 0 |

[Laporan aktif](../hasil_validasi/LAPORAN_VALIDASI.md) dan [kelompok difficulty](../hasil_validasi/difficulty_groups.json) tersedia di `../hasil_validasi/`. Salinan versi ada di [bundle](bundle/README.md). Soal Hard adalah nomor 33, ID `78652b4108bd747c96b2f4a8`.

## Bukti dan batas hasil

- [silver_labels.json](silver_labels.json): seluruh run, hash prompt/respons, solusi, profil difficulty, adjudikasi, serta riwayat retry.
- [audit JSON](audit-v1/pilot_audit.json) dan [audit Markdown](audit-v1/PILOT_AUDIT.md): checkpoint dikunci sebelum pemeriksaan scope model.
- [manifest aktif](../hasil_validasi/manifest.json): hash keluaran dan asal checkpoint/audit.
- [execution_verification.json](execution_verification.json): pemeriksaan offline terhadap checkpoint, ekspor, gambar, scope, dan hash manifest.

SHA-256 sumber: `61fe75b9390d8f01beed20a9a1aa2987a6295529960e5147a5a6104a6bd61ac1`.
SHA-256 checkpoint terkunci: `8385161afcbd16b1f85a606ad5dec927a5100cbf8a963e2d79782fc2364cdbc8`.

Semua soal `pending_expert_review`; gold manusia tetap null. Audit belum mengizinkan ekspansi/training (`readyForExpansion=false`): run 3 soal 37 menandai konflik kunci. Adjudikasi menerima kunci C dengan catatan penghitungan huruf nama. Riwayat konflik tetap utuh, sehingga `requiredEvidenceComplete` FAIL. Gate lain PASS; tidak diperlukan boundary analysis karena ketiga kategori difficulty terisi.

Model IndoBERT lama hanya mencakup SD kelas 1-6. Semua 49 keluaran kelas 7 `out_of_scope`; ketiga head abstain, label/confidence/entropy null, probabilitas kosong. Encoder tidak dijalankan untuk grade ini. Agreement dengan Gemini tidak tersedia. Label advisory sepenuhnya berasal dari penilaian Gemini blind. Tidak ada training, publikasi soal, respons siswa, CTT, atau IRT dalam batch ini.

## Resume dan konfigurasi retry

Run 1 soal 18 gagal beberapa kali karena solusi melebihi batas schema 700 karakter. Resume hanya mengulang run gagal. Percobaan terakhir memakai temperature 0.7 pada proses; prompt/rubrik/schema tetap sama. Run awal lainnya memakai temperature 0.2, sedangkan adjudikasi memakai 0.0. Semua respons final lolos validasi tanpa dipotong atau dilonggarkan. `.env` tidak diubah.

Token sukses yang tercatat: 386.009. Provider dapat mencatat usage tambahan dari percobaan gagal. Packaging dan pemeriksaan offline tidak memanggil LLM. Jangan resume/mengubah checkpoint ini setelah audit; perubahan berikutnya memerlukan direktori versi baru.

Perintah dan aturan rubrik ada di [runbook kelas 7](../../../../API_DOCUMENTATION/29_KELAS7_BLIND_VALIDATION.md).
