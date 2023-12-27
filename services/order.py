from login import *
import requests
from json import dumps

def place_order( quantity, type, order_type, symbol, product, validity, price=None, trigger_price=None, exchange='NSE'):
    try:
        #global kite

        url = "https://api.kite.trade/orders/regular"

        headers_data = {
            "X-Kite-Version" : "3",
            "Authorization" : f"token {api_key}:{access_token}"
        }
        
        order_data = {
            "tradingsymbol" : symbol,
            "exchange" : exchange,
            "transaction_type" : type,
            "order_type": order_type,
            "quantity" : quantity,
            "product" : product,
            "validity" : validity
        }

        if order_type == "LIMIT":
            order_data["price"] = price

        elif order_type == "SL" or order_type == "SL-M":
            order_data["trigger_price"] = trigger_price
        
        order_result = requests.post(url, headers=headers_data, data= dumps(order_data) )
        
        # order_id = kite.place_order(variety=kite.VARIETY_REGULAR, exchange=exchange, tradingsymbol=symbol,
        #                 transaction_type=type, quantity=quantity, product=product, order_type=order_type,
        #                 validity=validity)
        
        print("Order placed with order id - ", order_result["data"]["order_id"])

        # store order id details to modify order or cancel

    except Exception as e:
        print("Exception in placing order - ", e)

def ModifyOrder(order_id,price):  
    try:  
        # Modify order given order id

        url = f"https://api.kite.trade/orders/regular/{order_id}"

        headers_data = {
            "X-Kite-Version" : "3",
            "Authorization" : f"token {api_key}:{access_token}"
        }
        
        order_data = {
            "price" : price
        }

        modify_order_result = requests.put(url, headers=headers_data, data= dumps(order_data) )
        
        
        # kite.modify_order(order_id=order_id,
        #                 price=price,
        #                 trigger_price=price,
        #                 order_type=kite.ORDER_TYPE_SL,
        #                 variety=kite.VARIETY_REGULAR) 
    
    except Exception as e:
        print("Exception in modifying order - ", e)