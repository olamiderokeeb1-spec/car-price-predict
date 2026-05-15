import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import streamlit as st
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import (
    LinearRegression,
    Ridge,
    Lasso
)

from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import RandomForestRegressor

from sklearn.neighbors import KNeighborsRegressor

from xgboost import XGBRegressor
joblib.dump(rf, 'models/car_price_model.joblib')

joblib.dump(scaler, 'models/car_price_scaler.joblib')

joblib.dump(
    X_r.columns.tolist(),
    'models/car_price_columns.joblib'
)
model = joblib.load(
    'models/car_price_model.pkl'
)

scaler = joblib.load(
    'models/car_price_scaler.pkl'
)

columns = joblib.load(
    'models/car_price_columns.pkl'
)
st.title("Car Price Prediction App")
mileage = st.number_input("Mileage")
fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel"]
)
if st.button("Predict Price"):
  st.success(
    f"Estimated Price: ₦{prediction[0]:,.0f}"
)
