# Laporan Proyek Machine Learning - Rhamdan Syahrul Mubarak

## advertisement click on ad

### Domain Proyek
Pertumbuhan banyaknya penonton film yang meningkat selaras dengan banyaknya jumlah film yang diproduksi. Berbagai film dengan alur cerita, genre, dan tema film yang serupa ataupun berbeda-beda meramaikan pasar industri dari bidang perfilman di luar negeri hingga dalam negeri. Dari banyaknya film yang diproduksi membuat calon penonton bingung dan kesulitan untuk mencari dan menentukan film apa yang akan ditonton selanjutnya sehingga menghabiskan waktu lebih banyak dalam mencari film. Beberapa orang menggunakan fitur yang disediakan di beberapa situs untuk mencari film untuk memutuskan film yang akan ditonton. Setiap orang memiliki selera yang berbeda-beda dan cenderung memilih menonton film yang serupa dengan film yang disukainya. 

Salah satu cara untuk mendapatkan informasi yang tepat terhadap film adalah dengan sistem rekomendasi. Setiap film memiliki beberapa informasi berupa genre film dan sinopsis film yang berbeda-beda. Pada penelitian ini untuk mendapatkan hasil rekomendasi menggunakan algoritme content based filtering dengan mencari kemiripan bobot dari term pada bag of words hasil pre-processing sinopsis film dan genre film. Pembobotan dilakukan menggunakan metode TF-IDF yang telah dinormalisasi. Kemudian hasil pembobotan akan melalui tahap cosine distance untuk mencari kemiripan berdasarkan sinopsisnya dan diakhiri dengan filtering berdasarkan genre menggunakan cosine similarity.

## Business Understanding

### Problem Statements
- Bagaimana cara menentukan rekomendasi film yang cocok untuk pengguna ?
- Siapa pengguna yang cocok untuk melihat film sesuai dengan film yang baru mereka tonton ?
- seberapa cocok rekomendasi film yang diberikan kepada pengguna berdasarkan film yang mereka tonton ?

### Goals
- Dapat menentukan rekomendasi film yang cocok untuk ditonton oleh pengguna.
- Dapat meningkatan intensitas pengguna dalam menonton menggunakan aplikasi atau _website_ yang dibuat.
- Dapat menentukan apakah rekomendasi film menggunakan _content filtering_ cocok digunakan untuk membuat rekomendasi film.

### Solution statements

Untuk menyelesaikan masalah ini terdapat solusi yang digunakan, yaitu menggunakan _matrics pairwise_ yaitu _cossine simmilarity_ untuk menentukan _genre_ film rekomendasi yang mirip seperti film yang ditonton. Hal tersebut karena dirasa teknik tersebut cocok untuk model _content-based filtering_

## Data Understanding
dataset yang digunakan ini merupakan salah satu dataset yang tersedia secara bebas untuk digunakan pada kaggle dataset. Isi dari dataset ini adalah mengenai film yang sudah tayang. Rentang waktu yang terdapat di dalam dataset ini berisi dari tahun 1986 hingga 2022 yang berisikan 9373 film. kolom yang terdapat pada dataset ini adalah _movie id_, _title_, dan _genres_.

