
def check_length(text:str, max:int):
    if len(str(text)) > max:
        return False
    return True

def check_price(price:float):
    if price < 0.000:
        return False
    return True




