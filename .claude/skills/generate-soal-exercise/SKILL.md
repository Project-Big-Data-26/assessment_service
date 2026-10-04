---
name: generate-soal-exercise
description: Generate bank soal LATIHAN (exercise) pilihan ganda per subbab per level (easy/medium/hard) dari Buku Siswa SD-SMA (v1), dengan pagar format mekanis. Validasi mutu, sampling, dan confidence dikerjakan tim lain. Pakai saat user minta generate / lanjutkan latihan soal, mis. "/generate-soal-exercise kelas9 bab 1 A easy", "/generate-soal-exercise kelas9 easy", atau "/generate-soal-exercise lanjut".
---

# Generate bank soal latihan (agentic) -- SKILL v1

Versi skill ini: **v1**. Setiap file hasil WAJIB memuat `"skill_versi": "v1"` di tingkat file (sejajar `book`),
supaya mutu hasil versi ini bisa dibandingkan dengan versi lain (mis. model lain di 9router).
Argumen: `<buku> bab <N> <subbab> <level>` | `<buku> bab <N> <level>` | `<buku> <level>` | `lanjut`.
Perintah dijalankan dari root project dengan `venv/Scripts/python` (Windows).
Opsional `batch=<N>` (default 1). Batch baru = tambahan bank soal; soal batch baru WAJIB beda dari
semua soal pretest dan batch sebelumnya (validator memeriksanya).

## Konsep

- Latihan dikerjakan **per subbab**. 1 sesi = 10 (SD) / 15 (SMP) / 20 (SMA) soal dari satu level.
- Bank per subbab per batch = 3 level x kuota: SD 10+10+10, SMP 15+15+15, SMA 20+20+20
  (`KUOTA_PER_LEVEL` di `app/services/exercise/config.py`).
- Yang tampil ke siswa (level mana, soal mana) diputuskan Backend. Tugas di sini hanya bank soalnya.
- Level easy/medium/hard hanya **perkiraan awal**: tim data mengkalibrasinya dengan IRT dari jawaban siswa.
  Karena itu: jangan memaksa kuota hard dengan soal nyaris kembar; sebaran kesulitan yang lebar di dalam
  level (medium atas, hard bawah) lebih berguna daripada kuota yang penuh.
- Hanya pilihan ganda, **teks saja** (soal bergambar belum didukung): data yang dibutuhkan soal
  (angka, tabel, bacaan) harus ditulis di `stimulus`/`pertanyaan`.
- Export ke `soal_exercise_db.json` mengosongkan `cognitive_level`, `cognitive_score`, `confidence_score`, dan
  `status` (null); itu diisi tahap validasi tim lain. Info pendamping (level target, tipe, acuan, pembahasan,
  penanda) ada di `soal_exercise_meta.json`. `subbab_id` = nama subbab di buku panduan.
- Soal yang sudah diserahkan tidak diedit; tambahan/perbaikan lewat batch baru.

## Mode orkestrator (sesi utama)

Untuk SETIAP (subbab, level):

1. Jalankan subagent `generator-soal-exercise` dengan prompt
   `buku=<buku> bab_no=<N> subbab=<K> level=<level> batch=<B> file=output/exercise/<buku>/batch<BB>/bab<NN>/<K>_<level>.json`.
   Satu panggilan = satu subbab + satu level. Level dalam satu subbab dikerjakan BERURUTAN
   easy -> medium -> hard (agen membaca soal level sebelumnya). Subbab berbeda boleh paralel,
   tetapi **maksimal 2-3 agen sekaligus**: lebih banyak memicu batas sesi API (rate limit) yang
   menghentikan agen sebelum menulis apa pun. Minta agen menyimpan file bertahap (tiap ~5 soal).
   Sebutkan di prompt: jenjang, kuota level, porsi variasi, dan nama skrip bantu yang UNIK
   (mis. `<buku>_<K>_<level>_gen.py`); skrip bernama sama pernah saling menimpa antar agen paralel.
2. Validasi sendiri (jangan percaya laporan agen):
   `venv/Scripts/python -m app.services.exercise.validate <file>`
3. Setelah semua file satu batch selesai, ekspor:
   `venv/Scripts/python -m app.services.exercise.export --book <buku> --batch <B>`
   (menulis master, meta, `per_subbab/` untuk koreksi manusia, dan `README.md` serah-terima).
4. Validasi mutu (kebenaran kunci, sampling manusia, `confidence_score`, IRT, push ke DB) dikerjakan anggota
   tim lain, BUKAN bagian skill ini. `validate.py` hanya pagar generator (format, kuota, duplikat, acuan ada di buku).
