
from datetime import date, datetime
from time import sleep
from services.data_utils import *

def check_order_logic():
    try:
        while True:

            current_time = datetime.now().strftime("%H:%M")
            if current_time != "09:45":
                sleep(60)
                continue

            start_ts = datetime.now().strftime("%Y-%m-%D") + " 09:45:00"
            end_ts = datetime.now().strftime("%Y-%m-%D") + " 10:00:00"
            data_dump = fetchOHLC("NIFTY", "15minute", start_ts, end_ts)

            

    except Exception as e:
        print("Exception occured while checking logic for creating order")
