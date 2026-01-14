import pickle
from pathlib import Path


def save_pickle(obj, path: Path):
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "wb") as f:
            pickle.dump(obj, f)
    except Exception as e:
        raise RuntimeError(f"Failed to save pickle: {e}")


def load_pickle(path: Path):
    try:
        if not path.exists():
            raise FileNotFoundError(f"Pickle file not found: {path}")

        with open(path, "rb") as f:
            return pickle.load(f)

    except Exception as e:
        raise RuntimeError(f"Failed to load pickle: {e}")
