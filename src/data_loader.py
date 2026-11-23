"""Load the raw and processed datasets."""
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = PROJECT_ROOT / "data" / "raw" / "insurance.csv"
PROCESSED_PATH = PROJECT_ROOT / "data" / "processed" / "insurance_clean.csv"
MODEL_PATH = PROJECT_ROOT / "models" / "best_model.joblib"

def load_raw_data(path=RAW_PATH):
    if not Path(path).exists():
        raise FileNotFoundError(f"Dataset not found at {path}")
    return pd.read_csv(path)