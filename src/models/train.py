import os

import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from typing import Tuple

def split_train_test(X: pd.DataFrame, y: pd.Series, test_size: float = 0.2
                     , stratify: bool = True, random_state: int = 42) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Split dataframe into training and testing. Divides it into feaures and labels for each.
    Also, saves each training and testing datasets into files.
    
    :param X: Features matrix
    :type X: pd.DataFrame
    :param y: Labels series
    :type y: pd.Series
    :param test_size: Proportion of dataset to include in test set
    :type test_size: float
    :param stratify: Whether wants to stratify splitting or not
    :type stratify: bool
    :param random_state: Random state to apply
    :type random_state: int
    :return: Data divided
    :rtype: Tuple[DataFrame, DataFrame, Series[Any], Series[Any]]
    """

    # Verify if we need to stratify
    use_stratify = y if stratify else None

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size,
                                                        random_state=random_state, stratify=use_stratify)
    
    # Now, let's save our training and testing set
    train_set = pd.concat([X_train, y_train], axis=1)
    test_set = pd.concat([X_test, y_test], axis=1)

    os.makedirs("../data/processed", exist_ok=True)
    train_set.to_csv("../data/processed/train.csv", index=False)
    test_set.to_csv("../data/processed/test.csv", index=False)

    return X_train, X_test, y_train, y_test

def perform_cross_validation(models: dict, X: pd.DataFrame, y: pd.Series, scoring:str = "accuracy",
                             cv: int = 5, verbose: int = 1) -> dict:
    """
    Performs cross-validation on the models received.
    
    :param models: Models to perform cross-validation on
    :type models: dict
    :param X: Features matrix
    :type X: pd.DataFrame
    :param y: Labels series
    :type y: pd.Series
    :param scoring: Metric to evaluate in cross-validation.
    :type scoring: str
    :param cv: Number of folds to evaluate
    :type cv: int
    :param verbose: Verbose level
    :type verbose: int
    :return: Dictionary with mean performance for each fold of the cross-validation
    :rtype: Dict
    """
    
    scorings = {}
    for key, model in models.items():
        current_score = cross_val_score(model, X, y, scoring=scoring, cv=cv, verbose=verbose, n_jobs=-1)
        scorings[key] = current_score
    
    return scorings