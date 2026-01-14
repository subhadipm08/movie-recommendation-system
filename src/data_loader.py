import pandas as pd
from pathlib import Path


def load_csv(path: Path) -> pd.DataFrame:
    """
    Load a CSV file safely.
    """
    try:
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        df = pd.read_csv(path)

        if df.empty:
            raise ValueError("Loaded DataFrame is empty")

        return df

    except Exception as e:
        raise RuntimeError(f"Failed to load CSV: {e}")

