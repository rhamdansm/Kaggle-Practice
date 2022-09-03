# Laporan Proyek Machine Learning - Rhamdan Syahrul Mubarak

## advertisement click on ad

### Domain Proyek
Pemasaran internet telah mengambil alih strategi pemasaran tradisional di masa lalu. Perusahaan lebih suka mengiklankan produk mereka di situs web dan platform media sosial. Namun, menargetkan audiens yang tepat masih menjadi tantangan dalam pemasaran online. Menghabiskan jutaan untuk menampilkan iklan kepada audiens yang tidak mungkin membeli produk Anda bisa menjadi sia-sia.

Pada repository ini, saya akan bekerja dengan data periklanan dari agensi pemasaran untuk mengembangkan algoritma pembelajaran mesin yang memprediksi apakah pengguna tertentu akan mengklik iklan. Data terdiri dari 10 variabel:  'Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage', 'Ad Topic Line', 'City', 'Male', 'Country', Timestamp' dan 'Clicked on Ad'.

Variabel utama yang kami minati adalah 'click on ad'. Variabel ini dapat memiliki dua kemungkinan hasil: 0 dan 1 di mana 0 mengacu pada kasus di mana pengguna tidak mengklik iklan, sedangkan 1 mengacu pada skenario di mana pengguna mengklik iklan.

Pada masa digital saat ini, kebutuhan akan iklan digital menjadi berkembang secara pesat. Namun sayangnya, tidak semua iklan yang ada di internet mampu untuk menarik orang untuk melihat iklan tersebut. Oleh karena itu, dengan model ini diharapkan dapat membantu para pengiklan untuk merencanakan pemasaran produk mereka secara digital. 

Cara yang dilakukan untuk dapat membuat model _machine learning_ ini adalah dengan melakukan sebuah klasifikasi biner untuk menentukan apakah user yang meilhat iklan ini mengklik iklan tersebut berdasarkan dengan background user. 

## Business Understanding

### Problem Statements
- Bagaimana bentuk iklan digital yang efektif di situs _website_ dan platform sosial media ?
- Siapa audiens yang cocok untuk melihat iklan produk digital ?
- Berapa banyak dana yang harus digunakan untuk membuat iklan digital suatu produk ?

### Goals
- Dapat menentukan prediksi apakah iklan yang dibuat akan dilirik oleh audiens atau tidak
- Membantu membuat prediksi jenis iklan yang mungkin akan dilirik oleh audiens
- Membantu menghemat dana untuk mengiklankan suatu produk secara digital

### Solution statements

Untuk menyelesaikan masalah ini terdapat beberapa solusi yang digunakan, antara lain :
- menggunakan lebih dari 1 algoritma machine learning yang cocok untuk melakukan klasifikasi, seperti logistik regression, Naive bayes, Random Forest, dan Decission Tree.
- Membuat metriks evaluasi untuk membandingkan masing-masing algoritma tersebut untuk mencari yang paling optimal. Beberapa matriks yang digunakan, antara lain Confusion matrix, Classification report, dan Accuracy

