---
name: ekstrak-soal-pretest
description: Ekstraksi soal pretest pilihan ganda (1 benar + 3 distraktor) dari Buku Siswa SD-SMA, kunci dari Buku Guru, per bab, dengan validasi mekanis. Pakai saat user minta ekstrak / lanjutkan soal pretest, mis. "/ekstrak-soal-pretest kelas5 bab 1", "/ekstrak-soal-pretest lanjut", atau "/ekstrak-soal-pretest kelas9 semua".
---

# Ekstraksi soal pretest (agentic)

Argumen: `<buku> bab <N>` | `<buku> semua` | `lanjut` (ambil bab berikutnya dari progres).
Semua perintah dijalankan dari root project dengan `venv/Scripts/python` (Windows).

## Mode orkestrator (sesi utama)

1. `venv/Scripts/python -m app.services.pretest.agentic.progress next [--book <buku>]` -> bab berikutnya.
   Kalau buku belum dikonversi: `venv/Scripts/python -m app.services.pretest.agentic.convert --book <buku>`.
2. Untuk SETIAP bab, jalankan subagent `ekstraktor-soal-pretest` dengan prompt
   `buku=<buku> bab_no=<N> halaman=<start>-<end> file=output/pretest/<buku>/bab<NN>.json`.
   Satu bab = satu subagent: konteks tiap bab mulai bersih, jadi sesi utama tetap kecil.
   Beberapa bab dari buku BERBEDA boleh paralel; bab dari buku yang sama berurutan saja
   (mereka berbagi CATATAN.md).
3. Setelah subagent selesai, jalankan validasi ulang sendiri (jangan percaya laporannya):
   `venv/Scripts/python -m app.services.pretest.agentic.validate output/pretest/<buku>/bab<NN>.json`
4. Setelah semua bab sebuah buku OK, rakit pretest ke format tabel `soal` backend:
   `venv/Scripts/python -m app.services.pretest.agentic.pretest --book <buku>`. Setiap
   baris `KURANG` menunjukkan subbab yang belum punya 2 soal, atau bab prasyarat (sering
   dari buku kelas sebelumnya) yang belum diekstrak. Bab prasyarat cukup dikerjakan dengan
   `"mode": "prasyarat"`.
5. Laporkan ke user: jumlah soal, draft vs review, dan WARNING yang tersisa.

Kalau subagent tidak tersedia, kerjakan sendiri dengan "Prosedur per bab" di bawah, satu bab per giliran.

## Prosedur per bab (dikerjakan subagent)

### Tujuan akhir: sesi pretest per bab
Satu sesi pretest = **2 soal PG untuk setiap subbab** + **1 soal PG per bab prasyarat**
(diambil dari subbab TERAKHIR bab prasyarat, yang paling susah). Daftar subbab dan
prasyarat HANYA dari `data/bab_prasyarat/Prasyarat_Math.xlsx`. Lihat dengan:
`venv/Scripts/python -c "from app.services.pretest.agentic import kurikulum as k; print(k.get('<buku>', <N>))"`
Karena itu, setiap subbab bab ini harus punya **≥2 soal siap pakai**. Kalau latihan di
Buku Siswa kurang, cari berurutan di: (1) Uji Kompetensi, (2) Eksplorasi/Ayo Mencoba yang
berupa pertanyaan tertutup dengan jawaban pasti, (3) soal Benar/Salah atau menjodohkan
yang diubah jadi PG (`pertanyaan_disesuaikan: true`), (4) Soal Pengayaan/Remedial/Tambahan
di Buku Guru (`sumber_soal: "guru"`, `source_page` = halaman Guru, id memakai halaman itu).

Mode `prasyarat` (field `"mode": "prasyarat"`): bab diekstrak HANYA untuk subbab
terakhirnya, sebagai sumber soal prasyarat bab lain. Ambil soal-soal subbab terakhir
(usahakan ≥3, termasuk yang tersulit). Subbab lain tidak perlu.