5. Laporkan: jumlah soal per level, rasio variasi/orisinal, sebaran jenis soal, file yang kapasitasnya kurang,
   dan WARNING yang tersisa.

## Prosedur per (subbab, level) -- dikerjakan subagent generator

### Dua tipe soal
Porsi variasi (sisanya orisinal): easy 60%, medium 50%, hard sekitar 30% **tanpa batas bawah** (toleransi ±2
soal; hard boleh 0 variasi). Jangan melabeli soal sebagai variasi hanya demi porsi.
- **variasi**: tiru kalimat soal yang sudah ada (acuan), dengan
  `variasi_cara: "angka"` -> ganti SEMUA angka (maks 50% angka sama dengan acuan; koefisien kecil 1/2/3
  mudah kebetulan sama, pakai 4-9 atau nilai besar yang jauh berbeda) dan jawabannya pasti berbeda; atau
  `variasi_cara: "konteks"` -> cerita/objek diganti sehingga kalimatnya jelas berbeda (kemiripan kata <= 0.6).
  Satu acuan maks 2 variasi per level.
  - Acuan **tanpa angka**, atau angka yang ditulis kata ("sepuluh"), hanya boleh `variasi_cara: "konteks"`
    (validator hanya mengenali angka digit).
  - **Jawaban variasi tidak boleh sama dengan jawaban acuan.** Acuan berjawaban kategori ("tidak ada solusi",
    "banyak solusi") harus divariasikan ke kategori atau bentuk jawaban lain.
  - Acuan harus **soal asli** (pretest atau Buku Siswa), bukan potongan penyelesaian ("Substitusikan ...") dan
    bukan teks pengganti untuk soal bergambar. Kalau tidak ada acuan layak, jadikan soal itu `orisinal`.
  - Acuan boleh: pretest (`sumber: "pretest"`, cukup `id`; cek ID asli dengan Grep `"id":` di
    `output/pretest/<buku>/bab<NN>.json`, ID tidak selalu sama dengan halaman yang diduga), atau Buku Siswa
    (`sumber: "siswa"`, `halaman`, `bagian`, `nomor`, `teks` VERBATIM, `jawaban`). `halaman` = nomor file `p<PPPP>.md`
    (bukan nomor cetak buku). Soal "Contoh"/"Ayo Mencoba"/"Latihan" yang jawabannya pasti boleh jadi acuan.
  - **Acuan pretest per subbab hanya ~2 soal** (maks 4 variasi), jadi subbab tipis, dan jenjang SMA, WAJIB
    memakai acuan siswa. Pakai acuan yang berbeda per level; acuan habis cepat di easy.
  - `teks`/`kutipan` boleh versi bersih tanpa markup (`_x_`, `<sup>`): validator normalisasi tag HTML dan toleran,
    tetapi SEMUA angkanya harus ada di halaman. Teks yang pecah baris (tabel) berisiko gagal verbatim: pakai
    kalimat utuh dari halaman teks biasa.
  - `jawaban` acuan boleh dihitung sendiri. Kunci Buku Guru hanya cek tambahan (kadang berupa gambar, kadang
    salah ketik atau tertukar label: kalau berbeda dari hitunganmu, percaya hitunganmu dan catat di CATATAN.md).
- **orisinal**: soal baru buatanmu, tapi konsep/rumus/prosedurnya HARUS dari materi subbab di Buku Siswa.
  `acuan` = `{sumber:"siswa", halaman, kutipan}` dengan `kutipan` potongan VERBATIM dari buku yang memuat
  konsep itu (dicek validator). Jangan membawa materi di luar subbab ini.

### Definisi level (dicek validator via `cognitive_c` dan `jumlah_langkah`)
| level  | cognitive_c | jumlah_langkah | ciri |
|--------|-------------|----------------|------|
| easy   | C1-C2 | 1-2 | mengingat/memahami: sebut definisi, kenali bentuk, satu operasi/rumus langsung |
| medium | C3-C4 | 2-4 | menerapkan/menganalisis: dua-tiga langkah, ubah bentuk dulu, soal cerita sederhana |
| hard   | C5-C6 | 3-8 | mengevaluasi/mencipta: evaluasi klaim, temukan kesalahan, bandingkan kemungkinan, rancang |
- `jumlah_langkah` = langkah penyelesaian MINIMAL; tulis jujur. Pada percobaan awal generator cenderung
  membesarkan 1-2 langkah. Jangan menaikkan level hanya dengan angka besar.
- Hard = kesulitan dari **penalaran** (jebakan, evaluasi klaim, syarat ganda, parameter, perancangan), bukan
  hitung panjang dan bukan materi di luar subbab. Di SD dan SMA hard sering hanya setara medium atas; itu wajar,
  tulis jujur di `alasan_level`.
