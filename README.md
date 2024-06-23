# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000.

## Permasalahan Bisnis
Hingga saat ini Jaya Jaya Institute telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Cakupan Proyek
Cakupan proyek yang dilakukan adalah sebagai berikut :
1. Persiapan
   - Menyiapkan library yang akan digunakan pada proses analisis
   - Menyiapkan daya yang akan digunakan
2. Data Understanding
   - Melakukan pengecheckan data yang kosong (missing value)
   - Melakukan pengecheckan tipe data
   - Eksplorasi Data
3. Data Preprocessing
   - Train test split : membagi data latih dan data uji yang akan digunakan degnan rasio 90% data train dan 10% data test
   - Undersampling sample : menangani imbalance data dengan mengurangi jumlah data pada kelas mayoritas secara acak
   - Split X dan Y : menentukan feature yang akan digunakan untuk train data sebagai X dan Y sebagai target (status)
   - Standarizing & Label Encoder : melakukan encoding pada data categorical dan scaling pada data numerik
   - PCA : reduksi pada feature yang tidak berkolerasi linear
4. Modeling & Evaluation
   - Modeling : algoritma yang digunakan pada tahap modeling adalah Decision Tree dan Random Forest
   - Evaluation : akurasi pada model Decision Tree adalah sebesar 69% dan Random Forest sebesar 85% dengan menggunakan evaluasi confussion matrix.

### Persiapan

Sumber Data : https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv

Setup Environment :
#### Library Installation
1. Pastikan python sudah terinstall dengan mengetik kode berikut pada Command Prompt
   ```
   python --version
   ```
2. Passtikan pip sudah terinstall dengan mengetik kode berikut pada Command Prompt
   ```
   pip --version
   ```
3. Install library yang digunakan pada proyek ini dengan mengetik kode berikut
   ```
   pip install requirements.txt
   ```
#### Running Streamlit
Untuk menjalankan prototype applikasi dapat mengetikkan kode berikut pada terminal
```
streamlit run prediction_app.py
```
## Business Dashboard
<div align="center">
   
