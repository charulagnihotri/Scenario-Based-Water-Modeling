import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import os

# Define the 10 scenarios with descriptions and affected parameters
scenarios = {
    "Algal Bloom": {
        "description": "Algal bloom caused by nutrient overload alters water quality.",
        "affected_params": {
            "Dissolved Oxygen": "-50%",
            "Biochemical Oxygen Demand": "+40%",
            "Nitrate": "-25%",
            "pH": "±15% fluctuations"
        }
    },
    "Introduction of New Wastewater Treatment Plants": {
        "description": "Installation of new wastewater treatment plants reduces pollution.",
        "affected_params": {
            "Biochemical Oxygen Demand": "-30%",
            "Total Coliform": "-50%",
            "Fecal Coliform": "-50%",
            "Dissolved Oxygen": "+30%"
        }
    },
    "Seasonal Temperature Variations": {
        "description": "Seasonal temperature changes impact water parameters.",
        "affected_params": {
            "Temperature": "±20% seasonal variation",
            "Dissolved Oxygen": "-30% (inverse relationship in summer)",
            "Biochemical Oxygen Demand": "+10%"
        }
    },
    "Industrial Discharge Incident": {
        "description": "Industrial effluent discharge affects river water quality.",
        "affected_params": {
            "Biochemical Oxygen Demand": "+50%",
            "Conductivity": "+60%",
            "Dissolved Oxygen": "-40%",
            "Nitrate": "+30%"
        }
    },
    "Festival or Pilgrimage Event": {
        "description": "Large religious events impact water quality due to high crowd and waste.",
        "affected_params": {
            "Biochemical Oxygen Demand": "+40%",
            "Total Coliform": "+60%",
            "Fecal Coliform": "+50%",
            "Fecal Streptococci": "+50%",
            "Turbidity": "+40%",
            "Dissolved Oxygen": "-25%"
        }
    }
}
# Streamlit Sidebar for City Selection
cities = [
    "Kanpur", "Kannauj", "Varanasi", "Devprayag", "Rudraprayag", "Haridwar",
    "Gulabi ghat", "Ghazipur", "Bhagalpur", "Howrah", "Prayagraj", "Dakshineshwar"
]
city = st.sidebar.selectbox("Select a City", cities)

# Streamlit Sidebar for Scenario Selection
scenario = st.sidebar.selectbox("Select a Scenario", list(scenarios.keys()))

# Display Selected Scenario and Its Details
st.title(f"Water Quality Forecasting for {city}")
st.header(f"Scenario: {scenario}")
st.write(scenarios[scenario]["description"])

# Streamlit Dropdown for Parameter Selection
selected_param = st.selectbox("Select a Parameter", list(scenarios[scenario]["affected_params"].keys()))

# Path Construction for Forecast CSV, Visualization Image, and Actual vs Predicted Graph
forecast_file = f"{city}/forecasts/{scenario}_{selected_param}_forecast.csv"
visualization_file = f"{city}/visualizations/{scenario}_{selected_param}_forecast.png"
actual_vs_predicted_file = f"{city}/visualizations/{scenario}_{selected_param}_predictions.png"

# Check if forecast files exist and display the forecast data
if os.path.exists(forecast_file):
    # Load the Forecast Data from the CSV file
    forecast_data = pd.read_csv(forecast_file)
    
    # Display Forecast Data as a Table
    st.subheader(f"Forecast Data for {selected_param}")
    st.write(forecast_data)
else:
    st.warning(f"No forecast data available for {selected_param} in {scenario}.")

if os.path.exists(visualization_file):
    # Display Forecast Visualization Image
    st.subheader(f"Forecast Visualization for {selected_param}")
    st.image(visualization_file, caption=f"{selected_param} Forecast Visualization")
else:
    st.warning(f"No forecast visualization available for {selected_param} in {scenario}.")

# Check if Actual vs Predicted graph file exists and display it
if os.path.exists(actual_vs_predicted_file):
    # Display Actual vs Predicted Visualization Image
    st.subheader(f"Actual vs Predicted Visualization for {selected_param}")
    st.image(actual_vs_predicted_file, caption=f"{selected_param} Actual vs Predicted Graph")
else:
    st.warning(f"No Actual vs Predicted graph available for {selected_param} in {scenario}.")