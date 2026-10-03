---
name: generate-soal-exercise
description: Generate bank soal LATIHAN (exercise) pilihan ganda per subbab per level (easy/medium/hard) dari Buku Siswa + Buku Guru SD-SMA, dengan pagar format mekanis (validasi mutu oleh tim lain). Pakai saat user minta generate / lanjutkan latihan soal, mis. "/generate-soal-exercise kelas9 bab 1 A easy", "/generate-soal-exercise kelas9 easy", atau "/generate-soal-exercise lanjut".
---

# Generate bank soal latihan (agentic)

Argumen: `<buku> bab <N> <subbab> <level>` | `<buku> bab <N> <level>` | `<buku> <level>` | `lanjut`.
Perintah dijalankan dari root project dengan `venv/Scripts/python` (Windows).
Opsional `batch=<N>` (default 1). Batch baru = tambahan bank soal; soal batch baru WAJIB beda dari
semua soal pretest dan batch sebelumnya (validator memeriksanya).

## Konsep

- Latihan dikerjakan **per subbab**. 1 sesi = 10 (SD) / 15 (SMP) / 20 (SMA) soal dari satu level.
- Bank per subbab per batch = 3 level x kuota: SD 10+10+10, SMP 15+15+15, SMA 20+20+20.
  Kuota per level ada di `app/services/exercise/config.py` (`KUOTA_PER_LEVEL`).
- Yang tampil ke siswa (level mana, soal mana) diputuskan Backend. Tugas di sini hanya bank soalnya.
- Hanya pilihan ganda, **teks saja** (soal bergambar belum didukung): data yang dibutuhkan
  soal (angka, tabel, bacaan) harus ditulis di `stimulus`/`pertanyaan`.
- Export ke `soal_exercise_db.json` mengosongkan `cognitive_level`, `cognitive_score`, `confidence_score`, dan
  `status` (null); itu diisi tahap validasi sistem berikutnya. Nilai usulan kita (level target, skor target,
  jenis soal, acuan, pembahasan) ada di `soal_exercise_meta.json`. `subbab_id` = nama subbab di buku panduan.

## Mode orkestrator (sesi utama)

Untuk SETIAP (subbab, level):

1. Jalankan subagent `generator-soal-exercise` dengan prompt
   `buku=<buku> bab_no=<N> subbab=<K> level=<level> batch=<B> file=output/exercise/<buku>/batch<BB>/bab<NN>/<K>_<level>.json`.
   Satu panggilan = satu subbab + satu level. Level dalam satu subbab dikerjakan BERURUTAN
   easy -> medium -> hard (agen melihat soal level sebelumnya lewat validator/dedup).
   Subbab berbeda boleh paralel.
2. Validasi sendiri (jangan percaya laporan agen):
   `venv/Scripts/python -m app.services.exercise.validate <file>`
3. Setelah semua file satu batch selesai, ekspor ke format tabel `soal`:
   `venv/Scripts/python -m app.services.exercise.export --book <buku> --batch <B>`
4. Validasi mutu (kebenaran kunci, sampling manusia, `confidence_score`, push ke DB) dikerjakan anggota
   tim lain, BUKAN bagian skill ini. `validate.py` di sini hanya pagar generator (format, kuota, duplikat,
   acuan ada di buku) supaya hasil rapi saat diserahkan.
5. Laporkan: jumlah soal per level, rasio variasi/orisinal, sebaran jenis soal, dan WARNING yang tersisa.

## Prosedur per (subbab, level) -- dikerjakan subagent generator

### Dua tipe soal (wajib dicampur sesuai porsi di config; easy 60% variasi)
- **variasi**: tiru kalimat soal yang sudah ada (acuan), tapi
  `variasi_cara: "angka"` -> angka-angkanya diganti (maks 50% angka sama dengan acuan) dan jawabannya
  pasti berbeda; atau `variasi_cara: "konteks"` -> konteks/cerita/objek diganti sehingga kalimatnya jelas
  berbeda (kemiripan kata <= 0.6). Satu acuan maks 2 variasi per level.
  Acuan boleh: soal pretest (`sumber: "pretest"`, cukup `id`), atau soal latihan Buku Siswa
  (`sumber: "siswa"`, `halaman`, `bagian`, `nomor`, `teks` VERBATIM, `jawaban` = kunci Buku Guru yang
  kamu cocokkan sendiri). Acuan siswa/guru dicek validator di halaman +-1. `bagian`/`nomor` bebas
  ("Contoh 1.1" / "1.1"), hanya untuk membedakan acuan. Soal "Contoh"/"Ayo Mencoba" yang jawabannya pasti
  boleh jadi acuan siswa. **Acuan pretest per subbab hanya ~2 soal** (maks 4 variasi), jadi subbab tipis
  WAJIB memakai acuan siswa agar porsi variasi tercapai. `teks`/`kutipan` boleh versi bersih tanpa markup
  (`_x_`, `<sup>`): validator menormalisasi tag HTML dan toleran, tetapi SEMUA angkanya harus ada di halaman.
- **orisinal**: soal baru buatanmu, tapi konsep/rumus/prosedurnya HARUS dari materi subbab di Buku Siswa.
  `acuan` = `{sumber:"siswa", halaman, kutipan}` dengan `kutipan` potongan VERBATIM dari buku yang memuat
  konsep itu (dicek validator). Jangan membawa materi di luar subbab ini.

