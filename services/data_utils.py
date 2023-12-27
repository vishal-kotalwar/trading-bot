#from kiteconnect import KiteConnect

import datetime as dt
import pandas as pd

from services.login import *

import requests

#get dump of all NSE instruments
instrument_dump = kite.instruments("NSE")
instrument_df = pd.DataFrame(instrument_dump)


def fetchOHLC(ticker,interval,start_ts, end_ts, continue_flag):
    """extracts historical data and outputs in the form of dataframe"""
    instrument = instrumentLookup(instrument_df,ticker)
    data = pd.DataFrame(kite.historical_data(instrument,start_ts, end_ts,interval, continuous=continue_flag))
    data.set_index("date",inplace=True)
    return data

def instrumentLookup(instrument_df,symbol):
    """Looks up instrument token for a given script from instrument dump"""
    try:
        return instrument_df[instrument_df.tradingsymbol==symbol].instrument_token.values[0]
    except:
        return -1


def fetch_instrument_dump():
    url = "https://api.kite.trade/instruments"

    header_data = {
        "X-Kite-Version" : "3",
        "Authorization" : f"token {api_key}:{access_token}"
    }

    csv_dump_res = requests.get(url, headers=header_data)
    df = pd.DataFrame(data=csv_dump_res)
