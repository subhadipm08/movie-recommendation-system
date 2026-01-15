import requests
from src.config import  TMDB_API_KEY_CONFIG,TMDB_IMAGE_BASE_URL



def fetch_movie_poster(movie_id: int) -> str:
    """
    Fetch movie poster using TMDB movie ID.
    """

    try:
        TMDB_API_KEY = TMDB_API_KEY_CONFIG
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        params = {
            "api_key": TMDB_API_KEY
        }

        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()

        data = response.json()
        poster_path = data.get("poster_path")

        if poster_path:
            return f"{TMDB_IMAGE_BASE_URL}{poster_path}"

        return "/static/images/no_poster.png"

    except Exception:
        return "/static/images/no_poster.png"

    
# if __name__=="__main__":
#     print(fetch_movie_poster(285))
