from login import *
import requests



def get_net_position():

    url = "https://api.kite.trade/portfolio/positions"

    header_data = {
        "X-Kite-Version" : "3",
        "Authorization" : f"token {api_key}:{access_token}"
    }

    pos_data = requests.get(url, headers=header_data)
    print("Positions data -- ", pos_data["data"]["net"])
    if len(pos_data["data"]["net"]) > 0:
        print("Currently there are net position available.")
    return  pos_data["data"]["net"]