from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def build_similarity(df: pd.DataFrame, text_col: str = "tags"):
    """
    Build cosine similarity matrix.
    """
    if text_col not in df.columns:
        raise KeyError(f"Column '{text_col}' not found")

    vectorizer = CountVectorizer(max_features=5000, stop_words="english")
    vectors = vectorizer.fit_transform(df[text_col])

    similarity = cosine_similarity(vectors)
    return similarity
