from login import *
import requests

def get_candle_data(interval, instrument_token, start_time, end_time):

    url = f"https://api.kite.trade/instruments/historical/{instrument_token}/{interval}?from={start_time}&to={end_time}"

    header_data = {
        "X-Kite-Version" : "3",
        "Authorization" : f"token {api_key}:{access_token}"
    }

    response_data = requests.get(url, headers=header_data)
    ohlc_data = response_data["data"]["candles"][0]

    return ohlc_data