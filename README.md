# DriveValue Nigeria - Nigerian Car Price Predictor

This is a machine learning web application that predicts the market price of used cars in Nigeria. Users can input car details and instantly receive an estimated price in Naira.

The model is built using a Random Forest Regressor and includes SHAP (SHapley Additive exPlanations) for model explainability, helping users understand which features influence the predicted price.

---

## Project Overview

DriveValue Nigeria helps users:
- Estimate used car prices in Nigeria
- Understand key factors affecting car prices
- Get instant predictions using a trained ML model

---

## Features

- User-friendly web interface built with Streamlit
- Real-time car price prediction
- Machine learning model trained on Nigerian car data
- Model explainability using SHAP
- Handles categorical and numerical car features

---

## Machine Learning Model

- Algorithm: Random Forest Regressor
- Explainability: SHAP (SHapley Additive exPlanations)
- Task Type: Regression
- Target Variable: Car price (Naira)

---

## Project Workflow

### 1. Data Collection
Collected dataset of used cars in Nigeria.

### 2. Data Cleaning
- Removed missing and duplicate values
- Handled incorrect data types
- Processed inconsistent entries

### 3. Feature Engineering
- Encoded categorical variables using one-hot encoding
- Selected important features for prediction

### 4. Model Training
- Trained multiple models
- Selected Random Forest as best performer

### 5. Model Evaluation
- Evaluated using MAE, RMSE, and R² score

### 6. Model Explainability
- Used SHAP to interpret feature importance

---

## Installation

### Clone the repository
```bash
git clone https://github.com/your-username/drivevalue-nigeria.git
cd drivevalue-nigeria
