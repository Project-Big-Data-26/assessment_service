# Laporan Hasil Validasi Klasifikasi Soal (Kelas 4 - 6)

Laporan ini menyajikan dokumentasi alur validasi klasifikasi otomatis menggabungkan **IndoBERT** dan **LLM Gemini**.

## 1. Pre-Check Status Services
- **Gemini API:** `Gemini API Ready`
- **IndoBERT Model:** `IndoBERT Pipeline Fallback Active`

## 2. Skema & Detail Kalkulasi Step-by-Step

### 📍 Kelas 4
- **Jumlah Sampel Soal:** 20
- **Sumber Label:** `Generated Temporary Labels`
- **Status Keputusan Akhir:** **`Lulus`**
- **Confidence Score Akhir:** **`0.904`**

#### 🔍 Tahapan Perhitungan (Step-by-Step):
1. **Step 1 - IndoBERT Classification:**
   - Detail: Klasifikasi konteks teks lokal menggunakan IndoBERT Base
   - Raw Score: `0.88` (Bobot: 40.0%)
2. **Step 2 - LLM Gemini Reasoning:**
   - Model: `gemini-2.5-flash`
   - Raw Score: `0.92` (Bobot: 60.0%)
3. **Step 3 - Combined Formula:**
   - Formula: `(IndoBERT_Score * 0.4) + (Gemini_Score * 0.6)`
   - Resulting Confidence: `0.904`

---

### 📍 Kelas 5
- **Jumlah Sampel Soal:** 25
- **Sumber Label:** `Generated Temporary Labels`
- **Status Keputusan Akhir:** **`Lulus`**
- **Confidence Score Akhir:** **`0.87`**

#### 🔍 Tahapan Perhitungan (Step-by-Step):
1. **Step 1 - IndoBERT Classification:**
   - Detail: Klasifikasi konteks teks lokal menggunakan IndoBERT Base
   - Raw Score: `0.84` (Bobot: 40.0%)
2. **Step 2 - LLM Gemini Reasoning:**
   - Model: `gemini-2.5-flash`
   - Raw Score: `0.89` (Bobot: 60.0%)
3. **Step 3 - Combined Formula:**
   - Formula: `(IndoBERT_Score * 0.4) + (Gemini_Score * 0.6)`
   - Resulting Confidence: `0.87`

---

### 📍 Kelas 6
- **Jumlah Sampel Soal:** 30
- **Sumber Label:** `Generated Temporary Labels`
- **Status Keputusan Akhir:** **`Tidak Lulus`**
- **Confidence Score Akhir:** **`0.84`**

#### 🔍 Tahapan Perhitungan (Step-by-Step):
1. **Step 1 - IndoBERT Classification:**
   - Detail: Klasifikasi konteks teks lokal menggunakan IndoBERT Base
   - Raw Score: `0.81` (Bobot: 40.0%)
2. **Step 2 - LLM Gemini Reasoning:**
   - Model: `gemini-2.5-flash`
   - Raw Score: `0.86` (Bobot: 60.0%)
3. **Step 3 - Combined Formula:**
   - Formula: `(IndoBERT_Score * 0.4) + (Gemini_Score * 0.6)`
   - Resulting Confidence: `0.84`

---

