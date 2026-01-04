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

Contoh Kode Thresholding (PDF Dosen):  
_, otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

---

## Edge-Based Segmentation
Edge-based segmentation mendeteksi batas objek berdasarkan perubahan intensitas yang tajam (tepi). Proses ini terdiri dari tahapan deteksi tepi, koneksi tepi, dan segmentasi region.

### Gradient dan Sobel Operator
Deteksi tepi didasarkan pada konsep gradient, yaitu turunan intensitas terhadap arah horizontal dan vertikal. Operator Sobel digunakan untuk menghitung komponen gradient pada citra.

Contoh Kode Sobel (PDF Dosen):  
gx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  
gy = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  
magnitude = np.sqrt(gx**2 + gy**2)

### Canny Edge Detector
Canny Edge Detector merupakan algoritma deteksi tepi multi-tahap yang mencakup noise reduction, perhitungan gradient, non-maximum suppression, dan hysteresis thresholding.

Contoh Implementasi:  
edges = cv2.Canny(gray, 100, 200)

---

## Region-Based Segmentation
Region-based segmentation mengelompokkan piksel menjadi region berdasarkan kemiripan properti seperti intensitas dan tekstur sehingga membentuk area objek yang lebih utuh.

### Region Growing
Region growing dimulai dari seed point dan memperluas region berdasarkan kemiripan intensitas antar piksel yang berdekatan.

### Watershed Algorithm
Watershed Algorithm memandang citra sebagai permukaan topografi dan menggunakan marker untuk memisahkan objek yang saling berdekatan.

Contoh Implementasi:  
markers = cv2.watershed(image, markers)  
image[markers == -1] = [255, 0, 0]

---

## Implementasi Program
Program diimplementasikan menggunakan bahasa **Python** dengan library **OpenCV**, **NumPy**, dan **Matplotlib**. Program memproses satu citra dan menerapkan thresholding, edge-based segmentation (Canny), serta region-based segmentation (Watershed).

---

## Analisis Hasil Praktikum
Thresholding efektif pada citra dengan perbedaan intensitas yang jelas, namun kurang optimal pada pencahayaan tidak merata. Edge-based segmentation mampu mendeteksi batas objek dengan jelas, tetapi tidak membentuk area objek secara utuh. Region-based segmentation menggunakan watershed memberikan hasil segmentasi area objek yang paling lengkap, meskipun sensitif terhadap preprocessing.

---

## Analisis Pemilihan Parameter
Pemilihan parameter threshold pada Canny dan tahap preprocessing pada watershed sangat berpengaruh terhadap hasil segmentasi. Rasio threshold rendah dan tinggi pada Canny mengikuti rekomendasi 2:1 atau 3:1. Pada watershed, pemilihan marker yang tepat diperlukan untuk menghindari over-segmentation.

---

## Diskusi Hasil dan Keterbatasan
Setiap metode segmentasi memiliki keterbatasan. Thresholding sensitif terhadap pencahayaan, edge-based segmentation tidak membentuk area objek, dan region-based segmentation memiliki kompleksitas tinggi serta sangat bergantung pada tahap preprocessing.

---

## Studi Kasus dan Skenario Penggunaan
Thresholding cocok digunakan pada citra sederhana dengan histogram bimodal. Edge-based segmentation sesuai untuk citra dengan batas objek yang jelas. Region-based segmentation lebih tepat digunakan pada citra kompleks dengan objek saling berdekatan, seperti citra medis.

---

## Kesimpulan dan Rekomendasi
Segmentasi citra lanjutan memberikan hasil yang lebih fleksibel dibandingkan segmentasi dasar. Thresholding efektif sebagai tahap awal, edge-based segmentation berguna untuk deteksi batas, dan region-based segmentation menghasilkan area objek yang lebih homogen. Pemilihan metode segmentasi sebaiknya disesuaikan dengan karakteristik citra dan tujuan analisis.

---

## Referensi
Materi PDF Pengolahan Citra Digital Pertemuan 7  
Dr. Arya Adhyaksa Waskita, S.Si., M.Si.  
Materi PPT Presentasi Kelompok
