

def get_strike_val_call(value):
    # 16225
    # 16225 +80 = 17305

    new_val = (value) + 100
    if new_val % 50 < 25:
        strike_price = new_val - (new_val % 50)

    else:
        strike_price = new_val + (new_val % 50)

    return strike_price

def get_strike_val_put(value):

    new_val = (value) - 100
    if new_val % 50 < 25:
        strike_price = new_val - (new_val % 50)

    else:
        strike_price = new_val + (new_val % 50)

    return strike_price