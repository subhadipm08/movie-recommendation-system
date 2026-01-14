from flask import Flask, render_template, request, jsonify
import pandas as pd

from src.config import MOVIES_PATH, SIMILARITY_PATH, TOP_N
from src.recommender import recommend
from src.tmdb import fetch_movie_poster
from src.utils import load_pickle


app = Flask(__name__)


try:
    movies_df = load_pickle(MOVIES_PATH)
    similarity = load_pickle(SIMILARITY_PATH)
    print("✅ Pickle files loaded successfully")
except Exception as e:
    print("❌ Failed to load pickle files:", e)
    movies_df, similarity = None, None



@app.route("/")
def index():
    return render_template("index.html")



@app.route("/autocomplete")
def autocomplete():
    if movies_df is None:
        return jsonify([])

    query = request.args.get("q", "").strip().lower()

    if not query:
        return jsonify([])

    matches = (
        movies_df[movies_df["title"].str.lower().str.contains(query)]
        ["title"]
        .head(10)
        .tolist()
    )

    return jsonify(matches)



@app.route("/recommend", methods=["POST"])
def recommend_api():
    if movies_df is None or similarity is None:
        return jsonify({
            "success": False,
            "error": "Model not loaded properly"
        })

    data = request.get_json()
    movie_name = data.get("movie", "").strip()

    if not movie_name:
        return jsonify({
            "success": False,
            "error": "Movie name is required"
        })

    try:
        results = recommend(
            movie_title=movie_name,
            movies_df=movies_df,
            similarity=similarity,
            top_n=TOP_N
        )

        response = []
        for title, movie_id in results:
            response.append({
                "title": title,
                "poster": fetch_movie_poster(movie_id)
            })

        return jsonify({
            "success": True,
            "data": response
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })



if __name__ == "__main__":
    app.run(debug=True,port=5000)


