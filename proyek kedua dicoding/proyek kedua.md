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

Untuk menyelesaikan masalah ini terdapat solusi yang digunakan, yaitu menggunakan lebih dari 1 _matrics pairwise_ yaitu _cossine simmilarity_ untuk menentukan _genre_ film rekomendasi yang mirip seperti film yang ditonton dan _cossine distance_ untuk mengukur kedekatan film berdasarkan sinopsinya 

## Data Understanding
dataset yang digunakan ini merupakan salah satu dataset yang tersedia secara bebas untuk digunakan pada kaggle dataset. Isi dari dataset ini adalah mengenai film yang sudah tayang. Rentang waktu yang terdapat di dalam dataset ini berisi dari tahun 1986 hingga 2022 yang berisikan lebih dari 900 ribu film. Dikarenakan jumlah film yang terlalu banyak sehingga dataset yang digunakan adalah 5000 saja.Terdapat beberapa kolom yang terdapat pada dataset ini, tetapi kolom yang digunakan hanya _title_, _overview_, dan _genres_.
Data untuk melakukan pemodelan machine learning untuk kasus ini diambil pada website kaggle dengan link sebagai berikut :
[Advertisement - Click on Ad dataset](https://www.kaggle.com/datasets/gabrielsantello/advertisement-click-on-ad).

### Variabel-variabel pada Advertisement - Click on Ad dataset adalah sebagai berikut:
_title_: Berisikan judul-judul film yang ada di dataset. \
_overview_: Berisikan sinopsis film yang ada di dataset. \
_genres_: Berisikan genre film

### Explorasi data yang dilakukan
Beberapa explorasi yang dilakukan antara lain :
1. mencari nilai _null_. \
   Pada dataset yang digunakan ini, terdapat beberapa kolom yang memiliki nilai kosong atau _None_. Tujuan dari melakukan ini adalah untuk mencari tahu baris-baris yang data yang dapat digunakan sehingga data dapat bekerja secara optimal.
2. Mencari nilai _Duplicated_ \
   pada dataset yang digunakan ini, terdapat beberapa dataset yang yang memiliki nilai sama pada baris yang berbeda. Tujuan dari melakukan ini adalah untuk mencari tahu teknik terbaik untuk mengurus data yang terduplikasi ini. 

## Data Preparation
Beberapa data preparation yang dilakukan antara lain :
1. Menghilangkan nilai _null_. \
   untuk mengurangi data-data yang tidak dapat digunakan, maka salah satu cara terbaik yang dapat digunakan adalah dengan menghapus nilai _Null_ pada dataset. Dikarenakan dataset yang cukup besar dibandingkan dengan dataset yang memiliki niai _null_ maka teknik ini dapat menjadi solusi yang baik.
2.Menghilangkan nilai _duplicated_. \
  Data yang memiliki nilai yang sama membuat dataset menjadi bekerja kurang optimal, maka salah satu cara terbaik yang dapat digunakan untuk mengoptimalisasi adalah dengan menghapus nilai _duplicated_ pada dataset.
3. melakukan _vectorize_ \
   vektorisasi adalah langkah dalam ekstraksi fitur. Idenya adalah untuk mendapatkan beberapa fitur berbeda dari teks untuk model untuk dilatih, dengan mengubah teks menjadi vektor numerik.
4. melakukan _matrics pairwise_
   Memberikan pendekatan yang konsisten dan efisien untuk memprioritaskan atau memeringkat beberapa opsi. Dua _matrics pairwise_ yang digunakan adalah pembobotan akan melalui tahap cosine distance untuk mencari kemiripan berdasarkan sinopsisnya dan diakhiri dengan filtering berdasarkan genre menggunakan cosine similarity.
   
## Modeling
modeling yang digunakan adalah dengan menggunakan _matrics pairwise_. Jadi, model yang kami buat Memberikan pendekatan yang konsisten dan efisien untuk memprioritaskan atau memeringkat beberapa opsi. Dua _matrics pairwise_ yang digunakan adalah pembobotan akan melalui tahap cosine distance untuk mencari kemiripan berdasarkan sinopsisnya dan diakhiri dengan filtering berdasarkan genre menggunakan cosine similarity.

## _Evaluation_
![alt text](https://github.com/rhamdansm/Kaggle-Practice/blob/main/proyek%20kedua%20dicoding/recomendation.png)

Gambar diatas merupakan hasil yang didapatkan pada percobaan untuk melakukan rekomendasi. Berikut adalah penjelasan dari setiap 5 rekomendasi film yang diberikan oleh sistem.
1. Rekomendasi film yang diberikan oleh sistem berdasarkan sinopsinya terasa masih kurang tepat. Hal tersebut dikarenakan film-film yang dijadikan rekomendasi oleh sistem memiliki cerita dan genre yang berbeda. Sebagai contoh, film "American Horor Movie" memiliki cerita yang berbeda jauh dengan alur cerita yang berada di film "Dragon Ball Super: Super Hero", selain itu juga film tersebut memiliki genre yang berbeda sehingga kemungkinan besar pengguna tidak akan menonton film yang direkomendasikan.

2. Rekomendasi film yang diberikan oleh sistem berdasarkan genrenya sudah cukup baik karena memiliki genre yang masih berhubungan dengan film yang ditonton pengguna. Namun sinopsis pada film yang direkomendasikan masih terasa kurang pas.

3. Rekomendasi film yang diberikan oleh sistem berdasarkan sinopsis dan genrenya sudah lebih baik karena memiliki genre yang masih berhubungan dengan film yang ditonton pengguna dan sinopsis pada film tersebut sedikit mirip dengan film yang sudah ditonton oleh pengguna.


**Daftar Pustaka**
1. [Recomender System Handbook : Second Edition](https://www.google.co.id/books/edition/Recommender_Systems_Handbook/hGb_CgAAQBAJ?hl=en&gbpv=1&dq=content+filtering+machine+learning&printsec=frontcover)
