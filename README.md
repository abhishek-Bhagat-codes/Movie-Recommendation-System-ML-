# 🎬 Movie Recommendation System

A machine learning-powered movie recommender application built with **Streamlit** that suggests movies similar to your favorites using content-based filtering.

## 📋 Features

- **Movie Search & Selection**: Browse and select from a comprehensive movie database
- **ML-Based Recommendations**: Uses similarity metrics to recommend 5 movies similar to your selection
- **Movie Posters**: Fetches and displays movie posters from TMDB API for visual reference
- **User-Friendly Interface**: Clean, intuitive Streamlit UI with interactive components
- **Fast Performance**: Leverages caching for optimal app performance

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- TMDB API Key (get one free at [themoviedb.org](https://www.themoviedb.org/settings/api))

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd movie_recommendation
   ```

2. **Install dependencies**
   ```bash
   pip install -r model_t/requirements.txt
   pip install streamlit requests python-dotenv
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   TMDB_API_KEY=your_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

The app will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
movie_recommendation/
├── app.py                          # Main Streamlit application
├── README.md                       # This file
├── model_t/
│   ├── movie_recom.ipynb          # ML model development notebook
│   ├── requirements.txt            # Python dependencies
│   ├── movies.json                # Movie metadata
│   ├── pkl_files/                 # Trained model files (pickled)
│   └── dataSet/
│       ├── credits.csv            # Cast and crew data
│       └── movies.csv             # Movie details and features
└── movies_info/
    └── movies.json                # Movie data used by the app
```

## 🤖 How It Works

1. **Data Processing**: The notebook (`movie_recom.ipynb`) processes movie data from CSV files
2. **Feature Engineering**: Creates feature vectors from movie attributes (genres, cast, crew, keywords, etc.)
3. **Similarity Calculation**: Computes cosine similarity between movies
4. **Recommendations**: When you select a movie, the system finds and ranks the most similar movies
5. **Poster Fetching**: Retrieves movie posters from TMDB API for visual display

## 🔧 Technologies Used

- **Streamlit**: Web app framework
- **scikit-learn**: Machine learning and similarity calculations
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **requests**: API calls to TMDB
- **pickle**: Model serialization

## 📊 Dataset

The project uses movie data from:
- **movies.csv**: Movie metadata (titles, genres, budget, runtime, etc.)
- **credits.csv**: Cast and crew information

### ⚠️ **IMPORTANT: Download Training Data**

The training datasets are **not included** in this repository due to file size limitations. You need to download them manually from Kaggle:

**Kaggle Dataset Link:** https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv

**Steps:**
1. Visit the Kaggle link above
2. Download both files:
   - `tmdb_5000_movies.csv`
   - `tmdb_5000_credits.csv`
3. Place them in the `model_t/dataSet/` directory
4. Run the `movie_recom.ipynb` notebook to generate the model files

## 🌐 API Integration

The app integrates with **The Movie Database (TMDB) API** to:
- Fetch high-quality movie posters
- Display current movie information

## 📝 Environment Variables

| Variable | Description |
|----------|-------------|
| `TMDB_API_KEY` | Your TMDB API key for poster fetching |

## 🎯 Usage

1. Launch the app
2. Select a movie from the dropdown menu
3. Click "🎯 Recommend Movies"
4. View 5 recommended movies with their posters

## 📈 Future Enhancements

- Add collaborative filtering for personalized recommendations
- Implement user ratings and feedback
- Add movie details (plot, reviews, ratings)
- Expand recommendation algorithm with hybrid approach
- Deploy as web service

## 🤝 Contributing

Contributions are welcome! Feel free to fork and submit pull requests.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created as a machine learning project for movie recommendation system.

---

**Note**: Make sure to add `.env` to your `.gitignore` to protect your API keys!





