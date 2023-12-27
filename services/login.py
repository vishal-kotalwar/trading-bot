
from kiteconnect import KiteConnect

access_key = ""
request_token = ""
api_secret = ""
api_key = ""
access_token = ""
kite = KiteConnect(api_key= "")

def generate_session():
    global kite

    data = kite.generate_session(request_token, api_secret=api_secret)

    kite.set_access_token(data["access_token"])