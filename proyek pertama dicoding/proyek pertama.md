# Laporan Proyek Machine Learning - Rhamdan Syahrul Mubarak

## advertisement click on ad

### Domain Proyek
Pemasaran internet telah mengambil alih strategi pemasaran tradisional di masa lalu. Perusahaan lebih suka mengiklankan produk mereka di situs web dan platform media sosial. Namun, menargetkan audiens yang tepat masih menjadi tantangan dalam pemasaran online. Menghabiskan jutaan untuk menampilkan iklan kepada audiens yang tidak mungkin membeli produk Anda bisa menjadi sia-sia.

Pada repository ini, saya akan bekerja dengan data periklanan dari agensi pemasaran untuk mengembangkan algoritme pembelajaran mesin yang memprediksi apakah pengguna tertentu akan mengklik iklan. Data terdiri dari 10 variabel:  'Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage', 'Ad Topic Line', 'City', 'Male', 'Country', Timestamp' and 'Clicked on Ad'.

Variabel utama yang kami minati adalah 'click on ad'. Variabel ini dapat memiliki dua kemungkinan hasil: 0 dan 1 di mana 0 mengacu pada kasus di mana pengguna tidak mengklik iklan, sedangkan 1 mengacu pada skenario di mana pengguna mengklik iklan.

Pada masa digital saat ini, kebutuhan akan iklan digital menjadi berkembang secara pesat. Namun sayangnya, tidak semua iklan yang ada di internet mampu untuk menarik orang untuk melihat iklan tersebut. Oleh karena itu, dengan model ini diharapkan dapat membantu para pengiklan untuk merencanakan pemasaran produk mereka secara digital. 

Cara yang dilakukan untuk dapat membuat model machine learning ini adalah dengan melakukan sebuat klasifikasi biner untuk menentukan apakah user yang meilhat iklan ini mengklik iklan tersebut berdasarkan dengan background user. 

