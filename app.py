import streamlit as st
import pickle
import pandas as pd



movies = pickle.load(open('movies.pkl','rb'))

movie_titles = movies['title'].values

st.title('Movie Recommender System')

movie=st.selectbox('Which movie would you like to watch? ',movie_titles)

if st.button('Recommend'):
    recommendations=recommend(movie)
    
    for i in recommendations:
        st.write(i)