### Aturan harga mati
1. **Soal = salinan verbatim Buku Siswa.** Jangan parafrase, jangan memperbaiki kalimat.
   Validator menolak teks yang tidak ditemukan di halaman sumber ±1. Pengecualian hanya
   notasi matematika (lihat bagian Notasi) dan `pertanyaan_disesuaikan` (lihat bagian Jenis soal).
2. **Soal harus bisa dikerjakan siswa tanpa buku.** Bacaan, tabel, dan data yang
   dirujuk soal masuk ke `stimulus` (juga verbatim). Ini penyebab utama kegagalan pipeline lama.
3. **Kunci jawaban benar diambil dari Buku Guru, lalu dicek dengan pengerjaanmu sendiri.**
   Kerjakan soalnya DULU (`jawaban_agen`), BARU buka kuncinya. Dengan begitu kamu tidak
   terpengaruh kunci saat mengerjakan.
4. **Tepat 1 jawaban benar + 3 distraktor yang pasti salah.**
5. Soal yang tidak bisa dijadikan PG yang adil dicatat di `dilewati` beserta alasannya,
   tidak dipaksakan.

### Langkah
1. **Muat memori (hemat token):**
   - `output/pretest/<buku>/CATATAN.md` kalau ada. Isinya temuan sesi sebelumnya
     tentang buku ini.
   - Bagian bab ini saja dari `data/processed/pretest_md/<buku>/siswa/INDEX.md` dan
     `.../guru/INDEX.md`.
   - Kalau `bab<NN>.json` sudah ada, lanjutkan file itu (JANGAN mulai dari nol).
2. **Baca soal:** buka halaman ★ (`p<PPPP>.md`) di rentang bab, lalu halaman sesudahnya
   sampai latihannya selesai. Soal juga bisa ada di bawah heading yang tidak terdeteksi.
   Untuk menangkapnya, jalankan Grep `^\d{1,2}\. ` di halaman-halaman bab. Soal apersepsi
   di awal bab ("Ayo Mengingat Kembali") juga termasuk. Contoh soal yang sudah dijawab di
   buku (Contoh/Eksplorasi) BUKAN soal latihan.
3. **Per soal:** susun `pertanyaan` + `stimulus` → kerjakan (`jawaban_agen`) → cari kunci
   di Buku Guru → tentukan `jawaban_benar` + 3 distraktor.
4. **Simpan bertahap:** tulis/perbarui `bab<NN>.json` setiap selesai satu section, supaya
   pekerjaan tidak hilang kalau konteks dipadatkan.
5. **Validasi:** `venv/Scripts/python -m app.services.pretest.agentic.validate <file>`.
   Perbaiki semua ERROR. Baca setiap WARNING; perbaiki yang memang salah, dan jelaskan
   di `catatan` untuk yang tidak perlu diperbaiki. Ulangi sampai LOLOS.
6. **Tulis memori:** tambahkan temuan yang berguna untuk bab berikutnya ke
   `output/pretest/<buku>/CATATAN.md` (maks. beberapa baris). Contoh: di mana kunci bab ini
   berada di Buku Guru, pola penomoran yang aneh, halaman yang notasinya rusak.
7. Laporan akhir ke orkestrator (singkat): jumlah soal, dilewati, status_kunci, dan warning
   yang tersisa.

### Jenis soal
- **Sub-soal a/b/c:** setiap sub-soal = satu item (`source_item_no` "4a", "4b").
  Kalimat induk dan data bersama masuk `stimulus`.
- **Sudah pilihan ganda di buku** (Uji Kompetensi A-D/E): pakai opsi dari buku. Untuk
  opsi A-E, ambil 3 distraktor yang paling masuk akal dan tulis di `catatan`.
