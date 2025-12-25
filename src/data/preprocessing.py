import pandas as pd
import os

def drop_columns(df: pd.DataFrame, columns_to_drop: list) -> pd.DataFrame:
    """
    Given a pandas dataframe, drop the columns received
    
    :param df: Dataframe to drop columns from
    :type df: pd.DataFrame
    :param columns_to_drop: Columns to drop on the dataset
    :type columns_to_drop: list
    :return: Dataframe modified
    :rtype: DataFrame
    """

    # Drop columns received
    df = df.drop(columns_to_drop, axis=1)
    
    return df

def save_dataset(df:pd.DataFrame, filename: str):
    """
    Save a dataset into processed folder.
    
    :param df: Dataframe to save
    :type df: pd.DataFrame
    :param filename: File to save's name. Must include the extension (.csv)
    :type filename: str
    """
    # Folder to save the dataset
    folder_path = "../data/processed"

    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)
    df.to_csv(file_path, index=False)
