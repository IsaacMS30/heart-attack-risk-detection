import pandas as pd

def load_dataset(dataset_path: str) -> pd.DataFrame:
    return pd.read_csv(dataset_path)