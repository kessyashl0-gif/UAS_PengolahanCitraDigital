# UAS Pengolahan Citra Digital  
## Segmentasi Lanjut: Edge-Based dan Region-Based

---

## Informasi Umum
Repository ini dibuat untuk memenuhi **Tugas Kelompok Ujian Akhir Semester (UAS)**  
pada mata kuliah **Pengolahan Citra Digital**.

Materi UAS yang dibahas adalah **Segmentasi Lanjut**, sesuai dengan materi
perkuliahan **Pertemuan 7**, yang meliputi:
- Review Thresholding
- Edge-Based Segmentation
- Region-Based Segmentation
- Aplikasi praktis dan perbandingan metode

Seluruh pembahasan teori dan implementasi program disusun berdasarkan  
**materi PDF dosen** dan **PPT presentasi kelompok**.

---

## Identitas Kelompok

| No | Nama | NIM |
|----|-----------------------------|--------------|
| 1 | Kessya Shalsabilla Fahlevi | 231011400427 |
| 2 | Nurul Stefhani | 231011402225 |
| 3 | Aldi Januari | 231011400440 |
| 4 | M. Daffa Maulana | 231011400420 |
| 5 | Rusman Sampulawa | 231011403260 |

Program Studi : Teknik Informatika  
Universitas : Universitas Pamulang  
Mata Kuliah : Pengolahan Citra Digital  
Dosen Pengampu : Dr. Arya Adhyaksa Waskita, S.Si., M.Si.

---

## Pendahuluan
Segmentasi citra merupakan salah satu tahapan penting dalam pengolahan citra digital yang bertujuan untuk membagi citra menjadi beberapa bagian atau region berdasarkan karakteristik tertentu, seperti intensitas, warna, dan tekstur. Hasil segmentasi yang baik sangat berpengaruh terhadap proses lanjutan seperti ekstraksi fitur, analisis bentuk, dan pengenalan objek.

Metode segmentasi dasar seperti thresholding sering digunakan karena implementasinya sederhana dan cepat. Namun, metode ini memiliki keterbatasan pada citra dengan pencahayaan tidak merata dan kontras rendah. Oleh karena itu, diperlukan metode segmentasi lanjutan seperti edge-based segmentation dan region-based segmentation untuk memperoleh hasil yang lebih akurat.

---

## Tujuan
Tujuan dari pelaksanaan proyek kelompok UAS ini adalah:
1. Memahami konsep segmentasi citra lanjutan  
2. Menerapkan thresholding sebagai tahap awal segmentasi  
3. Menerapkan metode edge-based segmentation untuk mendeteksi batas objek  
4. Menerapkan metode region-based segmentation untuk membentuk area objek yang homogen  
5. Membandingkan karakteristik dan hasil dari masing-masing metode segmentasi  

---

## Konsep Dasar Segmentasi
Segmentasi citra bertujuan untuk memisahkan objek utama dari latar belakang atau objek lain di dalam citra. Segmentasi dilakukan dengan memanfaatkan perbedaan karakteristik piksel dan hubungan spasial antar piksel.

Pendekatan segmentasi yang digunakan dalam proyek ini meliputi:
- Thresholding (berdasarkan intensitas)
- Edge-Based Segmentation (berdasarkan tepi)
- Region-Based Segmentation (berdasarkan kemiripan region)

Setiap pendekatan memiliki kelebihan dan keterbatasan yang berbeda.

---

## Review Thresholding
Thresholding merupakan metode segmentasi dasar yang memisahkan objek dan latar belakang berdasarkan nilai intensitas piksel. Pada materi UAS dibahas tiga jenis thresholding, yaitu:
- Global Thresholding
- Otsu’s Method
- Adaptive Thresholding

Pada implementasi praktikum digunakan **Otsu’s Method**, karena mampu menentukan nilai threshold optimal secara otomatis berdasarkan variansi histogram citra.

### Contoh Kode Thresholding (PDF Dosen)
```python
_, otsu = cv2.threshold(image, 0, 255,
                        cv2.THRESH_BINARY + cv2.THRESH_OTSU)
