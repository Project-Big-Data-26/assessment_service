# Catatan ekstraksi kelas4

## Bab 1
- Mode prasyarat (subbab I, Faktor dan Kelipatan). Soal I: Siswa p0061 (AB 1, tabel), p0062 (AB 2a-c, 3), p0064 (AB kelipatan 1-4), Uji Kompetensi p0066 no. 7, 8, 14, 15 (UK no. 1-6, 9-13 = subbab A-H).
- Kunci: Guru p0084 (AB faktor), p0086 (AB kelipatan), p0089 (UK no. 6-15, teks soal+kunci satu baris). Pengayaan Guru p0095 hanya operasi hitung (bukan subbab I), tanpa kunci.
- Guru p0086 no. 4 menulis "pada hari ke 6", Siswa "setelah 6 hari" (jawaban sama 12).

## Bab 2
- Mode prasyarat (subbab E, persen). Latihan E: Siswa p0094 Ayo Berlatih (1a-d, 2a-d); Uji Kompetensi p0095-p0096 no. 7-10 = subbab E (no. 1-6 = subbab A-D).
- Kunci: Guru p0122 (Ayo Berlatih p0094), p0123-p0125 (Uji Kompetensi; no. 7-8 di p0124, 9-10 di p0125). Soal Pengayaan di Guru p0130-p0131, kuncinya di p0131.
- Kunci Pengayaan no. 5 SALAH: 5% = 5/10 (PNG Guru hal. 119). Yang benar 5/100 (status tidak_cocok).
- Siswa p0094/p0096 bukan [M]; desimal di Markdown sesuai PNG. p0095 [M][T] (pecahan bersusun) perlu PNG bila subbab A-D diekstrak nanti.

## Bab 4
- Mode prasyarat (subbab B, volume). Subbab B mulai Siswa p0140 (satuan baku volume). Latihan: Ayo Berlatih p0144 (1a-b kotak susu bergambar, 2a-c konversi ml, 3 tangki, 4 tukang susu), Ayo Berlatih p0148-p0149 (1 kubus A-D: img 0148-07 = A+B, 0148-08 = C, 0148-09 = D; 2a-e img 0149-02; 3 menggambar). Uji Kompetensi p0149-p0150: no. 4-7 = subbab B (no. 1-3 = luas, subbab A).
- Kunci: Guru p0170-p0171 (AB p0144), p0173-p0174 (AB kubus), p0177-p0178 (UK 4-7). Soal Pengayaan Guru p0182-p0183, kunci p0183-p0185 (no. 3-5 volume).
- Kunci Pengayaan 5 (drum pernis) SALAH hitung di Guru p0185 (12.136 ml, 12 x 900 = 11.700, sisa 436); soal juga ambigu, dilewati.
- Pengayaan 3 = duplikat Ayo Berlatih 3 (tangki 2.225 liter).

## Bab 5
- Mode prasyarat (subbab B, komposisi/dekomposisi). Subbab B mulai Siswa p0178 (tangram); Aktivitas 6 p0179-p0180, Ayo Berpikir Kreatif p0181, Aktivitas 7 p0182-p0184, Ayo Berlatih p0184 (1 tangram perahu) & p0185 (2 paving). Uji Kompetensi no. 12-15 (p0187-p0188) = subbab B tapi semuanya menggambar/terbuka; no. 1-11 = subbab A.
- Kunci: Guru p0213 (tabel gambar: Segitiga 5, Jajargenjang 1, Persegi 1). Kunci paving (Guru p0214) TIDAK ada, gambar pilihan tanpa lingkaran; Aktivitas 6 no. 7a juga tanpa kunci. Pengayaan Guru p0224-p0225: no. 4-5 (komposisi/dekomposisi) jawabannya kosong.
- Semua gambar tangram/paving tersedia sebagai file img (siswa 0179-12, 0184-10, 0185-06).

## Bab 3
- Mode lengkap (subbab A Pola Gambar, B Pola Bilangan). Latihan 1 (Siswa p0105-p0106, pola gambar) dan Uji Kompetensi no. 1-4 (p0113, pola gambar) SEMUA berbasis gambar dekoratif yang disusun dari puluhan ikon kecil (mis. `panduan_siswa_kelas4.pdf-0105-13.png` s.d. `-53.png` hanya ikon semangka tunggal ~4KB), tidak ada satu file gambar yang memuat pola utuh. Jadi seluruh soal subbab A diberi `butuh_gambar: true, image_refs: []` -> status `needs_image` dan TIDAK terhitung "siap pakai" oleh validator (warning "subbab A 0 soal siap pakai" adalah SAH, bukan bug -- lihat catatan tiap soal). Jawaban dihitung sendiri dari crop PNG (scratchpad), bukan dari kunci Guru (Latihan 1 tidak punya kunci di Buku Guru sama sekali, hanya catatan pedagogis di guru hal. 130-131).
- Latihan 1 no. 4 (belah ketupat) dan no. 5 (pilih gambar kotak kosong) dilewati: no.4 jumlah bentuk ambigu dari gambar (berisiko salah hitung), no.5 formatnya pilih-2-opsi per baris (4 baris), bukan PG 4 opsi standar.
- Kunci Uji Kompetensi no. 1-4 (pola gambar) & no. 5-8 (pola bilangan) ada di Guru p0146 (urutan cetak tercampur: 1,3,2,4 lalu 5,6,7,8 berurutan). Uji Kompetensi no. 9-10 (soal cerita) kuncinya di Guru p0147. Latihan 2 no. 1-7 kuncinya di Guru p0144, no. 8 di Guru p0145.
- Beberapa nomor Latihan 2 (p0111-p0112) dan UK no. 6, no. 8 punya DUA kotak kosong tidak berlabel a/b -> digabung jadi satu jawaban "X dan Y" (lihat catatan tiap soal terkait).
- CATATAN INFRA: `app/services/pretest/llm_backend.py` hilang dari working tree (hanya ada `__pycache__/llm_backend.cpython-313.pyc`, tidak pernah ter-commit di git). `validate.py` mengimpornya untuk `_approx_numeric_value`/`_normalize_for_match`. Sementara ini disalin sebagai `app/services/pretest/llm_backend.pyc` (sourceless module) agar `validate` bisa jalan -- perlu direkonstruksi/dikembalikan sumber aslinya oleh tim.

## Bab 6
- Mode prasyarat (subbab B, diagram batang). Nomor file = nomor halaman di header (p0203 = cetak 191). Siswa: Ayo Berlatih p0203-p0204 (1a-e diagram tegak, 2b-f data teks), Uji Kompetensi p0204-p0206 (no. 3 = diagram batang mendatar; no. 1-2 = piktogram/menggambar).
- Kunci: Guru p0238-p0239 (Ayo Berlatih), p0241 (Uji Kompetensi 3). Soal Pengayaan Guru p0244-p0246, kunci p0247-p0248.
- Kunci Pengayaan 1a salah ketik "365 – (...)" padahal total di soal 346; hasil 54 tetap benar.
- File img diagram (siswa 0203-10, 0205-08; guru 0244-06, 0245-05) utuh, tidak perlu crop.