**Daftar Pustaka**
1. [Machine Learning Based Ad-click prediction system](https://www.researchgate.net/publication/336666758_Machine_Learning_Based_Ad-click_prediction_system)
2. [Click-Through Rate Prediction in Online Advertising: A Literature Review](https://arxiv.org/abs/2202.10462)

## Business Understanding

### Problem Statements
- Perusahaan lebih suka mengiklankan produk mereka di situs web dan platform media sosial.
- menargetkan audiens yang tepat masih menjadi tantangan dalam pemasaran online.
- Menghabiskan banyak dana untuk menampilkan iklan kepada audiens yang tidak mungkin membeli produk Anda bisa menjadi sia-sia.

### Goals
- Dapat menentukan prediksi apakah iklan yang dibuat akan dilirik oleh audiens atau tidak
- Membantu membuat prediksi jenis iklan yang mungkin akan dilirik oleh audiens
- Membantu menghemat dana untuk mengiklankan suatu produk secara digital

### Solution statements

Untuk menyelesaikan masalah ini terdapat beberapa solusi yang digunakan, antara lain :
- menggunakan lebih dari 1 algoritma machine learning yang cocok untuk melakukan klasifikasi, seperti logistik regression, Naive bayes, Random Forest, dan Decission Tree.
- Membuat metriks evaluasi untuk membandingkan masing-masing algoritma tersebut untuk mencari yang paling optimal. Beberapa matriks yang digunakan, antara lain Confusion matrix, Classification report, dan Accuracy

## Data Understanding
Data untuk melakukan pemodelan machine learning untuk kasus ini diambil pada website kaggle dengan link sebagai berikut :
[Advertisement - Click on Ad dataset](https://www.kaggle.com/datasets/gabrielsantello/advertisement-click-on-ad).

### Variabel-variabel pada Advertisement - Click on Ad dataset adalah sebagai berikut:
- 'Daily Time Spent on Site': waktu konsumen di situs dalam hitungan menit
- 'Age': usia pelanggan dalam tahun
- 'Area Income': Rata-rata. Pendapatan wilayah geografis konsumen
- 'Daily Internet Usage': Rata-rata. menit sehari konsumen ada di internet
- 'Ad Topic Line': Judul iklan
- 'City': Kota konsumen
- 'Male': Apakah konsumen adalah laki-laki atau tidak
- 'Country': Negara konsumen
- 'Timestamp': Waktu saat konsumen mengklik Iklan atau jendela tertutup
- 'Clicked On': 0 atau 1 menunjukkan mengklik Iklan

### Explorasi data yang dilakukan
Beberapa explorasi yang dilakukan antara lain :
1. mencari nilai outlier dan membuangnya. \
   Pada repository ini, metode yang digunakan untuk mendeteksi outlier adalah dengan menggunakan metode IQR.
2. Mencari nilai persebaran data numerik. \
   diagram yang digunakan untuk menampilkan data persebaran nilai numerik adalah menggunakan histogram chart.
3. mencari nilai persebaran data categorical. \
   diagram yang digunakan untuk menampilkan data persebaran nilai categorical adalah menggunakan bar chart.
4. Melakukan Multivariate Analysis. \
   digunakan pairplot chart Untuk melakukan Multivariate Analysis untuk setiap data numerik yang ada pada dataset.

## Data Preparation
Beberapa data preparation yang dilakukan antara lain :
1. Menghilangkan Outlier. \
   mengurangi bias pada data.
2. Feature Scalling. \
   membuat numerical data pada dataset memiliki rentang nilai (scale) yang sama sehingga Tidak ada lagi satu variabel data yang mendominasi variabel data lainnya.
3. Splitting train-test data.\ 
   membagi dataset menjadi data latih dan data uji dengan ratio split adalah 70% untuk data latih dan 30% untuk data uji.

## Modeling
Beberapa algoritma yang digunakan antara lain :
1. Binary Logistic Regression. \
   Logistic Regression yang hanya memiliki 2 output saja (mengklasifikasi kedalam 2 kelas berbeda)
    * Kelebihan
      - Variabel independen dalam regresi logistik bisa campuran dari variabel kontinu, distrik, dan dikotomis. 
      - Regresi logistik tidak membutuhkan keterbatasan dari variabel independennya. 
      - Regresi logistik tidak mengharuskan variabel bebasnya dalam bentuk interval
    * Kekurangan
      - rentan terhadap underfitting pada dataset yang kelasnya tidak seimbang, sehingga akan menghasilkan akurasi yang rendah.
     
2. Gausian Naive Bayes. \
   Naive Bayes menerapkan Teorema Bayes, sebuah formula matematika sederhana yang digunakan untuk probabilitas bersyarat (conditional probability).
   * Kelebihan
      - model yang sederhana, namun dapat bersaing dengan model algoritma lainnya. 
      - Implementasinya tidak terlalu rumit, cocok untuk mengevaluasi probabilitas bersyarat.
      - probabilitas dapat langsung dihitung. Jadi, algoritma ini berguna saat membutuhkan kecepatan pelatihan yang tinggi.
    * Kekurangan
      - Algoritma ini menerapkan asumsi independensi bersyarat, sayangnya hal ini tidak selalu berlaku. Dalam kebanyakan situasi, fitur yang ada justru menunjukkan beberapa bentuk dependensi.

3. Random Forest. \
    algoritma ini menerapkan teknik ansambel. Teknik ansambel sendiri berarti menggabungkan banyak penggolong (classifiers) untuk bisa memberikan solusi terhadap masalah yang kompleks.  
   * Kelebihan
      - Random forest dapat dijalankan pada tugas klasifikasi sekaligus regresi. 
      - algoritma ini juga mampu menghasilkan prediksi dengan tingkat akurasi tinggi yang mudah dipahami. 
      - Jika diterapkan pada kumpulan dataset berskala besar, random forest akan bekerja secara efisien. 
    * Kekurangan
      - Untuk bisa menghasilkan prediksi dengan tingkat akurasi tinggi, diperlukan lebih banyak sumber daya dalam proses komputasi.
      - Makin banyak sumber daya yang diperlukan, artinya makin banyak juga waktu yang diperlukan untuk bisa memprediksi hasil.
 
4. Decission Tree. \
   Sebuah Algoritma Machine Learning dengan struktur seperti pohon yang memodelkan kemungkinan hasil, biaya sumber daya, utilitas, dan kemungkinan konsekuensi.
   * Kelebihan
      - Mudah dibaca dan ditafsirkan
      - Mudah disiapkan
      - Lebih sedikit pembersihan data yang diperlukan
    * Kekurangan
      - Sifat tidak stabil
      - Kurang efektif dalam memprediksi hasil dari variabel kontinu
   
**Algoritma Machine Learning yang paling Optimal** digunakan pada contoh kasus ini adalah Naive bayes. Karena kasus yang ada pada saat ini merupakan salah satu bentuk probabilitas bersyarat (conditional probability). Selain itu, berdasarkan matrik evaluasi hasil uji menunjukan bahwa nilai akurasi terbesar pada model machine learning yang dibuat pada setiap algoritma berada pada algoritma Naive Bayes dengan nilai akurasi sekitar 96%.

## Evaluation
Beberapa matriks yang digunakan untuk melakukan evaluasi antara lain :
1. Confusion matrix : \
   pengukuran performa untuk masalah klasifikasi machine learning dimana keluaran dapat berupa dua kelas atau lebih. Confusion Matrix adalah tabel dengan 4 kombinasi berbeda dari nilai prediksi dan nilai aktual.
2. Classification report : \
   Matriks evaluasi yang menampilkan tiga nilai evaluasi dalam bentuk True positive, True Negative, False Positive, dan False Negative.
4. Accuracy : \
   tingkat kedekatan antara nilai prediksi dengan nilai aktual.

**Alasan menggunakan ketiga metriks** tersebut dikarenakan ketiga metriks evaluasi tersebut cocok digunakan pada suatu model klasifikasi. Dengan menggunakan matriks-matriks tersebut, maka kita dapat menentukan algoritma machine learning mana yang menghasilkan prediksi klasifikasi yang paling sesuai.

**Nilai Accuracy Setiap Model yang digunakan:**
Logistic Regression	: 0.889261744966443
Naive Bayes		      : 0.9630872483221476
Random Forest		   : 0.9563758389261745
Decission Tree		   : 0.9429530201342282

**berdasarkan matrik akurasi hasil uji** menunjukan bahwa algoritma machine learning yang terbaik pada kasus ini adalah pada saat menggunakan Naive bayes. Hal tersebut juga dapat diperkuat dengan matriks confusion matriks berikut untuk algoritma naive bayes.
True Positive  : 135
True Negative  : 152
False Positive : 4
False Negative : 7
