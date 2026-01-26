import streamlit as st
import json
import pickle
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env from current directory


# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

# ================= TMDB CONFIG =================
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
POSTER_BASE_URL = "https://image.tmdb.org/t/p/w500"

# ================= LOAD DATA =================
@st.cache_data
def load_movies():
    with open("movies_info/movies.json", "r", encoding="utf-8") as f:
        return json.load(f)

@st.cache_resource
def load_similarity():
    with open("movies_info/similarity.pkl", "rb") as f:
        return pickle.load(f)

movies = load_movies()
similarity = load_similarity()

movie_titles = [movie["title"].title() for movie in movies]
movie_ids = [movie["movie_id"] for movie in movies]

# ================= TMDB POSTER FETCH =================
@st.cache_data
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": TMDB_API_KEY}

    response = requests.get(url, params=params)
    data = response.json()

    poster_path = data.get("poster_path")
    if poster_path:
        return POSTER_BASE_URL + poster_path
    return None

# ================= RECOMMENDATION FUNCTION =================
def recommend(movie_title, n=5):
    index = movie_titles.index(movie_title)
    distances = similarity[index]

    recommended_indices = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:n+1]

    recommendations = []
    for i, _ in recommended_indices:
        recommendations.append({
            "title": movie_titles[i],
            "poster": fetch_poster(movie_ids[i])
        })

    return recommendations

# ================= UI =================
st.title("🎬 Movie Recommender System")
st.markdown("Discover movies similar to your favorites using **machine learning**.")
st.divider()

selected_movie = st.selectbox(
    "🎥 Select a movie",
    movie_titles
)

if st.button("🎯 Recommend Movies", use_container_width=True):
    results = recommend(selected_movie)

    st.subheader("🍿 Recommended Movies")

    cols = st.columns(len(results))
    for col, movie in zip(cols, results):
        with col:
            if movie["poster"]:
                st.image(movie["poster"], use_container_width=True)
            else:
                st.write("No poster available")
            st.caption(movie["title"])