- **Satu soal meminta beberapa hal** ("tuliskan X dan tentukan Y"): utamakan tetap
  verbatim dengan opsi gabungan yang singkat. Kalau tidak mungkin, ubah seminimal mungkin
  menjadi satu pertanyaan, lalu set `pertanyaan_disesuaikan: true` +
  `catatan_penyesuaian` (soal akan masuk review manusia).
- **Merujuk soal lain** ("dari nomor 1 di atas"): masukkan data yang dirujuk ke `stimulus`.
- **Menjodohkan:** setiap baris = satu soal PG. Kalau baris kiri sudah berupa pertanyaan
  utuh ("Yohana membeli ... Berapa uang yang harus ia bayarkan?"), salin apa adanya dan
  jangan set `pertanyaan_disesuaikan`. Kalau baris kiri hanya label ("Tiga belas ribu
  empat ratus..."), gabungkan dengan kalimat perintahnya dan set `pertanyaan_disesuaikan: true`.
- **Isian kotak/titik-titik:** kotak kosong sering hilang di Markdown, jadi lihat PNG untuk
  posisinya. Tulis kotak sebagai `....` dan set `notasi_dari_png: true`.
- **Benar/Salah:** jadikan PG "Pernyataan manakah yang benar?" (opsi = pernyataan dari
  soal, 1 benar + 3 salah sesuai kunci) atau PG per pernyataan dengan opsi bermakna.
  Set `pertanyaan_disesuaikan: true`. Pretest hanya memakai PG.
- **Lewati** (`dilewati`) soal dengan kategori berikut: jawaban bervariasi/pendapat,
  pembuktian, menggambar/mengukur, proyek, tabel isian banyak, butuh alat peraga, atau
  teks rusak yang tidak terbaca walau sudah dilihat dari PNG.

### Tabel, notasi matematika, gambar
- **Tabel:** Markdown sudah berupa tabel `|...|`. Salin apa adanya ke `stimulus`.
- **Notasi:** halaman bertanda `RISIKO_MATEMATIKA` / `[M]` punya notasi yang rusak di
  Markdown (pecahan bersusun jadi `1<sup>1</sup> 2`, garis pecahan hilang, soal bisa
  hilang total). WAJIB render dan lihat PNG-nya:
  `venv/Scripts/python -m app.services.pretest.agentic.convert render <buku> siswa <hal>`
  lalu Read file PNG yang dihasilkan. Tulis notasinya dalam LaTeX inline: `$1\frac{1}{2}$`,
  `$x^2$`, `$\sqrt{3}$`, `$\angle ABC$`. Set `notasi_dari_png: true`. Teks biasa di
  sekitarnya tetap verbatim. Gunakan LaTeX yang sama di opsi jawaban.
  Kalau Buku Guru bertanda [M], render juga dengan `guru` untuk membaca kuncinya.
- **Teks di dalam gambar `[T]` / `TEKS_DALAM_GAMBAR`:** soal, tabel, atau kunci yang
  didesain sebagai grafik muncul di antara `<!-- Start of picture text -->`. Urutan dan
  pasangannya bisa kacau: garis penghubung atau centang hanya terlihat di gambar, dan
  layout dua kolom bisa tercampur. Lihat PNG sebelum memakainya.
- **Gambar:** gambar tertanam muncul sebagai `![](img/....png)`. Kalau soal tidak bisa
  dijawab tanpa gambar: set `butuh_gambar: true`. Lihat dulu file gambarnya untuk
  memastikan itu gambar yang benar, lalu isi `image_refs: ["img/<nama>.png"]`. Kalau
  gambarnya vektor (tidak ada file img), biarkan `image_refs` kosong; statusnya otomatis
  `needs_image`. Teks yang ada di dalam gambar (label harga, dll.) boleh disalin ke
  stimulus kalau muncul di Markdown sebagai "picture text".
- Jangan render PNG tanpa alasan. Satu PNG ≈ 1.500 token.

### Mencari kunci di Buku Guru
1. Lihat halaman [K] milik bab ini di `guru/INDEX.md`. Cocokkan bab berdasarkan JUDUL,
   bukan nomor, karena ada Buku Guru yang penomorannya sendiri (SMA 10: "Bab 3 | Eksponen" =
   Bab 1 Buku Siswa).
2. Grep kata/angka khas soal di `data/processed/pretest_md/<buku>/guru/`, mis.
   `Kayu Tanam`, `26.932`, atau nama tokoh. Cara ini jauh lebih murah daripada membaca
   banyak halaman.
3. `kunci_guru.kutipan` = potongan TERPENDEK yang disalin persis dari Markdown Guru dan
   memuat jawabannya. `halaman` = nomor file `p<PPPP>.md`. Validator memeriksa kutipan
   ini, termasuk setiap angkanya, di halaman tersebut ±1.
   Untuk kunci GRAFIS (garis menjodohkan, centang di tabel): lihat PNG Guru, isi kutipan
   dengan teks jawaban yang tercetak (mis. `Rp64.000,00`), lalu tulis di `catatan`
   "pasangan dibaca dari PNG Buku Guru hal. N".
   **Kutipan WAJIB memuat jawabannya.** Kalau jawaban hanya terlihat di PNG Guru (tidak
   ada di Markdown), JANGAN mengisi kutipan dengan teks lain di halaman itu supaya lolos
   validator. Isi `"kunci_guru": {"halaman": N, "kutipan": "<jawaban seperti di PNG>",
   "dari_png": true}`. Soal akan diberi flag `kunci_guru_dari_png` dan dicek manusia.
   Mengakali validator = hasil tidak bisa dipercaya.
4. `status_kunci`:
   - `cocok`: kunci Guru = jawaban_agen. Bentuk penulisan boleh beda (2/4 = 1/2).
   - `tidak_cocok`: berbeda. Periksa ulang pengerjaanmu DAN soalnya (termasuk dari PNG).
     Kalau Buku Guru jelas salah ketik atau tidak sesuai soal (contoh nyata: kunci
     Rp15.590,00 untuk soal berlabel Rp15.950,00), `jawaban_benar` = jawabanmu. Selain
     itu, `jawaban_benar` = kunci Guru. Jelaskan di `catatan`; soal otomatis masuk review.
   - `tidak_ada_di_guru`: kunci tidak ditemukan atau berupa "jawaban bervariasi".
     `jawaban_benar` = jawaban_agen, `kunci_guru: null`.
5. Tempat kunci ditemukan ditulis ke CATATAN.md.
6. Kalau kunci Guru hanya menjawab sebagian (mis. hanya angka, padahal soal meminta angka
   dan cara baca), status tetap `cocok` untuk bagian yang ada. Tulis di `catatan` bagian
   mana yang dibuat agen.

### Subbab, tingkat kesulitan, alasan
- `subbab`: kode dari Excel ("A", "B", ...). Tentukan dari ISI soal (konsep yang diuji),
  bukan hanya dari posisi halaman. Soal Uji Kompetensi dan "Ayo Mengingat Kembali" juga
  wajib diberi subbab.
- `tingkat_kesulitan` 1-5 + `alasan_kesulitan` (satu kalimat):
  1 = mengingat/membaca langsung (sebut nama, baca bilangan) · 2 = satu operasi langsung ·
  3 = dua langkah atau konsep + hitung · 4 = soal cerita/tabel multi-langkah ·
  5 = penalaran/analisis beberapa konsep, banyak kemungkinan yang harus diperiksa.
  Dipakai untuk memilih soal prasyarat tersulit. Nilailah dengan jujur, jangan dinaikkan.
- `alasan_benar`: satu kalimat kenapa jawaban benar itu benar (dimasukkan ke
  `options.alasan` tabel soal). `alasan` distraktor = miskonsepsi yang ditiru.

### Distraktor yang baik
- Tiap distraktor meniru SATU kesalahan nyata siswa, misalnya salah nilai tempat, salah
  operasi, lupa meminjam, pembilang dan penyebut tertukar, salah satuan, atau hanya
  menjawab setengah langkah. Tulis kesalahannya di `alasan`.
- Format, satuan, dan panjangnya sejenis dengan jawaban benar. Jawaban benar tidak boleh
  menonjol.
- Distraktor harus PASTI salah. Tidak boleh senilai (2/3 vs 4/6), tidak boleh "semua benar",
  dan tidak boleh bisa dibenarkan dengan tafsiran lain.
- Jangan mengatur posisi A-D; export.py yang mengacak posisinya secara seimbang.

### Format file `output/pretest/<buku>/bab<NN>.json`
Contoh lengkap yang sudah lolos validator: `output/pretest/kelas5/bab01.json` (42 soal,
berbagai kasus: stimulus, sub-soal, menjodohkan, kunci grafis, kunci Guru salah ketik).
Buka satu-dua item dari sana kalau ragu soal format. Jangan membaca seluruh file.
```json
{
  "book": "kelas5", "bab": "Bab 1 - Bilangan Cacah Sampai 100.000", "bab_no": 1,
  "halaman_siswa": [19, 46],
  "soal": [
    {
      "id": "kelas5-b01-p0023-ayo-berpikir-kritis-2",
      "subbab": "A", "tingkat_kesulitan": 3,
      "alasan_kesulitan": "harus mengubah kata bilangan ke angka lalu menentukan nilai tempat tiap angka",
      "sumber_soal": "siswa",
      "source_page": 23, "source_section": "Ayo Berpikir Kritis", "source_item_no": "2",
      "stimulus": "Kecamatan Kayu Tanam terletak di ... tiga belas ribu lima ratus tujuh puluh delapan jiwa perempuan.",
      "pertanyaan": "Tuliskan jumlah penduduk perempuan Kecamatan Kayu Tanam dan tentukan nilai tempatnya.",
      "pertanyaan_disesuaikan": false, "catatan_penyesuaian": null,
      "notasi_dari_png": false, "butuh_gambar": false, "image_refs": [],
      "jawaban_benar": "13.578 (1 puluh ribuan, 3 ribuan, 5 ratusan, 7 puluhan, 8 satuan)",
      "alasan_benar": "tiga belas ribu lima ratus tujuh puluh delapan = 13.578 (= 26.932 - 13.354)",
      "distraktor": [
        {"teks": "13.354 (1 puluh ribuan, 3 ribuan, 3 ratusan, 5 puluhan, 4 satuan)", "alasan": "tertukar dengan jumlah penduduk laki-laki"},
        {"teks": "13.587 (1 puluh ribuan, 3 ribuan, 5 ratusan, 8 puluhan, 7 satuan)", "alasan": "puluhan dan satuan tertukar saat mengubah 'tujuh puluh delapan'"},
        {"teks": "130.578 (1 ratus ribuan, 3 puluh ribuan, 0 ribuan, 5 ratusan, 7 puluhan, 8 satuan)", "alasan": "menulis 'tiga belas ribu' sebagai 130 ribu"}
      ],
      "kunci_guru": {"halaman": 35, "kutipan": "Jumlah penduduk perempuan Kecamatan Kayu Tanam adalah 13.578"},
      "jawaban_agen": "13.578 (26.932 - 13.354 = 13.578, sesuai 'tiga belas ribu lima ratus tujuh puluh delapan')",
      "status_kunci": "cocok", "catatan": null
    }
  ],
  "dilewati": [
    {"source_page": 30, "source_section": "Ayo Berpikir Kritis", "source_item_no": "1",
     "alasan": "soal_terbuka", "keterangan": "memilih mainan beserta alasan (pendapat)"}
  ]
}
```
`id` = `<buku>-b<NN>-p<PPPP>-<slug-section>-<nomor>` (huruf kecil, tanda hubung).
`status`, posisi opsi, dan confidence TIDAK ditulis. Semua dihitung kode dari fakta di atas.
