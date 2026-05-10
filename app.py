import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    indices, scores = similarity[movie_index]
    
    recommended_movies = []
    for idx in indices:
        if idx != movie_index: 
            recommended_movies.append(movies.iloc[idx].title)
        if len(recommended_movies) == 5:
            break
    return recommended_movies
    
    
similarity = pickle.load(open('similarity_compressed.pkl', 'rb'))
movies = pickle.load(open('movies.pkl','rb'))

movie_titles = movies['title'].values

st.title('Movie Recommender System')

movie=st.selectbox('Which movie would you like to watch? ',movie_titles)

if st.button('Recommend'):
    recommendations=recommend(movie)
    st.subheader("Top 5 Recommendations:")
    for i, rec in enumerate(recommendations, 1):
        st.write(f"{i}. {rec}")
