# Paket soal dengan format LaTeX diperbaiki

Paket ini memuat turunan tampilan semua pretest dan exercise yang tersedia.
Struktur folder dan nama JSON mengikuti ekspor sebelumnya.

- `pretest/<kelas>/soal_pretest_db.json`: master pretest siap impor.
- `exercise/<kelas>/batchNN/soal_exercise_db.json`: master kandidat exercise.
- `.../hasil_validasi/validation_results.json`: keluaran tervalidasi yang telah
  dinormalisasi untuk tampilan, termasuk label/status aslinya.
- Metadata pendamping dan kandidat bab/subbab turut disertakan.
- `manifest.json`: checksum sumber dan turunan, versi kebijakan presentasi.
- `repair_patches.json`: patch teks untuk 53 soal, berdasarkan `_id`/`option_id`.
  Perbarui hanya field terdaftar jika cocok dengan nilai `before`; jika sudah
  `after`, lewati. Nilai yang berbeda dari keduanya perlu diperiksa sebagai konflik.

Gunakan jenis file yang sama dengan jalur import aplikasi saat ini. Jangan
memasukkan master, hasil validasi, dan file kandidat bab sebagai soal terpisah
secara bersamaan karena itu menggandakan record. Pilih berdasarkan `_id` yang
sudah dipakai backend. ID, kunci, label dan isi matematika tidak diganti.

Normalisasi memperbaiki format di 53 soal exercise pada master (74 field).
Perubahan pada salinan kandidat, hasil validasi dan metadata dicatat terpisah
dalam laporan audit. Formula pretest yang sudah benar dipertahankan.

Paket ini tidak mengganti checkpoint/bukti validasi AI asli dan belum diimpor ke
server eksternal. Manifest paket bukan pengganti manifest validasi AI. Gambar
tetap mengikuti referensi aset sebelumnya; paket ini tidak membuat gambar baru.

Frontend perlu renderer KaTeX/MathJax pada soal, stimulus, semua opsi, dan
pembahasan. Baca JSON satu kali; jangan decode backslash ulang atau menghapus
`\\r` yang dapat memotong perintah `\right`. Panduan integrasi:
`API_DOCUMENTATION/44_LATEX_DELIVERY_REPAIR.md` di repository.
