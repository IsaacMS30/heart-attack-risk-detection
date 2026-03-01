# 🫀 Heart Attack Risk Detection

This project builds and evaluates multiple machine learning models to predict the risk of heart disease based on patient medical attributes.

The goal is to compare different algorithms, analyze their performance, and select the most suitable model for deployment.


## 🚀 Deployment

The best-performing model was serialized using joblib and deployed through a FastAPI application.

The API is containerized with Docker and deployed on Render.

You can find the process and API link here: https://github.com/IsaacMS30/ml-model-containerization


## 📊 Dataset

The dataset contains over a 1000 patient medical records, with information such as age, blood pressure, cholesterol levels, and other cardiovascular indicators.

Tha Target Variable (binary) is called Classification. It's values: 0 (Absence of Heart Disease), 1 (Presence of Heart Disease)

Source:
https://www.kaggle.com/datasets/jocelyndumlao/cardiovascular-disease-dataset/data


## 🧠 Models Implemented

The following algorithms were trained and evaluated:

- K-Nearest Neighbors (KNN)
- Random Forest
- Logistic Regression


## 📈 Model Evaluation

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

The Random Forest model achieved the best overall performance and was selected as the final model for deployment.


## ⚙️ Workflow

1. Data preprocessing (handling missing values, feature scaling)
2. Exploratory data analysis
3. Model training and validation
4. Performance comparison
5. Model serialization using joblib


## 🛠 Technologies

- Python
- Scikit-learn
- Pandas
- NumPy
