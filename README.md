# 📌 Projek-SPPK — Sistem Pendukung Pemilihan Tempat Makan

Repositori ini berisi implementasi **Sistem Penunjang Pengambilan Keputusan (SPPK)** menggunakan metode **SAW** dan **TOPSIS** untuk menentukan **tempat makan terbaik di sekitar kampus** berdasarkan delapan kriteria penilaian.

---

## 📖 Deskripsi Proyek

Proyek ini dikembangkan untuk membantu mahasiswa menentukan tempat makan terbaik secara objektif dengan pendekatan **Multi-Criteria Decision Making (MCDM)**. Dua metode yang digunakan:

- **Simple Additive Weighting (SAW)**
- **Technique for Order Preference by Similarity to Ideal Solution (TOPSIS)**

Kedua metode menghasilkan ranking alternatif sehingga pengguna dapat melihat perbandingan hasil yang jelas dan objektif.

---

## 🎯 Kriteria Penilaian

Sistem menggunakan 8 kriteria benefit:

| Kode | Kriteria | Skala |
|------|----------|--------|
| C1 | Harga | 1–5 |
| C2 | Kualitas Rasa | 1–5 |
| C3 | Jarak | 1–5 |
| C4 | Kebersihan & Kenyamanan | 1–5 |
| C5 | Kecepatan Pelayanan | 1–5 |
| C6 | Variasi Menu | 1–5 |
| C7 | Ketersediaan Tempat Duduk | 1–5 |
| C8 | Fasilitas | 1–5 |

**Bobot kriteria:**

C2: 0.25
C1: 0.20
C3: 0.15
C4: 0.10
C5: 0.10
C6: 0.08
C7: 0.06
C8: 0.06


---

## ⭐ Fitur

- Implementasi penuh metode **SAW** dan **TOPSIS**
- Dataset hasil survei mahasiswa
- Perhitungan otomatis nilai normalisasi, pembobotan, dan ranking
- Perbandingan hasil SAW vs TOPSIS
- User Interface yang mudah dan interaktif 
- analisis untuk eksplorasi data
- Struktur proyek rapi dan mudah dikembangkan

---

## 🛠 Instalasi

Clone repositori:

```bash
git clone https://github.com/ariskiarr/Projek-SPPK-.git
cd Projek-SPPK-
