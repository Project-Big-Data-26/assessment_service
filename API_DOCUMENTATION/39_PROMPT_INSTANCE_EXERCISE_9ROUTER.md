# Prompt Instance: Pembuatan Soal Latihan via 9Router

Contoh nyata prompt untuk satu tugas: **Kelas 9, Bab 2 (Bangun Ruang), Subbab A, tingkat mudah**.
Dirender oleh `app/services/exercise/llm_generate.py` (kelas `_Context`, metode `prompt`). Isi lengkap sekitar 15.000 karakter;
bagian yang panjang dipotong dengan `[...]` di bawah.

## 1. Struktur prompt (5 blok)

| Blok | Isi | Dari mana |
|---|---|---|
| Pesan sistem | Peran AI dan aturan balasan (hanya JSON) | Tetap, di kode |
| 1. Tugas | Subbab, tingkat, jumlah soal, jumlah soal "variasi" | Dihitung program per putaran |
| 2. Aturan penulisan | Tipe soal, definisi tingkat, aturan harga mati | Dimuat dari `SKILL.md` |
| 3. Format balasan | Bentuk JSON soal dan acuan | Tetap, di kode |
| 4. Bahan | Isi Buku Siswa subbab, soal pretest, soal yang sudah ada | Dari data buku |

Tambahan di putaran berikutnya: soal yang sudah diterima, acuan yang sudah terpakai, dan alasan soal yang ditolak (umpan balik).

## 2. Pesan sistem (AI Penulis)

```text
Kamu penulis soal latihan pilihan ganda untuk buku pelajaran sekolah Indonesia.
Kamu TIDAK punya alat/berkas: semua bahan ada di pesan ini. [...]
Kerjakan setiap soal sampai selesai di benakmu SEBELUM menulis kunci; buang soal yang kuncinya ragu-ragu.
Balas HANYA satu objek JSON valid, tanpa teks lain.
```

## 3. Pesan pengguna (ringkas)

```text
# Tugas
Tulis 5 soal BARU untuk Bangun Ruang (bab 2), subbab A. Klasifikasi Bangun Ruang dan Jaring-Jaring,
level **easy** (SMP, kelas kelas9).

Level easy: cognitive_c C1/C2, jumlah_langkah 1-2. Kuota level 15 soal; target variasi total 9.
Dari 5 soal ini, TEPAT 3 bertipe variasi (sisanya orisinal). Jumlah itu wajib: porsi variasi satu level dicek validator.

# Aturan penulisan                                   <- dimuat dari SKILL.md
- variasi: tiru kalimat soal acuan, ganti angka (maks 50% sama) atau ganti konteks. Satu acuan maks 2 variasi.
- orisinal: soal baru, tetapi konsep harus dari materi subbab di Buku Siswa, dengan kutipan verbatim.
- Level easy = C1-C2, 1-2 langkah. Medium = C3-C4. Hard = C5-C6 (kesulitan dari penalaran, bukan hitung panjang).
- Tepat 1 jawaban benar + 3 pilihan salah yang pasti salah; pilihan salah = kesalahan nyata siswa.
- Soal harus bisa dijawab tanpa gambar atau buku; data ditulis di soal. [...]

# Format balasan
{"soal": [ {"tipe_generate": "variasi|orisinal", "acuan": {...}, "cognitive_c": "C1",
            "jumlah_langkah": 1, "pertanyaan": "...", "jawaban_benar": "...",
            "distraktor": [{"teks": "...", "alasan": "..."} x3], "pembahasan": "..."} ]}

# Materi Buku Siswa subbab ini (halaman 63-69)
=== HALAMAN 63 ===
A. Klasifikasi Bangun Ruang dan Jaring-Jaring ... Eksplorasi 2.1 Mengelompokkan Kemasan [...]
=== HALAMAN 64 === [...]

# Soal pretest subbab ini (acuan variasi)
- id: kelas9-b02-p0069-latihan-a-3
  soal: Dapatkah kita membuat jaring-jaring bangun ruang bola?
  jawaban: Ya, jaring-jaring bangun ruang bola dapat dibuat [...]
```

## 4. Contoh keluaran AI Penulis (1 soal, dari uji nyata)

```json
{
  "tipe_generate": "orisinal",
  "cognitive_c": "C2", "jumlah_langkah": 1,
  "pertanyaan": "Suatu polihedron memiliki $6$ sisi dan $8$ titik sudut. Berdasarkan rumus polihedron Euler
                 $S + T - R = 2$, banyak rusuk ($R$) pada polihedron tersebut adalah ....",
  "jawaban_benar": "$12$",
  "distraktor": [
    {"teks": "$14$", "alasan": "Lupa mengurangkan dengan 2, hanya menjumlahkan S + T"},
    {"teks": "$16$", "alasan": "Salah operasi: R = 14 + 2"},
    {"teks": "$10$", "alasan": "Salah memakai rumus"}
  ],
  "pembahasan": "6 + 8 - R = 2, sehingga R = 12."
}
```

## 5. Prompt AI Pengerja (verifikasi buta)

Menerima hanya teks soal dan 4 pilihan. Tidak ada kunci, alasan, pembahasan, atau tingkat.

```text
Kamu siswa penyelesai soal yang teliti dan independen.
Kerjakan setiap soal pilihan ganda DARI NOL (hitung/telusuri sendiri, jangan menebak dari bentuk opsi).
TULIS PENGERJAANMU di "kerja" SEBELUM memilih. Pilih tepat satu opsi A-D.
Kalau tidak ada opsi yang benar, atau lebih dari satu yang benar, tulis "pilihan": null.
Balas HANYA JSON: {"jawaban": {"<id soal>": {"kerja": "...", "pilihan": "B", "langkah": 2}}}
```

## Cara merender prompt asli lengkap

```bash
venv/Scripts/python -c "from app.services.exercise import llm_generate as G; \
c=G._Context(G.Job('kelas9',2,'A','easy')); print(c.prompt(5, 3, [], []))"
```
