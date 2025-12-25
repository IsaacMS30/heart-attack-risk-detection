import pandas as pd

def load_dataset(dataset_path: str) -> pd.DataFrame:
    """
    Load dataset from path
    
    :param dataset_path: Path where the dataset is located
    :type dataset_path: str
    :return: A pandas Dataframe containing the dataset
    :rtype: DataFrame
    """
    return pd.read_csv(dataset_path)
