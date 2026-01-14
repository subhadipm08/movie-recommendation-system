import numpy as np
import pandas as pd


def recommend(
    movie_title: str,
    movies_df: pd.DataFrame,
    similarity: np.ndarray,
    top_n: int = 5
) -> list:
    """
    Recommend top N movies similar to the given movie title.
    """

    if not movie_title or not isinstance(movie_title, str):
        raise ValueError("Movie title must be a non-empty string")

    if "title" not in movies_df.columns:
        raise KeyError("movies_df must contain a 'title' column")

    if len(movies_df) != similarity.shape[0]:
        raise ValueError("Similarity matrix size does not match movies_df")

    movie_title = movie_title.lower().strip()

    titles = movies_df["title"].str.lower()

    if movie_title not in titles.values:
        raise ValueError(f"Movie '{movie_title}' not found in database")

    idx = titles[titles == movie_title].index[0]

    distances = list(enumerate(similarity[idx]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)

    recommendations = []
    for i in distances[1 : top_n + 1]:
        recommendations.append((movies_df.iloc[i[0]]["title"],movies_df.iloc[i[0]]["id"]))

    return recommendations
