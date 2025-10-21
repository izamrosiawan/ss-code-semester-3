
# Deskripsi Kasus untuk Masalah Regresi

**Tujuan**:  
Tujuan dari analisis ini adalah untuk **memprediksi pendapatan penjualan es krim (`Revenue`)** berdasarkan **suhu udara harian (`Temperature`)** menggunakan metode *Simple Linear Regression*.  
Dugaan awalnya adalah bahwa semakin tinggi suhu udara, semakin tinggi pula penjualan es krim karena meningkatnya minat konsumen pada cuaca panas.

---

## Ringkasan Dataset

- **Variabel Target (Dependent Variable)**: Pendapatan penjualan es krim (`Revenue`)
- **Fitur Prediktor (Independent Variable)**: Suhu udara harian (`Temperature`)

Dataset ini memiliki total **500 observasi** dengan dua variabel numerik yang relevan:
- `Temperature`: Suhu udara harian dalam derajat Celsius.
- `Revenue`: Pendapatan harian penjualan es krim dalam ribuan satuan mata uang.

Dataset ini bersifat sederhana namun ideal untuk membangun model regresi linier karena adanya hubungan kontinu antara fitur prediktor dan variabel target.

---

## Tahapan Analisis Berdasarkan Siklus Hidup Data Science

Proses analisis data ini mengikuti tahapan dalam **Data Science Life Cycle**, yang meliputi beberapa langkah berikut:

### 1. Pemahaman Masalah (Problem Understanding)
   - **Pertanyaan Kunci**:
     - Bagaimana suhu udara memengaruhi pendapatan penjualan es krim harian?
     - Bisakah kita memprediksi pendapatan penjualan es krim jika suhu tertentu diketahui?
   - **Metrik Utama**:
     - Metrik yang digunakan untuk mengevaluasi model adalah $R^2$, *Mean Squared Error* (MSE), dan *Root Mean Squared Error* (RMSE).

### 2. Pengumpulan Data (Data Collection)
   - Dataset ini telah disediakan dalam file CSV: **`IceCreamData.csv`**, dengan dua kolom utama:
     - `Temperature (°C)`
     - `Revenue (ribu satuan mata uang)`

### 3. Eksplorasi Data (Data Exploration)
   - Memeriksa distribusi variabel (`Temperature` dan `Revenue`).
   - Menghitung statistik deskriptif seperti *mean*, *median*, dan *standard deviation* untuk memahami karakteristik data.
   - Visualisasi hubungan antara `Temperature` dan `Revenue` menggunakan *scatter plot* untuk melihat pola hubungan linear.

### 4. Persiapan Data (Data Preparation)
   - Memeriksa apakah terdapat data hilang (*missing values*) atau outlier.
   - Melakukan normalisasi atau standarisasi jika diperlukan.
   - Membagi data menjadi `training set` dan `test set` (80% : 20%) untuk melatih dan menguji model.

### 5. Pemodelan (Modeling)
   - Membangun model *Simple Linear Regression* dengan:
     - `Temperature` sebagai variabel independen (X)
     - `Revenue` sebagai variabel dependen (y)
   - Melatih model menggunakan `training set`.
   - Melakukan prediksi terhadap `test set`.

### 6. Evaluasi Model (Model Evaluation)
   - Mengukur performa model dengan metrik:
     - $R^2$ untuk melihat seberapa baik model menjelaskan variasi target.
     - *Mean Squared Error* (MSE) untuk menilai rata-rata kesalahan kuadrat.
     - *Root Mean Squared Error* (RMSE) untuk menilai rata-rata kesalahan dalam satuan aslinya.
   - Menampilkan nilai *intercept* dan *koefisien regresi* untuk melihat arah dan besar pengaruh suhu terhadap pendapatan.
   - Membuat visualisasi garis regresi pada *scatter plot* data aktual.

---

## Output yang Diharapkan
- Model regresi linear sederhana yang mampu memprediksi pendapatan (`Revenue`) berdasarkan suhu (`Temperature`).
- Nilai evaluasi model: $R^2$, MSE, dan RMSE.
- Hasil *intercept* dan *koefisien regresi* sebagai bentuk hubungan antara suhu dan pendapatan.
- Visualisasi hubungan linear antara data aktual dan hasil prediksi.
- Interpretasi hasil dan kesimpulan terhadap performa model.

---

## Pertanyaan
1. Apa arti nilai intercept (b₀) dari model regresi linear yang kamu dapatkan?
2. Apa arti nilai koefisien/slope (b₁) pada model regresi?
3. Apakah hubungan antara Temperature dan Revenue bersifat positif atau negatif?
4. Berapa nilai $R^2$ yang kamu peroleh, dan apa artinya?
5. Apa makna dari nilai MSE dan RMSE?