## Data Understanding
dataset yang digunakan ini merupakan salah satu dataset yang tersedia secara bebas untuk digunakan pada kaggle dataset. Isi dari dataset ini adalah mengenai iklan _click on_ yang ada di dunia digital. Rentang waktu yang terdapat di dalam dataset ini berisi dari januari 2016 hingga Juli 2016 yang berisikan 1000 iklan yang berbeda. Terdapat beberapa kolom yang terdapat pada dataset ini, seperti umur audiens, rata-rata pendapatan wilayah audiens, jenis kelamin audiens, dan sebagainya. Namun tidak semua fitur yang terdapat pada dataset ini memiliki korelasi yang baik terhadap pengaruh audiens untuk menekan iklan tersebut, sehingga perlu dicari terlebih dahulu fitur yang cocok untuk dapat digunakan dalam membuat model prediksi. Dataset ini sudah memiliki kolom _clicked on_ yang digunakan sebagai label, sehingga model _machine learning_ yang cocok untuk dataset dan kasus ini adalah _clustering_.
Data untuk melakukan pemodelan machine learning untuk kasus ini diambil pada website kaggle dengan link sebagai berikut :
[Advertisement - Click on Ad dataset](https://www.kaggle.com/datasets/gabrielsantello/advertisement-click-on-ad).

### Variabel-variabel pada Advertisement - Click on Ad dataset adalah sebagai berikut:
- '_Daily Time Spent on Site_': waktu konsumen di situs dalam hitungan menit
- '_Age_': usia pelanggan dalam tahun
- '_Area Income_': Rata-rata. Pendapatan wilayah geografis konsumen
- '_Daily Internet Usage_': Rata-rata. menit sehari konsumen ada di internet
- '_Ad Topic Line_': Judul iklan
- '_City_': Kota konsumen
- '_Male_': Apakah konsumen adalah laki-laki atau tidak
- '_Country_': Negara konsumen
- '_Timestamp_': Waktu saat konsumen mengklik Iklan atau jendela tertutup
- '_Clicked On_': 0 atau 1 menunjukkan mengklik Iklan

### Explorasi data yang dilakukan
Beberapa explorasi yang dilakukan antara lain :
1. mencari nilai _outlier_ dan membuangnya. \
   Pada repository ini, metode yang digunakan untuk mendeteksi outlier adalah dengan menggunakan metode IQR. Dengan menggunakan metode ini, terdapat beberapa outlier yang terdapat pada kolom _area income_.
2. Mencari nilai persebaran data numerik. \
   diagram yang digunakan untuk menampilkan data persebaran nilai numerik adalah menggunakan _histogram chart_. Tujuan dari melakukan ini adalah untuk mencari tahu persebaran data yang terdapat pada data numerik dan hasil yang didapatkan adalah dataset memiliki distribusi data yang cukup baik.
3. mencari nilai persebaran data kategorik. \
   diagram yang digunakan untuk menampilkan data persebaran nilai kategorik adalah menggunakan _bar chart_. Tujuan dari melakukan ini adalah untuk mencari tahu persebaran data yang terdapat pada data kategorik dan didapatkan hasil bahwa data pada kolom _clicked on_ dan _male_ memiliki jumlah nilai yang hampir sama atau tidak ada yang _oversampling_.
4. Melakukan _Multivariate Analysis_. \
   digunakan _pairplot chart_ Untuk melakukan _Multivariate Analysis_ untuk setiap data numerik yang ada pada dataset.

## Data Preparation
Beberapa data preparation yang dilakukan antara lain :
1. Menghilangkan _Outlier_. \
   mengurangi bias pada data. Karena jumlah outlier tidak terlalu banyak, maka untuk mengatasi hal tersebut adalah dengan menghapus baris yang memiliki nilai _outlier_.
2. _Feature Scalling_. \
   membuat data numerik pada dataset memiliki rentang nilai (_scale_) yang sama sehingga didak ada lagi satu variabel data yang mendominasi variabel data lainnya. _feature scalling_ yang digunakan pada kasus ini adalah dengan menggunakan _MinMaxScaller_ untuk mengubah rentang nilai yang ada menjadi -1 hingga 1
3. _Splitting train-test data_. <br> 
   membagi dataset menjadi data latih dan data uji dengan ratio split adalah 70% untuk data latih dan 30% untuk data uji.

## Modeling
Beberapa algoritma yang digunakan antara lain :
1. _Binary Logistic Regression_. \
   _Logistic Regression_ yang hanya memiliki 2 output saja (mengklasifikasi kedalam 2 kelas berbeda)
    * Kelebihan
      - Variabel independen dalam regresi logistik bisa campuran dari variabel kontinu, distrik, dan dikotomis. 
      - Regresi logistik tidak membutuhkan keterbatasan dari variabel independennya. 
      - Regresi logistik tidak mengharuskan variabel bebasnya dalam bentuk interval
    * Kekurangan
      - rentan terhadap underfitting pada dataset yang kelasnya tidak seimbang, sehingga akan menghasilkan akurasi yang rendah.
     
2. _Gausian Naive Bayes_. \
   _Naive Bayes_ menerapkan Teorema Bayes, sebuah formula matematika sederhana yang digunakan untuk probabilitas bersyarat (_conditional probability_).
   * Kelebihan
      - model yang sederhana, namun dapat bersaing dengan model algoritma lainnya. 
      - Implementasinya tidak terlalu rumit, cocok untuk mengevaluasi probabilitas bersyarat.
      - probabilitas dapat langsung dihitung. Jadi, algoritma ini berguna saat membutuhkan kecepatan pelatihan yang tinggi.
    * Kekurangan
      - Algoritma ini menerapkan asumsi independensi bersyarat, sayangnya hal ini tidak selalu berlaku. Dalam kebanyakan situasi, fitur yang ada justru menunjukkan beberapa bentuk dependensi.

3. _Random Forest_. \
    algoritma ini menerapkan teknik ansambel. Teknik ansambel sendiri berarti menggabungkan banyak penggolong (_classifiers_) untuk bisa memberikan solusi terhadap masalah yang kompleks. Parameter yang digunakan pada model ini adalah _n estimators_ sebanyak 100.
   * Kelebihan
      - Random forest dapat dijalankan pada tugas klasifikasi sekaligus regresi. 
      - algoritma ini juga mampu menghasilkan prediksi dengan tingkat akurasi tinggi yang mudah dipahami. 
      - Jika diterapkan pada kumpulan dataset berskala besar, random forest akan bekerja secara efisien. 
    * Kekurangan
      - Untuk bisa menghasilkan prediksi dengan tingkat akurasi tinggi, diperlukan lebih banyak sumber daya dalam proses komputasi.
      - Makin banyak sumber daya yang diperlukan, artinya makin banyak juga waktu yang diperlukan untuk bisa memprediksi hasil.
 
4. _Decission Tree_. \
   Sebuah Algoritma _Machine Learning_ dengan struktur seperti pohon yang memodelkan kemungkinan hasil, biaya sumber daya, utilitas, dan kemungkinan konsekuensi. Parameter yang digunakan pada model ini adalah _max depth_ sebanyak 10.
   * Kelebihan
      - Mudah dibaca dan ditafsirkan
      - Mudah disiapkan
      - Lebih sedikit pembersihan data yang diperlukan
    * Kekurangan
      - Sifat tidak stabil
      - Kurang efektif dalam memprediksi hasil dari variabel kontinu
   
**Algoritma _Machine Learning_ yang paling Optimal** digunakan pada contoh kasus ini adalah _Naive bayes_. Karena kasus yang ada pada saat ini merupakan salah satu bentuk probabilitas bersyarat (_conditional probability_). Selain itu, berdasarkan matrik evaluasi hasil uji menunjukan bahwa nilai akurasi terbesar pada model _machine learning_ yang dibuat pada setiap algoritma berada pada algoritma _Naive Bayes_ dengan nilai akurasi sekitar 96%.

## _Evaluation_
Beberapa matriks yang digunakan untuk melakukan evaluasi antara lain :
1. _Confusion matrix_ : \
   pengukuran performa untuk masalah klasifikasi _machine learning_ dimana keluaran dapat berupa dua kelas atau lebih. _Confusion Matrix_ adalah tabel dengan 4 kombinasi berbeda dari nilai prediksi dan nilai aktual.
2. _Classification report_ : \
   Matriks evaluasi yang menampilkan tiga nilai evaluasi dalam bentuk _True positive_, _True Negative_, _False Positive_, dan _False Negative_.
4. _Accuracy_ : \
   tingkat kedekatan antara nilai prediksi dengan nilai aktual.

**Alasan menggunakan ketiga metriks** tersebut dikarenakan ketiga metriks evaluasi tersebut cocok digunakan pada suatu model klasifikasi. Dengan menggunakan matriks-matriks tersebut, maka kita dapat menentukan algoritma _machine learning_ mana yang menghasilkan prediksi klasifikasi yang paling sesuai.

**Nilai _Accuracy_ Setiap Model yang digunakan:**
_Logistic Regression_	: 0.889261744966443
_Naive Bayes_		      : 0.9630872483221476
_Random Forest_		   : 0.9563758389261745
_Decission Tree_	   : 0.9429530201342282

**berdasarkan matrik akurasi hasil uji** menunjukan bahwa algoritma _machine learning_ yang terbaik pada kasus ini adalah pada saat menggunakan _Naive bayes_. Hal tersebut juga dapat diperkuat dengan matriks _confusion matriks_ berikut untuk algoritma _naive bayes_.

| **keterangan**   | **Jumlah** |
| ---------------- | ---------- |
| _True Positive_  |    135     |
| _True Negative_  |    152     |
| _False Positive_ |     4      |
|_False Negative_  |     7      |

**Daftar Pustaka**
1. [Machine Learning Based Ad-click prediction system](https://www.researchgate.net/publication/336666758_Machine_Learning_Based_Ad-click_prediction_system)
2. [Click-Through Rate Prediction in Online Advertising: A Literature Review](https://arxiv.org/abs/2202.10462)