![image](https://github.com/astriwidyastiti/Prediction/assets/112534966/bd587e9a-8dac-4886-af7a-0c02e561ce89)

</div>

Untuk mengakses dashboard di atas dapat melalui link berikut :
https://lookerstudio.google.com/reporting/8915d4aa-44f5-42b6-b052-e859dcdea030

Terdapat beberapa insight yang didapatkan berdasarkan dashboard yang dibuat, antara lain :
1. Jumlah siswa yang dinyatakan dropout sebanyak 1.421 orang
2. Nilai rata-rata siswa yang dinyatakan dropout adalah sebesar 124,96
3. Sebanyak 50,7% siswa yang dinyatakan dropout adalah perempuan
4. Nilai rata-rata GDP siswa yang dinyatakan dropout adalah -0.2, hal ini dapat menjadi asumsi jika siswa yang dinyatakan dropout memiliki nilai GDP yang kecil.
5. Siswa yang dinyatakan dropout paling banyak pada usia 18-19 tahun
6. Siswa yang melakukan metode aplikasi dengan kategori diatas 23 tahun paling banyak dinyatakan dropout
7. Terdapat korelasi antara addmision grade dan previous qualification grade dengan jumlah kurikulum yang diambil oleh siswa pada semester 1 dan 2

## Menjalankan Sistem Machine Learning

Sistem Prediksi dapat dijalankan dengan memasukkan data-data pengguna yang diperlukan untuk mendeteksi seseorang yang mungkin akan melakukan dropout. Data-data yang akan diinputkan terdiri dari 4 sesi:
1. Personal Information terdiri dari field : Gender, Marital Status, Nacionality, Father Occupation, Father Qualification, Mother Occupation, Mother Qualification
2. Application Informatio terdiri dari field : DayTime Evening Attendance, Previous Qualification, International Student, Application Mode, Course, Admission Grade, Previous Qualification Grade, Displaced, Education Special Needs
3. Financial Information terdiri dari field : Debtor, Scholarship Holder, Tuition Fees Up To Date
4. Student Progress terdiri dari field : Curricular Units 1st Sem & 2nd Sem Enrolled, Curricular Units 1st & 2nd Sem Evaluations, Curricular Units 1st Sem & 2nd Approved, Curricular Units 1st & 2nd Sem Grade, Applciation Order, Age at Enrollment, Unemployment Rate, Inflation Rate, GDP

Setelah memasukkan data, maka data yang diinputkan dapat dilihat dengan melakukan klik pada button View Data Raw. Untuk melakukan prediksi, pengguna dapat menekan button prediksi yang akan menghasilkan status :

1. Graduate : Status lulus
2. Enrolled : Status masih aktif menjalani akademik
3. Dropout : Status yang keluar dari kegiatan akademik

Prediksi pada sistem machine learning menggunakan metode Random Forest. Sistem prediksi dapat diakses melalui link : https://prediction-status.streamlit.app/

<div>
   
![image](https://github.com/astriwidyastiti/Prediction/assets/112534966/6e6bd60e-eb3e-4ff9-86ac-92d5f2af9f88)
 
</div>

## Conclusion
Setelah melakukan analisis dengan menggunakan model machine learning, dapat diambil beberapa faktor yang mempengaruhi seorang siswa melakukan dropout, antara lain :
1. Finansial : siswa yang dinyatakan dropout kebanyakan merupakan siswa yang telat melakukan pembayaran biaya.
2. Pekerjaan Orang Tua : Siswa yang melakukan dropout dipengaruhi oleh faktor pekerjaan orang tua baik ayah maupun ibu. Siswa yang melakukan dropout adalah siswa yang orang tua nya memiliki pekerjaan sebagai pekerja tidak terampil
3. Pemegang Beasiswa : siswa yang tidak memegang beasiswa lebih banyak melakukan dropout
4. Course : program studi dengan jumlah siswa terbanyak lebih banyak mengalami dropout

Feature numerik yang digunakan untuk membangun model machine learning prediksi adalah sebagai berikut :

1. Curricular_units_1st_sem_enrolled : Jumlah mata kuliah yang diambil siswa pada semester 1
2. Curricular_units_1st_sem_evaluations : Jumlah mata kuliah siswa yang dievaulasi pada semester 1
3. Curricular_units_1st_sem_approved : Jumlah mata kuliah siswa yang disetujui pada semester 1
4. Curricular_units_1st_sem_grade : Hasil akademik untuk setiap mata kuliah yang diambil oleh siswa pada semester 1
5. Curricular_units_2nd_sem_enrolled : Jumlah mata kuliah yang diambil siswa pada semester 2
6. Curricular_units_2nd_sem_evaluations : Jumlah mata kuliah siswa yang dievaulasi pada semester 2
7. Curricular_units_2nd_sem_approved : Jumlah mata kuliah siswa yang disetujui atau diakui pada semester 2
8. Curricular_units_2nd_sem_grade : Hasil akademik untuk setiap mata kuliah yang diambil oleh siswa pada semester 2
9. Admission_grade : Penilaian yang digunakan sebagai kriteria untuk diterima ke dalam sebuah program pendidikan
10. Age_at_enrollment : Usia ketika siswa mendaftarkan diri
11. Previous_qualification_grade : Hasil akademik siswa sebelum mendaftar pada institut
12. GDP

Hasil akurasi yang didapatkan dari pelatihan model adalah sebagai berikut :
1. DecisionTree : 69%
2. RandomForest : 85%

Berdasarkan hasil training di antara 2 model machine learning, model RandomForest memiliki nilai akurasi lebih baik jika dibandingkan dengan model DecisionTree sehingga model RandomForest akan digunakan sebagai model pada applikasi yang akan mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

## Rekomendasi Action Items

Berdasarkan data yang sudah dianalisis insitut Jaya Jaya dapat melakukan langkah-langkah berikut untuk meminimalisir siswa yang akan dropout dari Institut Jaya Jaya:
1. Pembayaran Bertahap: Mengimplementasikan opsi pembayaran biaya sekolah secara bertahap atau cicilan untuk meringankan beban keuangan siswa dan orang tua.
2. Program Beasiswa Khusus: Membuat program beasiswa khusus untuk siswa yang orang tuanya memiliki pekerjaan tidak terampil.
3. Perluasan Program Beasiswa: memperluas program beasiswa untuk mencakup lebih banyak siswa, terutama mereka yang berada dalam risiko dropout.Selain itu, buat kriteria beasiswa yang lebih fleksibel sehingga lebih banyak siswa dapat memenuhi syarat.
4. Kurikulum Relevan: Pastikan kurikulum program studi relevan dengan kebutuhan industri dan menarik minat siswa untuk belajar.Meningkatkan kegiatan ekstrakurikuler dan pengembangan soft skills untuk mendukung keseimbangan antara akademik dan kegiatan non-akademik.


  
