# app.py 
from dotenv import load_dotenv
load_dotenv()


import streamlit as st
import requests
import os

# === Streamlit UI ===
st.set_page_config(page_title="🌦️ Weather Predictor", layout="centered")
st.title("🌤️ Predict Rain or No Rain Using Weather Conditions")

# Input fields for web UI
temperature = st.number_input("🌡️ Temperature (°C):", min_value=-30.0, max_value=60.0, step=0.1)
humidity = st.number_input("💧 Humidity (%):", min_value=0.0, max_value=100.0, step=0.1)
wind = st.number_input("🌬️ Wind Speed (km/h):", min_value=0.0, max_value=300.0, step=0.1)

if st.button("🔍 Predict"):
    with st.spinner("Contacting the ML model on Modelbit..."):
        api_url = "https://api.modelbit.com/YOUR_USERNAME/weather_api"  # replace with your real Modelbit endpoint

        headers = {
            "Authorization": f"Bearer {os.getenv('API_KEY')}",
            "Content-Type": "application/json"
        }

        payload = {
            "temperature": temperature,
            "humidity": humidity,
            "wind": wind
        }

        try:
            response = requests.post(api_url, headers=headers, json=payload)
            if response.status_code == 200:
                result = response.json()  # If API returns plain string, use response.text instead
                st.success(f"🌧️ Prediction: {result}")
            else:
                st.error("❌ API call failed!")
                st.write("Status Code:", response.status_code)
                st.write(response.text)
        except Exception as e:
            st.error("⚠️ An error occurred while calling the API.")
            st.write(e)

# === Optional Local Prediction Logic ===

# If you want to test locally without API (for CLI testing)
def predict_weather(temperature: float, humidity: float, wind: float) -> str:
    import joblib

    try:
        model = joblib.load("weather_model.pkl")
        le = joblib.load("label_encoder.pkl")
        input_data = [[temperature, humidity, wind]]
        prediction = model.predict(input_data)
        return le.inverse_transform(prediction)[0]
    except Exception as e:
        return f"Error loading model: {e}"

# Step 4: Local testing via CLI (won't run in Streamlit Cloud)
def local_test():
    print("Enter weather parameters to predict rain or no rain:")
    try:
        temperature = float(input("Temperature (°C): "))
        humidity = float(input("Humidity (%): "))
        wind = float(input("Wind Speed (km/h): "))
    except ValueError:
        print("Invalid input! Please enter numerical values.")
        return
    
    result = predict_weather(temperature, humidity, wind)
    print(f"Prediction: {result}")

if __name__ == "__main__":
    local_test()
