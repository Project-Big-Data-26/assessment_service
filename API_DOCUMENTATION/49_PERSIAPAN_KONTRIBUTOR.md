# Persiapan kontributor sebelum menjalankan AI agent

Panduan ini untuk teman yang baru bergabung. Baca dan siapkan kebutuhan di
bawah **sebelum memberikan [instruksi kerja 48](48_AGENT_GENERATE_VALIDASI_SOAL.md)
kepada AI agent**. Bagian login akun, pembuatan API key, pengisian rahasia dan
pilihan biaya dilakukan oleh pemilik akun sendiri. Agent dapat membantu setup
program dan memeriksa kesiapan tanpa menampilkan rahasia.

## 1. Apa saja yang harus disiapkan?

| Kebutuhan | Disiapkan oleh | Tanda sudah siap |
|---|---|---|
| Repository proyek dan aksesnya | Tim memberi akses; kontributor clone/menyalin | Folder berisi `app/`, `scripts/`, `requirements.txt`, `.env.example` |
| Komputer/environment untuk menjalankan script | Kontributor | Python 3.12 dan terminal PowerShell tersedia |
| AI agent dengan akses folder dan terminal | Kontributor | Agent dapat membaca kode dan menjalankan perintah di root proyek |
| Kelas, bab/subbab, jumlah dan pembagian batch | Koordinasi tim | Tugas tercatat; tidak bertabrakan dengan kontributor lain |
| Excel kurikulum, buku dan hasil ekstraksi | Tim membagikan paket sumber | File berada pada struktur folder di bagian 3 |
| Akses generator 9Router | Kontributor atau pengelola server tim | URL `/v1`, API key dan model generator tersedia |
| API key Gemini untuk validasi | Kontributor melalui akun sendiri | Key pribadi tersimpan di `.env` pada environment eksekusi |
| Kuota/biaya layanan yang akan dipakai | Pemilik akun/provider | Pemilik akun memahami layanan dan batas request yang diizinkan |
| Artifact IndoBERT untuk diagnostik bila diperlukan | Tim | Folder model lengkap sesuai manifest, bukan folder kosong |

**AI agent mengoperasikan script. Akses model generator dan validator berasal
dari konfigurasi provider proyek yang Anda siapkan.** Menggunakan agent yang
bisa membantu menulis kode belum menyiapkan koneksi Gemini/9Router untuk script.

## 2. Dapatkan proyek dan siapkan komputer

Minta tim memberikan URL repository atau salinan proyek dan commit/versi yang
dipakai. Jika memakai Git, install Git lalu clone URL yang diberikan tim.
Jangan menyalin path komputer pembuat proyek sebagai alamat repository.

Buka folder proyek di IDE. Root proyek adalah folder tempat `requirements.txt`,
`app/` dan `scripts/` berada. Dari terminal folder tersebut, periksa:

```powershell
python --version
git --version
Get-Location
Test-Path -LiteralPath 'requirements.txt'
```

Gunakan Python 3.12 sesuai environment proyek. Perintah Git hanya diperlukan
jika proyek diperoleh/dikelola melalui Git. Jika `python` tidak dikenali,
perbaiki instalasi/PATH atau gunakan launcher Python yang tersedia.

Agent boleh membantu membuat `.venv` dan menginstal dependency mengikuti
bagian 3 dokumen 48. Langkah ini memerlukan akses unduhan paket dan ruang untuk
dependency machine learning/OCR yang tercantum di proyek. Tidak perlu menjalankan
server website, MongoDB, S3 atau database production untuk alur file lokal ini.

**Jika agent berjalan di cloud/container/komputer lain**, repository, sumber,
dependency dan `.env` harus tersedia pada environment tempat script benar-benar
dijalankan. File `.env` yang hanya ada di laptop Anda tidak otomatis terbaca
oleh proses di komputer lain. Gunakan mekanisme secret environment tersebut
jika tersedia; jangan menempelkan key ke percakapan.

## 3. Minta paket data kepada tim

Clone repository belum cukup karena beberapa folder data/model diabaikan Git.
Untuk kelas yang dikerjakan, minta paket berikut dan pertahankan nama/struktur:

```text
data/
  bab_prasyarat/Prasyarat_Math.xlsx
  sd/panduan_siswa_kelas1.pdf                 # contoh kelas 1
  processed/pretest_md/kelas1/siswa/
    index.json
    p0001.md
    p0002.md
    ...                                     # halaman sesuai index/sumber
models/
  indobert-3x4x3-v1/                         # bila diperlukan saat packaging
```

