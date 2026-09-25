Project Overview!!

1. Requirements System:

Sebelum mulai pastikan sudah terinstall:
* Python 3.9+ 
* Git

2. Cara setup:

* Clone repo
    git clone https://github.com/Project-Big-Data-26/assessment_service.git
* Masuk virtual environment
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
* Install package
    pip install -r requirements.txt

3. Project Architecture:

    app/
    ├── api/
    │   └── routes/          # (Endpoint untuk Backend)
    ├── ingestion/
    │   └── sibi_loader.py   # Script ekstraktor data dari buku SIBI
    ├── schemas/
    │   ├── request.py       # Pydantic models untuk validasi data masuk
    │   └── response.py      # Pydantic models untuk format output API
    ├── services/
    │   └── extractor.py      # Logika untuk mengambil data dari database hasil ekstraksi SIBI
    └── main.py
