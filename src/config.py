from pathlib import Path
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Base directory (project root)
BASE_DIR = Path(__file__).resolve().parent.parent

# Data paths
DATA_DIR = BASE_DIR / "data"
PROCESSED_DIR = DATA_DIR / "processed"

CLEANED_DATA_PATH = PROCESSED_DIR / "cleaned_data.csv"

# Model paths
MODEL_DIR = BASE_DIR / "model"
SIMILARITY_PATH = MODEL_DIR / "similarity.pkl"
MOVIES_PATH = MODEL_DIR / "movies.pkl"

# Recommender config
TOP_N = 5

# TMDB config
TMDB_API_KEY_CONFIG = os.environ.get("TMDB_API_KEY")
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

# if __name__ == "__main__":
#     print("TMDB_API_KEY:", TMDB_API_KEY_CONFIG)
