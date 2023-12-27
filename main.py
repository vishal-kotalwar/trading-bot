

from datetime import datetime, timedelta
import pandas as pd
from services.login import *
from services.order import place_order
from services.position import *
from services.candle_data import *
from services.utils import *

# from kiteconnect import KiteConnect

# access_key = ""
# request_token = ""
# api_secret = ""
# kite = KiteConnect(api_key= "")

# data = kite.generate_session(request_token, api_secret=api_secret)

# kite.set_access_token(data["access_token"])

if __name__ == "__main__":
    #global kite

    retry_pos_df , retry_order_df = 10

    try:
        pos_df = pd.DataFrame(kite.positions()["day"])

        curr_time = datetime.now() + timedelta(hours=5.5)
        curr_date = curr_time.date()

        if datetime.time(9,44) < curr_time < datetime.time(10, 00):
            pos_data =  get_net_position()

            if len(pos_data) > 0:
                print("No need to create another position !!")

            else:
                ohlc_data = get_candle_data("15minute", "", f"{curr_date} 09:30:00", f"{curr_date} 09:45:00")
                high_pt = ohlc_data[2]
                low_pt = ohlc_data[3]

                call_strike_val = get_strike_val_call(high_pt)
                put_strike_val = get_strike_val_put(low_pt)

                # Get instrument symbol for strike values

                call_ohlc_data = get_candle_data("15minute", "", f"{curr_date} 09:30:00", f"{curr_date} 09:45:00")
                put_ohlc_data = get_candle_data("15minute", "", f"{curr_date} 09:30:00", f"{curr_date} 09:45:00")
                
                call_strike_price = call_ohlc_data[2] - "0.50"
                call_trigger_price = call_ohlc_data[1] + "0.50"
                put_strike_price = put_ohlc_data[2] - "0.50"
                put_trigger_price = put_ohlc_data[1] + "0.50"


                sell_call_order_id = place_order("1", "SELL", "LIMIT", "", "MIS", "DAY", call_strike_price )
                sl_call_order_id = place_order("1", "BUY", "SL-M", "", "MIS", "DAY", "", call_trigger_price)

                sell_put_order_id = place_order("1", "SELL", "LIMIT", "", "MIS", "DAY", put_strike_price)
                sl_put_order_id = place_order("1", "BUY", "SL-M", "", "MIS", "DAY", "", put_trigger_price)

    except Exception as e:
        print()
        retry_pos_df +=1