"""
Pipeline ekstraksi soal pretest BERBASIS AI AGENT (pengganti regex + Ollama).

Pembagian kerja:
  - Kode Python di paket ini  -> pekerjaan MEKANIS & DETERMINISTIK:
      convert.py  : PDF -> Markdown per halaman + indeks + render PNG halaman
      validate.py : cek hasil kerja agen (schema, verbatim, opsi, kunci)
      export.py   : gabung per-bab -> format model `Pertanyaan` (acak opsi)
      progress.py : memori progres lintas sesi (PROGRESS.md)
  - AI Agent (Claude Code, lihat .claude/skills/ekstrak-soal-pretest) ->
    pekerjaan yang butuh PEMAHAMAN: membaca halaman, menentukan batas soal &
    stimulusnya, membaca notasi matematika dari gambar halaman, mencari &
    mencocokkan kunci di Buku Guru, membuat 3 distraktor.

Agen tidak pernah dipercaya begitu saja: setiap file hasil kerjanya wajib
lolos `validate.py` sebelum dianggap selesai.
"""
