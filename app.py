 import streamlit as st
 import requests
 # Set Streamlit app page configuration
 st.set_page_config(page_title="Weather Predictor", page_icon="￿ ")
 # Title and instructions
 st.title("￿ Weather Prediction App")
 st.write("Enter weather conditions to predict whether it will rain.")
 # Input fields
 temperature = st.number_input("￿ Temperature (°C)", value=25.0)
 humidity = st.number_input("￿ Humidity (%)", value=60.0)
 wind = st.number_input("￿ Wind Speed (km/h)", value=10.0)
if st.button("￿ Predict Weather"):
 # ￿ Correct Modelbit API endpoint
 api_url = "https://bamsrad.us-east-2.aws.modelbit.com/v1/weather_api/latest"
 # ￿ Use API Key from secrets.toml securely
 headers = {
 "Authorization": f"Bearer {st.secrets['miWvFVjCyK:msxl+Byhl/
 ↪EZcKSSS4ZAZic1k6BSR1KMkmllEowmBnyGY=']}",
 "Content-Type": "application/json"
 }
 # Request payload with inputs
 payload = {
 "temperature": temperature,
 "humidity": humidity,
 "wind": wind
 }
 # Request and response handling
 try:
 response = requests.post(api_url, json=payload, headers=headers)
 response.raise_for_status()
 result = response.json()
 prediction = result.get("result", "No result returned.")
 st.success(f"￿ Prediction: **{prediction}**")
     except requests.exceptions.HTTPError as errh:
 st.error(f"￿ HTTP Error: {errh}")
 except requests.exceptions.ConnectionError as errc:
 st.error(f"￿ Connection Error: {errc}")
 except requests.exceptions.Timeout as errt:
 st.error(f"￿ Timeout Error: {errt}")
 except requests.exceptions.RequestException as err:
 st.error(f"￿ Something went wrong: {err}")
