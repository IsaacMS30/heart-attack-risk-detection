import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_age_hist(age_no_risk, age_risk):
    plt.figure(figsize=(10, 6))
    plt.hist([age_no_risk, age_risk])

    plt.title("Heart Attack Disease by Age")
    plt.xlabel("Age")
    plt.ylabel("Total patients")
    plt.legend(["No Disease", "Disease"])

    plt.show()
    plt.close()


def plot_disease_vs_gender(df: pd.DataFrame):
    ct = pd.crosstab(df["target"], df["gender"])
    ax = ct.plot(kind="bar")

    ax.set_title("Heart Attack Disease by Gender")
    ax.set_xlabel("Heart Attack Disease")
    ax.set_ylabel("Total patients")
    ax.set_xticklabels(["No disease", "Disease"], rotation=0)
    ax.legend(["Female", "Male"])

    plt.show()
    plt.close()


def plot_hr_vs_chol(df: pd.DataFrame):
    plt.figure(figsize=(10,6))
    plt.scatter(df.serumcholestrol[df["target"] == 0], df.maxheartrate[df["target"] == 0])
    plt.scatter(df.serumcholestrol[df["target"] == 1], df.maxheartrate[df["target"] == 1])

    plt.title("Max Heart Rate vs Cholesterol")
    plt.xlabel("Cholesterol level")
    plt.ylabel("Max Heart Rate")
    plt.legend(["No disease", "Disease"])

    plt.show()
    plt.close()


def plot_corr_matrix(df: pd.DataFrame):
    cmatrix = df.corr(numeric_only=True)

    plt.figure(figsize=(15, 10))
    sns.heatmap(cmatrix, cmap="Reds", annot=True, fmt=".2f")
    plt.title("Correlation Matrix")

    plt.show()
    plt.close()