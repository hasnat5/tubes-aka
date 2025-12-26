# 🧮 KAJIAN EFISIENSI PROSES AKUMULASI BILANGAN ASLI BERURUTAN MENGGUNAKAN PENDEKATAN ITERATIF DAN REKURSIF

Penjumlahan bilangan asli berurutan merupakan operasi matematika fundamental yang sering dijumpai dalam berbagai aplikasi komputasi. Permasalahan ini melibatkan perhitungan total penjumlahan dari 1 hingga n, yang dapat dinyatakan sebagai: 1 + 2 + 3 + ... + n.

## The Problem

Permasalahan yang diangkat dalam tugas besar ini adalah perhitungan penjumlahan bilangan asli dari 1 hingga n. Permasalahan ini dipilih untuk dianalisis karena dapat diselesaikan menggunakan lebih dari satu pendekatan algoritmik, khususnya pendekatan iteratif dan rekursif.

Studi kasus ini dipilih dengan pertimbangan sebagai berikut:

- Memiliki representasi yang dapat diimplementasikan secara iteratif menggunakan struktur perulangan.
- Memiliki representasi yang dapat diimplementasikan secara rekursif menggunakan pemanggilan fungsi.
- Menunjukkan perbedaan karakteristik kinerja antara pendekatan iteratif dan rekursif seiring dengan bertambahnya ukuran input n.
- Memungkinkan dilakukan pengukuran empiris waktu eksekusi yang jelas berdasarkan variasi ukuran masukan.

Melalui studi kasus ini, analisis kompleksitas algoritma diverifikasi melalui pengujian empiris, sehingga dapat menunjukkan pentingnya pemilihan algoritma yang efisien dalam penyelesaian suatu permasalahan komputasi.

---

## 👥 Anggota Tim IF-48-05

| Nama                 | NIM          |
| -------------------- | ------------ |
| ANNISA ROSLINA ANWAR | 103012430064 |
| HASNAT FERDIANANDA   | 103012430038 |
| RASYID RIDLO         | 103012400042 |

---

## 🎯 Studi Kasus

**💼 Penyelesaian Sprint dalam Manajemen Proyek**

Dalam manajemen proyek software, sering ditemukan pola di mana kompleksitas fitur yang diselesaikan bertambah seiring dengan sprint yang berjalan:

- Sprint 1: 1 fitur selesai
- Sprint 2: 2 fitur selesai
- Sprint 3: 3 fitur selesai
- ...
- Sprint n: n fitur selesai

**Total fitur setelah n sprint = 1 + 2 + 3 + ... + n**

**Contoh**: Setelah 12 sprint = 78 fitur delivered

Permasalahan ini dapat diselesaikan dengan tiga pendekatan:

1. **Iteratif**: Loop untuk menjumlahkan setiap bilangan
2. **Rekursif**: Fungsi yang memanggil dirinya sendiri

---

## ✨ Fitur Aplikasi

### 1. **Input Nilai n Interaktif**

- Input nilai n dengan number input
- Range: 1 hingga 5000
- Nilai default: 500
- Warning otomatis untuk nilai n > 5000 (risiko stack overflow)

### 2. **Perbandingan Algoritma**

- ✅ **Algoritma Iteratif**: Menggunakan loop untuk menjumlahkan 1 hingga n
  - Kompleksitas Waktu: O(n)
- 🔁 **Algoritma Rekursif**: Menggunakan fungsi rekursif
  - Kompleksitas Waktu: O(n)

### 3. **Analisis Waktu Eksekusi**

- Mengukur waktu rata-rata dari 3 percobaan (`measure_time`)
- Menampilkan hasil dalam milidetik (ms)
- Visualisasi grafik bar perbandingan waktu eksekusi

### 4. **Grafik Perbandingan untuk Berbagai Nilai n**

Opsi untuk menampilkan grafik runtime dari n = 1 hingga n = 500:

- Menghitung waktu eksekusi untuk setiap nilai n secara individual
- Menampilkan trend performa kedua algoritma
- Visualisasi perbedaan overhead antara iteratif dan rekursif
- Grid dan legend untuk kemudahan pembacaan

---

## 🛠️ Teknologi yang Digunakan

- **Python 3.x**
- **Streamlit** - Framework untuk web app interaktif
- **Matplotlib** - Library visualisasi data
- **time** - Modul untuk pengukuran waktu eksekusi

---

## 📦 Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/hasnat5/tubes-aka.git
cd tubes-aka
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Isi File `requirements.txt`

```txt
streamlit
numpy
matplotlib
```

---

## 🚀 Cara Menjalankan

### Jalankan Aplikasi Streamlit

```bash
streamlit run bilangan_ali.py
```

Aplikasi akan terbuka di browser pada alamat:

```
http://localhost:8501
```

---

## 📂 Struktur Proyek

```
tubes_aka/
│
├── bilangan_asli.py   # Aplikasi utama Streamlit
├── requirements.txt    # Dependencies Python
├── README.md           # Dokumentasi proyek
└── bilangan_asli.js       # (Opsional) Implementasi JavaScript
```

---

## 🔗 Referensi

1. **Streamlit Documentation** - [docs.streamlit.io](https://docs.streamlit.io)
2. **NumPy Documentation** - [numpy.org](https://numpy.org/doc/)
3. **Big O Notation** - Analisis Kompleksitas Algoritma

---

## 📝 Lisensi

Proyek ini dibuat untuk keperluan tugas akademik **Analisis Kompleksitas Algoritma** di Telkom University.

---

## 🙏 Kontribusi

Dibuat dengan ❤️ oleh **Tim IF-48-05**

Jika ada pertanyaan atau saran, silakan hubungi anggota tim melalui email institusi.
