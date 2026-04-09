from src.config import CLEANED_DATA_PATH, SIMILARITY_PATH, MOVIES_PATH
from src.data_loader import load_csv
from src.preprocessing import preprocess_tags
from src.vectorizer import build_similarity
from src.recommender import recommend
from src.utils import save_pickle, load_pickle


def main():
    # 1️⃣ Load cleaned CSV
    df = load_csv(CLEANED_DATA_PATH)

    # 2️⃣ Preprocess tags
    df = preprocess_tags(df)

    # 3️⃣ Build similarity matrix
    similarity = build_similarity(df)

    # 4️⃣ Prepare movies dataframe (drop tags)
    movies = df.drop(columns=["tags"])

    # 5️⃣ Save artifacts
    save_pickle(movies, MOVIES_PATH)
    save_pickle(similarity, SIMILARITY_PATH)

    print("DONE: Movies & similarity saved successfully")

    # -------------------------------
    # 6️⃣ LOAD PICKLES (IMPORTANT)
    # -------------------------------
    movies_loaded = load_pickle(MOVIES_PATH)
    similarity_loaded = load_pickle(SIMILARITY_PATH)

    print("DONE: Movies & similarity loaded successfully")

    # -------------------------------
    # 7️⃣ OFFLINE RECOMMENDATION TEST
    # -------------------------------
    test_movie = "Avatar"  # must exist in dataset

    try:
        results = recommend(
            movie_title=test_movie,
            movies_df=movies_loaded,
            similarity=similarity_loaded,
            top_n=5
        )

        print(f"\nRecommendations for '{test_movie}':")
        for title, movie_id in results:
            print(f"- {title} (ID: {movie_id})")

    except Exception as e:
        print("ERROR: Recommendation failed:", e)


if __name__ == "__main__":
    main()
