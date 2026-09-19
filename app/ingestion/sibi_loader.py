import pdfplumber
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

FILE_PATH = BASE_DIR / "data" / "sd" / "kelas6" / "panduan_siswa_kls_6.pdf" # <-- UBAH NAMA FILE INI

def test_read_pdf():
    print(f"Mencari file di: {FILE_PATH}")
    
    if not FILE_PATH.exists():
        print("File tidak ditemukan! Pastikan nama file dan path sudah benar.")
        return

    print("File ditemukan. Mulai membaca PDF...\n")
    
    try:
        with pdfplumber.open(FILE_PATH) as pdf:
            total_pages = len(pdf.pages)
            print(f"Total Halaman dalam buku: {total_pages}\n")
            
            start_page = 39 
            end_page = 42   
            
            for i in range(start_page, end_page):
                if i >= total_pages:
                    break
                    
                page = pdf.pages[i]
                teks_mentah = page.extract_text()
                
                print(f"{"="*20} TEKS HALAMAN {i+1} {"="*20}")
                if teks_mentah:
                    print(teks_mentah)
                else:
                    print("[Halaman ini kosong atau berisi gambar penuh yang tidak terbaca]")
                print("="*60 + "\n")
                
    except Exception as e:
        print(f"Terjadi error saat membaca PDF: {e}")

if __name__ == "__main__":
    test_read_pdf()