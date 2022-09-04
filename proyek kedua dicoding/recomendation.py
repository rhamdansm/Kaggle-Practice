import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nltk
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity, cosine_distances
pd.options.mode.chained_assignment = None

data = pd.read_csv("/content/movies.csv")
data = data.loc[:5000, ["title", "genres", "overview"]]

data.dropna(inplace=True)
data = data.drop_duplicates(subset=["title"])

def Vectorize(data, column, cosine):
  # Inisialisasi TfidfVectorizer
  tf = TfidfVectorizer()
  
  # Melakukan perhitungan idf pada data cuisine
  tf.fit(data[column])

  # Melakukan fit lalu ditransformasikan ke bentuk matrix
  tfidf_matrix = tf.fit_transform(data[column]) 
  
  if cosine == 0:
    cosine_dis =  cosine_distances(tfidf_matrix)
    cosine_dis_df = pd.DataFrame(cosine_dis, index=data['title'], columns=data['title'])
    return cosine_dis_df
  else :
    cosine_sim = cosine_similarity(tfidf_matrix)
    cosine_sim_df = pd.DataFrame(cosine_sim, index=data['title'], columns=data['title'])
    return cosine_sim_df


cosine_dis_overview = Vectorize(data, "overview", 0)
cosine_sim_genres = Vectorize(data, "genres", 1)

def movie_recommendations(title, distance_data=cosine_dis_overview, similarity_data=cosine_sim_genres,items=data[["title", "genres", "overview"]], k=300):
 
    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan    
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index_dis = distance_data.loc[:,title].to_numpy().argpartition(
        range(-1, -300, -1))

    index_sim = similarity_data.loc[:,title].to_numpy().argpartition(
        range(-1, -300, -1))
    
    # Mengambil data dengan similarity dan distance terbesar dari index yang ada
    closest_dis = distance_data.columns[index_dis[-1:-(300+2):-1]]
    closest_sim = similarity_data.columns[index_sim[-1:-(300+2):-1]]
    
    # Drop title agar nama resto yang dicari tidak muncul dalam daftar rekomendasi
    closest_dis = closest_dis.drop(title, errors='ignore')
    closest_sim = closest_sim.drop(title, errors='ignore')

    # Menggabungkan title yang di rekomendasikan berdasarkan overview dan genrenya
    closest = [x for x in tuple(closest_dis) if x in tuple(closest_sim)]
    
    # Pandas dataframe rekomendasi film
    rec_overview = data.set_index("title").loc[closest_dis, :].head()
    rec_genres = data.set_index("title").loc[closest_sim, :].head()
    full_rec = data.set_index("title").loc[closest, :].head()
    
    return rec_overview, rec_genres, full_rec

rec_overview, rec_genres, full_rec = movie_recommendations('Dragon Ball Super: Super Hero')