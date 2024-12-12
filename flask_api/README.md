# Flask API
This project is a Flask API to serve machine learning model.
## Features
- Predict stock prices based on the ticker and the steps.
- Give some recommendation stocks based on user profile risks.

## Prerequisites
- Python 3.10

## Setup
1. Clone the repository:
```commandline
git clone https://github.com/WhoIsLiLY/finsight-ML
```
2. Install dependencies
```commandline
cd flash_api
pip install -r requirements.txt
```
3. Start the server
```commandline
python3 index.py
```

## Usage
This project provides 2 __endpoints__:
- __GET /predict__: Give stock prices prediction and percentage changes.
- __GET /riskprofile__: Give some stocks recommendation based on profile risk.

## File Structure
- `index.py`: The main entry point of the application, which setup the Flask server and defines the API endpoints.
- `utils.py`: Initialize the helper function for forecasting stock prices.
- `recommendation_k_means.py`: Initialize Recommender System Class using K-Means.
- `models/`: The directory for stock models.
- `csv/`: The directory for stock data.
- `scalers/`: The directory for scaler.

## Dependencies
- `tensorflow`: Machine Learning library.
- `keras`: Backend API for Machine Learning.
- `numpy`: Library for mathematics calculation.
- `pandas`: Library for manipulation and analysis data.
- `matplotlib`: Library for data visualization.
- `joblib`: Library for saving python object into file.
- `scikit-learn`: Machine Learning library.
- `flask`: Web Framework for Python.
- `yfinance`: Stock library from Yahoo Finance.
- `ta`: Technical Analysis library to do feature engineering from financial time series datasets.
