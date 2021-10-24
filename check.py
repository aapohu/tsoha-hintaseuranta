
def check_length(text:str, max:int):
    if len(str(text)) > max:
        return False
    return True

def check_price(price:float):
    if price < 0.000:
        return False
    return True

def check_table(table):
    #replaces None values with 0
    return [[val if val is not None else 0 for val in row] for row in table]
    
def check_prices(p1,p2,p3,p4):
    prices=[p1,p2,p3,p4]
    if p1==p2==p3==p4:
        return False
    for price in prices:
        if not check_price(price):
            return False
    return True