### Definisi level (dicek validator via `cognitive_c` dan `jumlah_langkah`)
| level  | cognitive_c | jumlah_langkah | ciri |
|--------|-------------|----------------|------|
| easy   | C1-C2 | 1-2 | mengingat/memahami: sebut definisi, kenali bentuk, satu operasi/rumus langsung |
| medium | C3-C4 | 2-4 | menerapkan/menganalisis: dua-tiga langkah, ubah bentuk dulu, soal cerita sederhana |
| hard   | C5-C6 | 3-8 | mengevaluasi/mencipta: banyak konsep, jebakan, bandingkan beberapa kemungkinan |
`jumlah_langkah` = jumlah langkah penyelesaian minimal. Jangan menaikkan level hanya dengan angka besar.
`alasan_level` = satu kalimat kenapa soal ini pantas di level itu. Tulis jujur: validator tim lain akan
membandingkan.

### Aturan harga mati
1. **Kerjakan soalnya DULU, baru tulis kunci.** Hitung ulang dua kali untuk soal berhitung. Satu kunci
   salah merusak kepercayaan siswa; lebih baik membuang soal ragu-ragu.
2. **Tepat 1 jawaban benar + 3 distraktor yang pasti salah.** Tidak boleh dua opsi senilai
   (1/2 vs 2/4), tidak boleh "semua benar/salah/tidak ada jawaban".
3. **Distraktor = kesalahan nyata siswa** (salah operasi, lupa tanda, tertukar, salah satuan, setengah
   langkah). Tulis kesalahannya di `alasan`. Format, satuan, dan panjang sejenis jawaban benar.
4. **Soal harus bisa dijawab tanpa buku/gambar.** Dilarang "perhatikan gambar", "tabel di atas",
   "pada buku". Data masuk `stimulus` (tabel Markdown boleh).
5. **Notasi LaTeX inline**: `$x^2$`, `$\frac{a}{b}$`, `$\sqrt{3}$`, juga di opsi.
6. **Tidak ada soal kembar.** Soal baru wajib beda dari soal pretest, batch lain, dan soal lain di file ini.
   Variasi yang hanya mengganti satu angka kecil dianggap buruk: ubah struktur nilainya.
7. Jangan menyusun posisi A-D; kode yang mengacak. `jawaban_benar` dan `distraktor` hanya teks.
8. **Keragaman jenis soal.** Isi `jenis_soal` (label singkat, mis. "mengenali bentuk", "menentukan nilai
   variabel", "menyusun model", "menafsirkan penyelesaian", "membandingkan") di SEMUA soal. Validator menolak
   bila satu jenis > 1/3 kuota level atau jenisnya < 3. Rencanakan sebaran jenis SEBELUM menulis, lihat jenis
   yang sudah dipakai level sebelumnya di subbab yang sama, dan cakup konsep subbab secara merata
   (bukan hanya pola soal latihan yang paling banyak).

### Langkah
1. Muat memori (hemat token): `output/pretest/<buku>/CATATAN.md` (pola halaman/notasi buku ini) dan
   `output/exercise/<buku>/CATATAN.md` kalau ada. Lihat subbab dan halamannya:
   `venv/Scripts/python -c "from app.services.pretest.agentic import kurikulum as k; print(k.get('<buku>', <N>))"`
   dan bagian bab ini di `data/processed/pretest_md/<buku>/siswa/INDEX.md`.
2. Kumpulkan **bahan acuan** subbab itu: soal pretest subbab (di `output/pretest/<buku>/bab<NN>.json`),
   soal latihan Buku Siswa di halaman subbab, dan konsep/rumus subbab. Cari kunci di Buku Guru (Grep angka
   khas), jangan membaca seluruh Buku Guru. Halaman bertanda [M]/notasi rusak: render PNG
   (`venv/Scripts/python -m app.services.pretest.agentic.convert render <buku> siswa <hal>`) lalu Read.
3. Kalau file sudah ada, lanjutkan (jangan mulai dari nol). Level sebelumnya di subbab yang sama:
   baca soalnya (jangan diulang polanya).
4. Tulis soal bertahap ke file (simpan setiap ~5 soal), validasi dengan `--partial`:
   `venv/Scripts/python -m app.services.exercise.validate <file> --partial`. Setelah kuota penuh,
   validasi TANPA `--partial` sampai LOLOS. Perbaiki setiap ERROR; baca WARNING.
5. Kalau kapasitas subbab tidak cukup untuk kuota tanpa soal nyaris kembar, JANGAN dipaksa:
   laporkan "kapasitas subbab tidak cukup" beserta jumlah soal yang layak.
6. Tulis temuan berguna (di mana kunci, halaman rusak, pola yang gagal) ke
   `output/exercise/<buku>/CATATAN.md` (beberapa baris saja).
7. Laporan akhir 5-10 baris: jumlah soal, variasi/orisinal, warning tersisa dan alasannya.

### Format file `output/exercise/<buku>/batch<BB>/bab<NN>/<K>_<level>.json`
```json
{
  "book": "kelas9", "bab_no": 1, "subbab": "A", "level": "easy", "batch": 1,
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
Cek ID pretest yang tersedia dengan Grep `"id":` di `output/pretest/<buku>/bab<NN>.json`.
