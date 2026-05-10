import streamlit as st
import pickle

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    indices, scores = similarity[movie_index]
    
    recommended_movies = []
    recommended_posters = []
    
    for idx in indices:
        if idx != movie_index:
            recommended_movies.append(movies.iloc[idx].title)
            recommended_posters.append(movies.iloc[idx].poster_url)
        if len(recommended_movies) == 5:
            break
    
    return recommended_movies, recommended_posters

similarity = pickle.load(open('similarity_compressed.pkl', 'rb'))
movies = pickle.load(open('movies_with_posters.pkl', 'rb'))
movie_titles = movies['title'].values

st.title('🎬 Movie Recommender System')
movie = st.selectbox('Which movie would you like to watch?', movie_titles)

if st.button('Recommend'):
    recommendations, posters = recommend(movie)
    st.subheader("Top 5 Recommendations:")
    
    cols = st.columns(5)
    for col, title, poster in zip(cols, recommendations, posters):
        with col:
            if poster:
                st.image(poster, use_container_width=True)
            st.caption(title)
