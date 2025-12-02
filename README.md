# 📌 Projek-SPPK — Sistem Pendukung Pemilihan Tempat Makan

Repositori ini berisi implementasi **Sistem Penunjang Pengambilan Keputusan (SPPK)** menggunakan metode **SAW** dengan **TOPSIS** untuk menentukan **tempat makan terbaik di sekitar kampus** berdasarkan delapan kriteria penilaian.

---

## 📖 Deskripsi Proyek

Proyek ini membantu mahasiswa memilih tempat makan terbaik secara objektif dengan pendekatan **Multi-Criteria Decision Making (MCDM)**. Proses utama:

1. **Normalisasi data menggunakan SAW**
2. **Perankingan akhir menggunakan TOPSIS dari hasil normalisasi SAW**

Hasil akhir berupa satu skor dan satu ranking gabungan untuk setiap tempat makan.

---

## 🎯 Kriteria Penilaian

Sistem menggunakan 8 kriteria benefit:

| Kode | Kriteria                  | Skala |
| ---- | ------------------------- | ----- |
| C1   | Harga                     | 1–5   |
| C2   | Kualitas Rasa             | 1–5   |
| C3   | Jarak                     | 1–5   |
| C4   | Kebersihan & Kenyamanan   | 1–5   |
| C5   | Kecepatan Pelayanan       | 1–5   |
| C6   | Variasi Menu              | 1–5   |
| C7   | Ketersediaan Tempat Duduk | 1–5   |
| C8   | Fasilitas                 | 1–5   |

**Bobot kriteria:**

- C2: 0.25
- C1: 0.20
- C3: 0.15
- C4: 0.10
- C5: 0.10
- C6: 0.08
- C7: 0.06
- C8: 0.06

---

## ⭐ Fitur

- Normalisasi otomatis dengan SAW
- Perankingan akhir dengan TOPSIS
- Satu skor dan ranking gabungan untuk setiap tempat makan
- Dataset hasil survei mahasiswa
- User Interface modern dan interaktif
- Struktur proyek rapi dan mudah dikembangkan

---

## 🛠 Instalasi

Clone repositori:

```bash
git clone https://github.com/ariskiarr/Projek-SPPK-.git
cd Projek-SPPK-
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Cara Menjalankan

1. Jalankan aplikasi:

```bash
python appsppk.py
```

2. Buka browser dan akses: [http://localhost:5000](http://localhost:5000)
3. Upload file CSV sesuai format kriteria di atas
4. Lihat hasil ranking tempat makan

---

## 📂 Struktur Folder

- `appsppk.py` — Main app
- `templates/` — HTML templates
- `static/` — CSS dan aset statis
- `program/` — (opsional) kode tambahan

---

## 📄 Lisensi

Proyek ini open source dan bebas digunakan untuk edukasi.
