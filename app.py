import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.set_page_config(layout="wide")
st.title("🇮🇳 Indian Real Estate Price Prediction Dashboard")
st.write("Enter the layout structural dimensions to compute real-time property values.")

# Setup simple interactive UI inputs
col1, col2, col3 = st.columns(3)

with col1:
    city = st.selectbox("Select Target City", ['Mumbai', 'Delhi', 'Bangalore', 'Pune', 'Hyderabad', 'Jaipur', 'Chennai'])
    sqft = st.number_input("Square Footage (Area)", min_value=400, max_value=8000, value=1200)
    bedrooms = st.slider("Number of Bedrooms", 1, 5, 2)

with col2:
    bathrooms = st.slider("Number of Bathrooms", 1, 6, 2)
    age = st.slider("Property Age (Years)", 0, 30, 5)
    furnishing = st.selectbox("Furnishing State", ['Unfurnished', 'Semi-Furnished', 'Fully Furnished'])

with col3:
    metro_dist = st.slider("Distance to Metro Station (KM)", 0.2, 15.0, 2.5)
    school_dist = st.slider("Distance to School (KM)", 0.5, 8.0, 1.2)
    hospital_dist = st.slider("Distance to Hospital (KM)", 0.5, 10.0, 1.8)

# Calculate dynamic simulated rule outputs to match linear behavior
city_multipliers = {'Mumbai': 25000, 'Delhi': 18000, 'Bangalore': 15000, 'Pune': 12000, 'Hyderabad': 11000, 'Jaipur': 8000, 'Chennai': 11000}
base_rate = city_multipliers[city]

predicted_price = (sqft * base_rate) + (bedrooms * 500000) + (bathrooms * 200000) - (age * 40000)
if furnishing == 'Fully Furnished': predicted_price += 300000
elif furnishing == 'Semi-Furnished': predicted_price += 150000

st.markdown("---")
st.subheader("Predicted Property Market Valuation")
st.metric(label="Estimated Price (INR)", value=f"₹{predicted_price:,.2f}")
