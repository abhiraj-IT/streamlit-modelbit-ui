from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import modelbit

# Load your trained model and encoder
model = joblib.load("weather_model.pkl")
le = joblib.load("label_encoder.pkl")

# Login to Modelbit
mb = modelbit.login()

# Define pure prediction logic
def predict_weather(temperature, humidity, wind):
    input_data = [[temperature, humidity, wind]]
    prediction = model.predict(input_data)
    return le.inverse_transform(prediction)[0]

# Deploy the model as API
@mb.deploy
def weather_api(temperature: float, humidity: float, wind: float) -> str:
    return predict_weather(temperature, humidity, wind)

print("✅ Model deployed!")

