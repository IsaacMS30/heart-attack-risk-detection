import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_age_hist(age_no_risk, age_risk):
    plt.figure(figsize=(10, 6))
    plt.hist([age_no_risk, age_risk])

    plt.title("Heart Attack Risk by Age")
    plt.xlabel("Age")
    plt.ylabel("Total patients")
    plt.legend(["No Risk", "Risk"])

    plt.show()
    plt.close()


def plot_risk_vs_history(df: pd.DataFrame):
    ct = pd.crosstab(df["Heart Attack Risk"], df["Family History"])
    ax = ct.plot(kind="bar")

    ax.set_title("Heart Attack Rate by Family History")
    ax.set_xlabel("Heart Attack Risk")
    ax.set_ylabel("Total patients")
    ax.set_xticklabels(["No disease", "Disease"], rotation=0)
    ax.legend(["No History", "History"])

    plt.show()
    plt.close()


def plot_bmi_vs_chol(df: pd.DataFrame):
    plt.figure(figsize=(10,6))
    plt.scatter(df.Cholesterol[df["Heart Attack Risk"] == 0], df.BMI[df["Heart Attack Risk"] == 0])
    plt.scatter(df.Cholesterol[df["Heart Attack Risk"] == 1], df.BMI[df["Heart Attack Risk"] == 1])

    plt.title("BMI vs Cholesterol")
    plt.xlabel("Cholesterol level")
    plt.ylabel("BMI")
    plt.legend(["No risk", "Risk"])

    plt.show()
    plt.close()


def plot_corr_matrix(df: pd.DataFrame):
    cmatrix = df.corr(numeric_only=True)

    plt.figure(figsize=(15, 10))
    sns.heatmap(cmatrix, cmap="Reds", annot=True, fmt=".2f")
    plt.title("Correlation Matrix")

    plt.show()
    plt.close()