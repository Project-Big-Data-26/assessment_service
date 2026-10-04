# Kategori operasional relatif

Array ini membagi soal aktif menjadi tiga kelompok berdasarkan profil bukti dan kuota.
Hard berarti sepertiga dengan ranking tertinggi dalam bank kelas ini; bukan validasi baru bahwa soal itu Hard.
Skor heuristik dan batas kategori yang memotong skor sama dicatat di balance_audit.json.
confidence_score dihitung dari dukungan run AI asli terhadap label operasional, sehingga dapat 0.
Hasil validasi aktif, bukti Gemini dan data training asli tetap tersedia di hasil_validasi.
IRT empiris tidak dihitung. Ekspor ini tidak otomatis dipakai untuk training atau delivery.