- Medium harus benar-benar lebih sulit dari easy (bukan easy dengan angka lebih besar); hard tidak boleh sekadar
  medium dengan langkah tambahan. Lihat soal level sebelumnya agar tidak mengulang pola.
- `alasan_level` = satu kalimat kenapa soal pantas di level itu.

### Aturan harga mati
1. **Kerjakan soalnya DULU, baru tulis kunci**, dua kali (untuk hitungan boleh dengan skrip). Satu kunci salah
   merusak kepercayaan siswa dan akan terbaca "sulit" oleh kalibrasi IRT; buang soal yang ragu-ragu.
2. **Tepat 1 jawaban benar + 3 distraktor yang pasti salah**, tanpa ambigu. Tulis syarat eksplisit: himpunan
   bilangan (cacah/bulat/real), "dadu/koin setimbang", "dengan/tanpa pengembalian", "salah satu jenis boleh nol"
   dsb. Tidak boleh dua opsi senilai (1/2 vs 2/4), tidak boleh "semua benar/salah/tidak ada jawaban".
   Hindari opsi Ya/Tidak dan soal berjawaban banyak ("kombinasi yang mungkin"): ubah jadi nilai terbesar/terkecil
   atau banyak cara. Soal parameter bertanya nilai yang membuat suatu sifat, bukan "agar tidak ada solusi"
   (semua nilai lain ikut benar). Hindari soal pendapat/subjektif ("urutan keterwakilan").
   Opsi "<, >, =" tidak bisa jadi 4 pilihan: ubah jadi "pernyataan yang benar" dengan 4 pernyataan.
3. **Distraktor = kesalahan nyata siswa**, tulis kesalahannya di `alasan`: salah operasi, lupa tanda, tertukar
   variabel/nilai tempat, salah satuan (ribu/juta, kg/ons), batas `<` vs `<=`, pembulatan, nol di depan/nol hilang,
   setengah langkah. Format, satuan, dan panjang sejenis jawaban benar. Tiap distraktor di soal bersyarat
   melanggar tepat satu syarat; cek satu per satu agar tidak ada dua jawaban benar.
4. **Soal harus bisa dijawab tanpa buku/gambar.** Dilarang "perhatikan gambar", "tabel di atas", "pada buku".
   Data masuk `stimulus` (tabel Markdown boleh). Soal menggambar/grafik tidak didukung.
5. **Notasi.** SMP-SMA: LaTeX inline `$x^2$`, `$\frac{a}{b}$`, juga di opsi. SD: angka biasa polos tanpa LaTeX,
   format Indonesia (titik ribuan `125.430`, koma desimal `3,5`). Tanda kutip lurus (`"`), bukan kutip lengkung.
6. **Tidak ada soal kembar.** Soal baru wajib beda dari soal pretest, batch lain, dan soal lain di file ini.
   Variasi yang hanya mengganti satu angka kecil dianggap buruk: ubah struktur nilainya. Jawaban akhir jangan
   berulang-ulang di satu level (ubah angka agar jawaban beragam).
7. Jangan menyusun posisi A-D; kode yang mengacak. `jawaban_benar` dan `distraktor` hanya teks.
8. **Keragaman jenis soal.** Isi `jenis_soal` (label singkat) di SEMUA soal. Validator menolak bila satu jenis
   > 1/3 kuota level (SD 4, SMP 5, SMA 7) atau jenisnya < 3. Rencanakan sebaran SEBELUM menulis, lihat jenis
   yang dipakai level sebelumnya, dan cakup konsep subbab secara merata.

### Aturan per jenjang
- **SD** (kuota 10): bahasa dan konteks kelas bersangkutan (kalimat pendek, konteks sehari-hari, istilah persis
  seperti di buku). Opsi sering teks (cara baca, nilai tempat): distraktor = menggeser digit/nol, bukan nilai acak.
  Stimulus bersama dan contoh bergambar di pretest tidak ikut: tulis ulang datanya di pertanyaan.
  Kunci Buku Guru SD kadang punya selisih halaman PDF (cetak + 12).
- **SMP** (kuota 15): tabel frekuensi/data ditulis sebagai tabel Markdown di `stimulus`.
- **SMA** (kuota 20): variasi jenis harus lebih luas; kuota 20 per level cepat memunculkan soal nyaris kembar.
  Contoh, Ayo Mencoba, dan kunci Guru sering berupa gambar: pilih acuan yang teksnya terbaca. Kalau notasi di
  halaman rusak (`[M]`), render PNG. Nomor cetak buku = nomor file dikurangi 16 (kelas 10; cek per buku).

