from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import joblib
import pandas as pd
import os
from utils import (
    extended_forecast,
    parse_data_from_file,
    load_scaler_from_gcs,
    load_model_from_gcs,
    load_csv_from_gcs,
    load_from_gcs
)

app = Flask(__name__)
WINDOW_SIZE = 52  # 1 year
BUCKET_NAME = "finsight-ml-model"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Get stock and steps from request
    stock = str(data['stock']).upper()
    steps = int(data['steps'])

    # ===== UNCOMMENT UNTUK DOWNLOAD DARI GCS =====
    # model_path = f"stock_model/{stock}/model_saham.h5"
    # scaler_path = f"stock_model/{stock}/scaler.pkl"
    # csv_path = f"stock_model/{stock}/data_saham.csv"
    #
    # local_model_path = f"models/{stock}"
    # local_scaler_path = f"scalers/{stock}"
    # local_csv_path = f"csv/{stock}"

    # Check dirs
    # if not os.path.exists(local_model_path):
    #     os.makedirs(local_model_path)
    # if not os.path.exists(local_scaler_path):
    #     os.makedirs(local_scaler_path)
    # if not os.path.exists(local_csv_path):
    #     os.makedirs(local_csv_path)

    # model = load_model_from_gcs(BUCKET_NAME, model_path, local_model_path + "/model_saham.h5")
    # scaler = load_scaler_from_gcs(BUCKET_NAME, scaler_path, local_scaler_path + "/scaler.pkl")
    # load_csv_from_gcs(BUCKET_NAME, csv_path, local_csv_path + "/data_saham.csv")

    # model, scaler = load_from_gcs(BUCKET_NAME, paths={
    #     "model_path": model_path,
    #     "local_model_path": local_model_path + "/model_saham.h5",
    #     "scaler_path": scaler_path,
    #     "local_scaler_path": local_scaler_path +"/scaler.pkl",
    #     "csv_path": csv_path,
    #     "local_csv_path": local_csv_path + "/data_saham.csv"
    # })
    # ===== UNCOMMENT UNTUK DOWNLOAD DARI GCS =====

    # Load model and scaler based on the stock
    model = tf.keras.models.load_model(f"models/{stock}/model_saham.h5")
    scaler = joblib.load(f"scalers/{stock}/scaler.pkl")

    # Get the data
    # TIME, SERIES = parse_data_from_file(local_csv_path + "/data_saham.csv")
    TIME, SERIES = parse_data_from_file(f"csv/{stock}/data_saham.csv")
    SERIES = scaler.fit_transform(SERIES.reshape(-1, 1)).flatten()

    # Predict
    predicted_values = extended_forecast(model, SERIES, WINDOW_SIZE, forecast_steps=steps)

    # Convert to actual price
    predicted_actual = scaler.inverse_transform([predicted_values])

    # Return json (array)
    return jsonify({
        'predictions': predicted_actual.flatten().tolist()
    })

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True, port=3000)