Data untuk melakukan pemodelan machine learning untuk kasus ini diambil pada website kaggle dengan link sebagai berikut :
[Movie recomendation pjct](https://www.kaggle.com/datasets/sayan0211/movie-recomendation-pjct).

### Variabel-variabel pada Advertisement - Click on Ad dataset adalah sebagai berikut:
_movie id_ : merupakan primary key pada setiap film
_title_: Berisikan judul-judul film yang ada di dataset. \
_genres_: Berisikan genre film

### Explorasi data yang dilakukan
Beberapa explorasi yang dilakukan antara lain :
1. mencari nilai _null_. \
   Pada dataset yang digunakan ini, terdapat beberapa kolom yang memiliki nilai kosong atau _None_. Tujuan dari melakukan ini adalah untuk mencari tahu baris-baris yang data yang dapat digunakan sehingga data dapat bekerja secara optimal. fungsi yang digunakan adalah pandas.DataFrame.isnull() tanpa parameter yang diisikan di dalamnya. 

2. Mencari nilai _Duplicated_ \
   pada dataset yang digunakan ini, terdapat beberapa dataset yang yang memiliki nilai sama pada baris yang berbeda. Tujuan dari melakukan ini adalah untuk mencari tahu teknik terbaik untuk mengurus data yang terduplikasi ini. fungsi yang digunakan adalah pandas.Dataframe.duplicated() dengan parameter yang digunakan ada subset dan berisikan kolom _title_ di dalamnya. Hal tersebut bermaksud untuk mencari judul film yang terduplikasi.  
   
## Data Preparation
Beberapa data preparation yang dilakukan antara lain :
1. Menghilangkan nilai _null_. \
   untuk mengurangi data-data yang tidak dapat digunakan, maka salah satu cara terbaik yang dapat digunakan adalah dengan menghapus nilai _Null_ pada dataset. Dikarenakan dataset yang cukup besar dibandingkan dengan dataset yang memiliki niai _null_ maka teknik ini dapat menjadi solusi yang baik. fungsi yang digunakan adalah pandas.DataFrame.dropna() dan parameter yang diisikan pada fungsi ini adalah _inplace_ yang berisikan nilai boolearn _True_ yang berarti data akan terganti dengan permanen menggantikan _dataframe_ sebelumnya.
   
2.Menghilangkan nilai _duplicated_. \
  Data yang memiliki nilai yang sama membuat dataset menjadi bekerja kurang optimal, maka salah satu cara terbaik yang dapat digunakan untuk mengoptimalisasi adalah dengan menghapus nilai _duplicated_ pada dataset. Fungsi yang digunakan untuk ini adalah pandas.Dataframe.drop_duplicates() dengan parameter adalah _subset_ dan nilai yang diisikan pada parameter tersebut adalah _title_, karena tujuan dari ini adalah untuk menghilangkan judul film yang terduplikasi.
  
3. melakukan _vectorize_ \
   vektorisasi adalah langkah dalam ekstraksi fitur. Idenya adalah untuk mendapatkan beberapa fitur berbeda dari teks untuk model untuk dilatih, dengan mengubah teks menjadi vektor numerik. Pada fungsi TfidfVectorizer(), tidak terdapat parameter yang diiskan, tetapi pada data.fit() terdapat parameter _genre_ yang diisikan sebagai parameter karena kata-kata yang terdapat pada kolom genre ingin dilakukan vektorisasi.
   
4. melakukan _matrics pairwise_
   Memberikan pendekatan yang konsisten dan efisien untuk memprioritaskan atau memeringkat beberapa opsi. _matrics pairwise_ yang digunakan pada kasus ini adalah _cosine similarity_ karena ingin mencari nilai kedekatan yang ada pada setiap genre. Parameter yang diisikan pada fungsi ini adalah variabel untuk TF-IDF yang sudah dijadikan bentuk matriks.
   
## Modeling
![cosine](https://user-images.githubusercontent.com/95296474/188324509-a581e5ac-b4bf-4c3b-b31e-35a41ce1c5e2.png)<br>
Gambar diatas merupakan kode yang dituliskan untuk mendapatkan nilai _cosine similarity_ pada kolom _genre_. Dengan menggunakan fungsi tersebut, maka dapat diketahui nilai kedekatan pada masing-masing genre yang ada. Setelah dibuat nilai _cosine similarity_, maka langkah selanjutnya adalah membuat fungsi untuk menampilkan rekomendasi film seperti berikut.

![function recomendation](https://user-images.githubusercontent.com/95296474/188324631-bbb10413-4402-4e6d-8f23-135ad16d2a6a.png) <br>
Beberapa parameter yang terdapat pada fungsi rekomendasi adalah :
1. title : judul film (index kemiripan dataframe).
2. Similarity_data : Dataframe mengenai similarity yang telah kita definisikan sebelumnya.
3. Items : Nama dan fitur yang digunakan untuk mendefinisikan kemiripan, dalam hal ini adalah ‘title’, 'year' dan ‘genres’.
4. k : Banyak rekomendasi yang ingin diberikan.

Dengan menggunakan argpartition, kita mengambil sejumlah nilai k tertinggi dari similarity data (dalam kasus ini: dataframe cosine_sim_df). Kemudian, kita mengambil data dari bobot (tingkat kesamaan) tertinggi ke terendah. Data ini dimasukkan ke dalam variabel closest. Berikutnya, kolom _title_ yang yang dicari juga harus dihapus agar tidak muncul dalam daftar rekomendasi. 

## _Evaluation_




**Daftar Pustaka**
1. [Recomender System Handbook : Second Edition](https://www.google.co.id/books/edition/Recommender_Systems_Handbook/hGb_CgAAQBAJ?hl=en&gbpv=1&dq=content+filtering+machine+learning&printsec=frontcover)