Buku kelas 7–9 berada di bawah `data/smp/`; kelas 10–12 di `data/sma/`.
Nama buku dan aturan jalur TL dijelaskan pada bagian 4 dokumen 48. Sertakan
aset yang dirujuk halaman bila ada. Minta sumber dan versi yang sama dengan
yang ditetapkan tim; jangan membuat file kosong agar pemeriksaan lolos.

Tim juga perlu menetapkan siapa mengerjakan kelas/subbab mana dan batch baru
yang digunakan. Jika masing-masing bekerja pada clone terpisah, pemilihan
nomor otomatis hanya melihat komputer masing-masing; koordinasikan nomor batch
agar dua kontribusi tidak memakai identitas kelas/batch yang sama.

## 4. Buat API key Gemini sendiri

1. Buka [Google AI Studio](https://aistudio.google.com/) dan login menggunakan
   akun Google yang akan dipakai untuk kontribusi.
2. Buka halaman API keys melalui menu AI Studio. Pilih atau buat project yang
   Anda kelola, lalu buat API key sesuai petunjuk di halaman tersebut.
3. Salin key ke file `.env` lokal sesuai bagian 6. Jangan kirim nilainya ke
   agent, grup tim, screenshot atau repository.
4. Periksa model yang tersedia serta kuota dan billing project Anda. Bila
   layanan/model membutuhkan billing, pemilik akun mengatur sendiri sebelum
   memberi izin menjalankan pekerjaan.

Key menghubungkan request API dengan project untuk kuota dan billing.
Ketersediaan model, kuota dan ketentuan biaya mengikuti akun/project Anda;
jangan menganggap seluruh proses pasti gratis. Rujuk
[panduan API key resmi Google](https://ai.google.dev/gemini-api/docs/api-key)
dan [billing Gemini API](https://ai.google.dev/gemini-api/docs/billing).

## 5. Siapkan generator 9Router juga

Dalam alur dokumen 48, **9Router membuat kandidat** dan **Gemini API memvalidasi**.
Memiliki key Gemini saja belum membuat tahap generate dapat berjalan.

Minta kepada pengelola server 9Router, atau siapkan pada server Anda sendiri:

- URL yang dapat diakses dari environment eksekusi, berakhiran `/v1`.
- API key khusus untuk akses server tersebut.
- Nama model generator yang tersedia pada server, termasuk prefix routing
  bila diperlukan.
- Informasi akun/provider yang menanggung kuota dan biaya generation.

Alamat LAN pada `.env.example` hanya contoh. Jika memakai server tim melalui
VPN/jaringan tertentu, koneksi jaringan itu harus aktif pada environment
eksekusi. Key Gemini dan key 9Router mengautentikasi layanan berbeda; isi
masing-masing variabel dengan kredensial layanan yang benar.

Panduan ini belum mengganti generator 9Router dengan Gemini langsung. Jika
belum memiliki akses 9Router, beritahukan kepada tim sebelum meminta agent
generate; agent tetap dapat membantu memeriksa prasyarat yang tersedia.

## 6. Isi `.env` di komputer/environment Anda

Di root proyek, salin template **hanya jika `.env` belum ada**:

```powershell
if (-not (Test-Path -LiteralPath '.env')) {
    Copy-Item -LiteralPath '.env.example' -Destination '.env'
}
```

Buka `.env` menggunakan editor lokal. Ubah baris terkait, jangan menambahkan
baris duplikat. Contoh berikut berisi placeholder yang **harus diganti sendiri**:

```dotenv
LLM_PROVIDER=gemini
EXERCISE_LLM_PROVIDER=gemini
EXERCISE_CHECKPOINT_NAMESPACE=

GEMINI_API_KEY=GANTI_DENGAN_KEY_GEMINI_ANDA
GEMINI_API_KEY_1=
GEMINI_API_KEY_2=
GEMINI_API_KEY_3=
GEMINI_MODEL=GANTI_DENGAN_MODEL_GEMINI_YANG_TERSEDIA
GEMINI_API_BASE_URL=https://generativelanguage.googleapis.com
GEMINI_LIVE_ENABLED=false

NINEROUTER_BASE_URL=https://SERVER_ANDA/v1
NINEROUTER_API_KEY=GANTI_DENGAN_KEY_9ROUTER_ANDA
NINEROUTER_MODEL=GANTI_DENGAN_MODEL_GENERATOR_YANG_TERSEDIA
```

Biarkan konfigurasi lain dari template tetap tersedia. Untuk satu key Gemini,
cukup isi `GEMINI_API_KEY` dan kosongkan slot `_1`, `_2`, `_3`. Slot `_1`
yang terisi dapat mengambil prioritas atas key tanpa suffix. Environment
variable proses juga dapat mengalahkan `.env`; beri tahu agent jika Anda
sebelumnya mengatur konfigurasi provider melalui terminal/secret manager.

`GEMINI_LIVE_ENABLED=false` mempertahankan default layanan tetap nonaktif;
runner validasi pada dokumen 48 menggunakan `--execute` untuk panggilan live
yang secara khusus diminta. Jangan mengaktifkan scheduler atau semua layanan
untuk sekadar menguji koneksi.

Simpan key hanya pada environment pribadi yang digunakan. `.env` sudah masuk
`.gitignore`; jangan memaksa menambahkannya ke Git. Jika proyek didapat sebagai
ZIP, pastikan tidak ikut mengemas `.env` saat membagikan kembali proyek.

## 7. Periksa kesiapan sebelum generate

Setelah dependency terpasang, minta agent menjalankan **preflight saja** dahulu:

```text
Baca API_DOCUMENTATION/49_PERSIAPAN_KONTRIBUTOR.md dan
API_DOCUMENTATION/48_AGENT_GENERATE_VALIDASI_SOAL.md.
Periksa kesiapan kelas1: dependency, sumber materi, konfigurasi Gemini dan
9Router. Jangan tampilkan isi .env atau key dan jangan lakukan panggilan API.
Laporkan SIAP/BELUM SIAP per kebutuhan beserta nama file/variabel yang kurang.
```

Pemeriksaan konfigurasi Gemini tanpa request live juga tersedia melalui:

```powershell
.\.venv\Scripts\python.exe -X utf8 scripts/check_exercise_providers.py --providers gemini
if ($LASTEXITCODE -ne 0) { throw 'Pemeriksaan konfigurasi gagal.' }
```

Tanpa `--execute`, pemeriksaan tersebut tidak membuktikan key asli, izin model,
kuota atau koneksi berhasil. Placeholder yang tidak kosong bisa terbaca sebagai
key tersedia; pastikan Anda sudah menggantinya. Uji koneksi nyata bersifat
opsional dan memakai API; minta secara jelas jika diperlukan, misalnya:

```text
Saya mengizinkan satu uji koneksi Gemini dengan konfigurasi pribadi saya.
Jalankan check_exercise_providers.py --providers gemini --execute.
Laporkan passed/error tanpa mencetak key. Jangan mulai generate atau validasi batch.
```

## 8. Checklist sebelum menyerahkan tugas penuh

- [ ] Repository dan versi/commit tim sudah tersedia pada environment eksekusi.
- [ ] Python 3.12, `.venv` dan dependency siap; agent dapat menjalankan terminal.
- [ ] Excel kurikulum, PDF, index, halaman dan aset sumber tersedia.
- [ ] Artifact diagnostik yang diperlukan sudah diberikan tim.
- [ ] Key Gemini pribadi dan model validator terpasang di `.env`.
- [ ] URL, key dan model 9Router dapat digunakan dari environment tersebut.
- [ ] Pembagian kelas/subbab/batch sudah disepakati dengan tim.
- [ ] Jumlah kandidat, proporsi gambar, N=1/N=3 dan batas request ditentukan.
- [ ] Preflight sumber berstatus ready; hasil cek konfigurasi dipahami.

Jika siap, berikan instruksi generate + validasi pada bagian 1
[dokumen 48](48_AGENT_GENERATE_VALIDASI_SOAL.md). Untuk pilot awal panduan itu
menggunakan 30 kandidat, 12 request generation dan 120 request validation N=3.
Batas request tidak menjamin batas biaya tertentu; tetapkan berdasarkan akun
dan izin Anda. Jika belum siap, sampaikan kebutuhan yang belum tersedia kepada
tim tanpa membagikan nilai key.

Pembagian tanggung jawabnya: **Anda menyiapkan akses akun, rahasia dan izin
penggunaan; tim menyediakan repo, sumber dan pembagian tugas; agent menjalankan
program, memeriksa hasil, menyimpan progres dan membuat laporan.**
