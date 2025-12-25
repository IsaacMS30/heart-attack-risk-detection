import pandas as pd

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
    df = df.drop(columns_to_drop, axis=1)
    
    return df
