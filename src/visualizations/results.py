import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.metrics import roc_curve, roc_auc_score

def plot_metrics(metrics: dict):
    """
    Plot a bar graph comparing each metric (accuracy, precisin, recall and auc) from each model.
    
    :param metrics: Dictionary containing one entry for each model. Each entry has one entry for each metric
    :type metrics: dict
    """
    metrics_names = list(next(iter(metrics.values())).keys())
    models_names = list(metrics.keys())

    values = {model: [metrics[model][metric] for metric in metrics_names] for model in models_names}

    x = np.arange(len(metrics_names))
    width = 0.25 

    fig, ax = plt.subplots(figsize=(10,6))

    for i, model in enumerate(models_names):
        bars = ax.bar(x + i*width, values[model], width, label=model)
        ax.bar_label(bars, fmt="%.2f", padding=3)

    ax.set_xticks(x + width)
    ax.set_xticklabels(metrics_names)
    ax.set_ylabel("Score")
    ax.set_title("Metrics comparison for each model")
    ax.legend()
    plt.show()

def plot_auc_curve(models: dict, X:pd.DataFrame, y: pd.Series):
    """
    Plot ROC curve for each model.
    
    :param models: Models to plot
    :type models: dict
    :param X: Feature matrix
    :type X: pd.DataFrame
    :param y: Labels Dataframe
    :type y: pd.Series
    """
    for name, model in models.items():
        y_preds = model.predict(X)
        fpr, tpr, thresh = roc_curve(y, y_preds)
        auc = roc_auc_score(y, y_preds)
        plt.plot(fpr,tpr,label=f"{name} AUC = {auc:.2f}")

    plt.title("ROC curves for each model")
    plt.xlabel("False positive rate")
    plt.ylabel("True positive rate")
    plt.legend()

