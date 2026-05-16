# app.py

import streamlit as st
import pandas as pd
import joblib

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="DriveValue Nigeria",
    page_icon="🚗",
    layout="centered"
)

# -----------------------------------
# LOAD MODEL
# -----------------------------------

model = joblib.load("car_price_model.joblib")

# -----------------------------------
# MAKE -> MODEL DATA
# -----------------------------------

car_data = {
    'Acura': ['ILX', 'MDX', 'RDX', 'RL', 'TL', 'TSX', 'ZDX'],
    'Audi': ['A4', 'A6', 'A7', 'Q5', 'Q7'],
    'BMW': ['116i', '130i', '3 Series', '320i', '323i', '325i',
            '328i', '5 Series', '523i', '525i', '528i',
            '530i', '535i', '550i', '7 Series', 'X3', 'X5', 'X6'],
    'Honda': ['Accord', 'Civic', 'CR-V', 'Pilot', 'Odyssey'],
    'Hyundai': ['Accent', 'Elantra', 'Sonata', 'Tucson'],
    'Kia': ['Cerato', 'Optima', 'Picanto', 'Rio',
            'Sorento', 'Sportage'],
    'Lexus': ['ES', 'GX', 'IS', 'LX', 'RX', 'RX 350'],
    'Mercedes-Benz': ['C300', 'C350', 'CLA-Class',
                      'E350', 'GLK-Class', 'GLE-Class',
                      'S-Class'],
    'Nissan': ['Altima', 'Maxima', 'Murano',
               'Pathfinder', 'Rogue', 'Sentra',
               'X-Trail'],
    'Toyota': ['4-Runner', 'Avalon', 'Camry',
               'Corolla', 'Highlander', 'Hilux',
               'Land Cruiser', 'Land Cruiser Prado',
               'Matrix', 'Prius', 'RAV4',
               'Sienna', 'Tacoma', 'Tundra',
               'Venza', 'Yaris'],
    'Volkswagen': ['Golf', 'Jetta', 'Passat',
                   'Polo', 'Touareg']
}

# -----------------------------------
# TITLE
# -----------------------------------

st.title("🚗 DriveValue Nigeria")
st.write("Get an instant estimate of your car's market value.")

# -----------------------------------
# USER INPUTS
# -----------------------------------

make = st.selectbox(
    "🏢 Car Make",
    sorted(car_data.keys())
)

model_name = st.selectbox(
    "🚘 Car Model",
    sorted(car_data[make])
)

fuel_type = st.selectbox(
    "⛽ Fuel Type",
    ["Petrol", "Diesel"]
)

gear_type = st.selectbox(
    "⚙️ Transmission",
    ["Automatic", "Manual"]
)

condition = st.selectbox(
    "📌 Condition",
    ["Nigerian Used", "Foreign Used", "Brand New"]
)

year = st.number_input(
    "📅 Year of Manufacture",
    min_value=1990,
    max_value=2026,
    value=2018
)

mileage = st.number_input(
    "🛣 Mileage (km)",
    min_value=0,
    value=50000
)

engine_size = st.number_input(
    "🔧 Engine Size",
    min_value=0.8,
    max_value=8.0,
    value=2.0
)

# -----------------------------------
# PREDICTION
# -----------------------------------

if st.button("🚀 Predict Price"):

    input_data = pd.DataFrame([{
        'fuel type': fuel_type,
        'gear type': gear_type,
        'Make': make,
        'Model': model_name,
        'Year of manufacture': year,
        'Condition': condition,
        'Mileage': mileage,
        'Engine Size': engine_size
    }])

    # Predict directly
    prediction = model.predict(input_data)

    predicted_price = prediction[0]

    # Output
    st.success(
        f"💰 Estimated Price: ₦{predicted_price:,.0f}"
    )

    st.info(
        "⚠️ Prices are estimates and may vary based on market conditions."
    )
    st.success(f"💰 Estimated Price: ₦{prediction[0]:,.0f}")
