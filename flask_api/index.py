from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import joblib
import pandas as pd
from utils import extended_forecast, parse_data_from_file

app = Flask(__name__)
WINDOW_SIZE = 4

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    stock = str(data['stock']).upper()
    model = tf.keras.models.load_model(f"../stock_model/{stock}/model_saham.h5")
    scaler = joblib.load(f"../stock_model/{stock}/scaler.pkl")
    TIME, SERIES = parse_data_from_file(f"../stock_model/{stock}/data_saham.csv")
    SERIES = scaler.fit_transform(SERIES.reshape(-1, 1)).flatten()
    # return "MASUK"
    predicted_values = extended_forecast(model, SERIES, WINDOW_SIZE, forecast_steps=1)
    predicted_actual = scaler.inverse_transform([predicted_values])
    return jsonify({
        'predictions': predicted_actual.flatten().tolist()
    })

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True, port=3000)