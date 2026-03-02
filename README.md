# Eksperimen Sistem Machine Learning - Rizki Dwi Febriansyah

Repository ini dibuat untuk memenuhi kriteria **Eksperimen Sistem Machine Learning (MSML)** pada proses pengembangan pipeline Machine Learning.

---

## 📊 Dataset

Dataset yang digunakan pada proyek ini adalah **Student Performance Dataset** yang berisi informasi mengenai kebiasaan belajar siswa dan pengaruhnya terhadap performa akademik.

Dataset terdiri dari beberapa fitur utama, antara lain:

* Hours Studied
* Previous Scores
* Extracurricular Activities
* Sleep Hours
* Sample Question Papers Practiced
* Performance Index

Dataset mentah disimpan pada folder:

```
Student_Performance_raw/
```

---

## 🔎 Eksperimen Dataset

Tahap eksperimen dilakukan menggunakan notebook:

```
preprocessing/Eksperimen_Rizki-Dwi-Febriansyah.ipynb
```

Pada tahap ini dilakukan beberapa proses eksplorasi data, yaitu:

* Data Loading
* Exploratory Data Analysis (EDA)
* Pengecekan missing value
* Analisis distribusi data
* Encoding data kategorikal
* Feature Engineering
* Standardisasi fitur numerik

Eksperimen ini menjadi dasar dalam pembuatan proses preprocessing otomatis.

---

## ⚙️ Data Preprocessing

Proses preprocessing otomatis dibuat pada file:

```
preprocessing/automate_Rizki-Dwi-Febriansyah.py
```

Tahapan preprocessing meliputi:

1. Menghapus data duplikat dan nilai kosong
2. Encoding fitur kategorikal
3. Pembuatan fitur baru (`study_efficiency`)
4. Standardisasi data numerik menggunakan **StandardScaler**
5. Penyimpanan dataset hasil preprocessing

Dataset hasil preprocessing disimpan pada:

```
preprocessing/Student_Performance_preprocessing/
```

---

## 🤖 Otomatisasi Menggunakan GitHub Actions

Repository ini menerapkan **GitHub Actions Workflow** untuk melakukan preprocessing dataset secara otomatis.

Workflow akan berjalan ketika:

* Terjadi perubahan (push) pada branch `main`
* Workflow dijalankan secara manual

File workflow berada pada:

```
.github/workflows/preprocessing.yml
```

Proses otomatis meliputi:

* Setup environment Python
* Instalasi dependency
* Menjalankan script preprocessing
* Menghasilkan dataset terbaru secara otomatis

---

## 📁 Struktur Repository

```
Eksperimen_SML_Rizki-Dwi-Febriansyah
│
├── .github/workflows/
│   └── preprocessing.yml
│
├── Student_Performance_raw/
│   └── Student_Performance.csv
│
└── preprocessing/
    ├── Eksperimen_Rizki-Dwi-Febriansyah.ipynb
    ├── automate_Rizki-Dwi-Febriansyah.py
    └── Student_Performance_preprocessing/
        └── student_performance_processed.csv
```

---

## ✅ Kesimpulan

Melalui repository ini, proses eksperimen hingga preprocessing dataset telah berhasil diotomatisasi sehingga data selalu berada dalam kondisi siap digunakan untuk tahap pelatihan model Machine Learning selanjutnya.
