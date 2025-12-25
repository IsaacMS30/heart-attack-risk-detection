import pandas as pd
from typing import Tuple

def split_features(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Split a dataframe into X (features) and y (labels).
    
    :param df: Dataframe to split
    :type df: pd.Dataframe
    """
    X = df.drop("target", axis=1)
    y = df["target"]

    return X, y