### Kapasitas dan penanda
- Kalau kapasitas subbab tidak cukup untuk kuota tanpa soal nyaris kembar atau di luar materi, **JANGAN dipaksa.**
  Tulis hanya soal yang layak lalu nyatakan di file: `"kapasitas_kurang": true` dan `"alasan_kapasitas": "<alasan jelas>"`
  (tingkat file). Validator hanya menerima jumlah di bawah kuota bila dinyatakan begitu.
- `"dipaksa_kuota": true` (per soal) HANYA bila pengguna memutuskan kuota harus penuh walau bahan habis; wajib
  disertai `catatan` yang menjelaskan kerentanannya.

### Langkah
1. Muat memori (hemat token): `output/pretest/<buku>/CATATAN.md`, `output/exercise/<buku>/CATATAN.md`, dan
   `output/exercise/kelas9/CATATAN.md` (tips umum). Lihat subbab/halaman:
   `venv/Scripts/python -c "from app.services.pretest.agentic import kurikulum as k; print(k.get('<buku>', <N>))"`
   dan bagian bab ini di `data/processed/pretest_md/<buku>/siswa/INDEX.md`.
2. Kumpulkan **bahan acuan** subbab: soal pretest subbab, soal latihan Buku Siswa di halaman subbab, dan
   konsep/rumus subbab. Kunci Buku Guru boleh dicek dengan Grep angka khas (jangan membaca seluruh Buku Guru).
   Halaman `[M]`/notasi rusak: render PNG
   (`venv/Scripts/python -m app.services.pretest.agentic.convert render <buku> siswa <hal>`) lalu Read.
3. Kalau file sudah ada, lanjutkan (jangan mulai dari nol). Baca soal level sebelumnya di subbab yang sama.
4. Tulis soal bertahap (simpan tiap ~5 soal). Skrip bantu bernama unik; tulis skrip dengan tool Write, bukan
   heredoc shell panjang (sering gagal di Windows). Validasi dengan `--partial` selama berjalan:
   `venv/Scripts/python -m app.services.exercise.validate <file> --partial`. Setelah kuota penuh (atau kapasitas
   kurang dinyatakan), validasi TANPA `--partial` sampai LOLOS. Baca setiap WARNING.
5. Tulis temuan berguna (kunci Guru salah/tertukar, halaman rusak, acuan yang tidak layak, pola yang gagal) ke
   `output/exercise/<buku>/CATATAN.md` dengan Edit di baris baru akhir file (file dipakai bersama agen paralel).
6. Laporan akhir 5-10 baris: jumlah soal, variasi/orisinal, kapasitas aktual, warning tersisa dan alasannya.

### Format file `output/exercise/<buku>/batch<BB>/bab<NN>/<K>_<level>.json`
```json
{
  "book": "kelas9", "bab_no": 1, "subbab": "A", "level": "easy", "batch": 1, "skill_versi": "v1",
  "soal": [
    {
      "id": "kelas9-b01-a-easy-bt01-001",
      "tipe_generate": "variasi", "variasi_cara": "angka",
      "acuan": {"sumber": "pretest", "id": "kelas9-b01-p0025-ayo-mencoba-1"},
      "cognitive_c": "C2", "jumlah_langkah": 2, "jenis_soal": "menyusun model",
      "alasan_level": "menerjemahkan keliling segitiga ke bentuk 2x + y = K, satu pemodelan langsung",
      "stimulus": null,
      "pertanyaan": "Keliling sebuah segitiga sama kaki adalah 54 cm. Model matematika ... adalah ....",
      "jawaban_benar": "$2x + y = 54$",
      "alasan_benar": "dua sisi sama panjang $x$ dan satu sisi $y$, sehingga keliling $2x + y$",
      "distraktor": [
        {"teks": "$x + y = 54$", "alasan": "lupa menghitung dua sisi yang sama panjang"},
        {"teks": "$x + 2y = 54$", "alasan": "variabel sisi sama dan sisi alas tertukar"},
        {"teks": "$2x + 2y = 54$", "alasan": "mengira kedua variabel dikalikan 2"}
      ],
      "pembahasan": "Segitiga sama kaki: dua sisi $x$, alas $y$. Keliling = $2x + y = 54$.",
      "catatan": null
    }
  ]
}
```
`id` = `<buku>-b<NN>-<subbab huruf kecil>-<level>-bt<BB>-<NNN>`. Acuan siswa/guru untuk variasi memakai
`{"sumber":"siswa","halaman":25,"bagian":"Latihan A","nomor":"2","teks":"...","jawaban":"..."}`;
acuan orisinal `{"sumber":"siswa","halaman":24,"kutipan":"...potongan buku..."}`.
Kapasitas kurang: tambahkan di tingkat file `"kapasitas_kurang": true, "alasan_kapasitas": "..."`.
