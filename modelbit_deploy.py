import modelbit
import joblib

model = joblib.load("weather_model.pkl")
le = joblib.load("label_encoder.pkl")

mb = modelbit.login()

@mb.deploy
def weather_api(temperature: float, humidity: float, wind: float) -> str:
    prediction = model.predict([[temperature, humidity, wind]])
    return le.inverse_transform(prediction)[0]
