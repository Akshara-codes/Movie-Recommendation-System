import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index =movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
     # to hold the index
    recommended_movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    
    for i in recommended_movies_list:
        #movie_id=i[0]
        # fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
        
    return recommended_movies
    
similarity=pickle.load(open('similarity.pkl','rb'))       
movies = pickle.load(open('movies.pkl','rb'))

movie_titles = movies['title'].values

st.title('Movie Recommender System')

movie=st.selectbox('Which movie would you like to watch? ',movie_titles)

if st.button('Recommend'):
    recommendations=recommend(movie)
    
    for i in recommendations:
        st.write(i)
