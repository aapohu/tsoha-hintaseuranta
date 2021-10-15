from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import queries as q

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

def add_user(username, password):
    db.session.execute(q.add_user, {"name":username, "password":password})
    db.session.commit()

def add_price(user, station, price1, price2, price3, price4):
    db.session.execute(q.add_price,{"station":station, "user":user, "price1":price1, "price2":price2, "price3":price3, "price4":price4})
    db.session.commit()

def add_station(name, address, city, postnr, road):
    db.session.execute(q.add_station, {"name":name, "address":address,"city":city, "postnr":postnr, "road":road})
    db.session.commit()

def hide_price(price_id):
    print("piilotetaan havainto", price_id)
    db.session.execute(q.hide_price,{"pid":price_id})
    db.session.commit()

def close_station(station_id):
    print("suljetaan asema",station_id)
    db.session.execute(q.close_station,{"stid":station_id})
    db.session.commit()

def ban_user(user_id):
    #prevents admin from being banned
    if user_id != 1:
        db.session.execute(q.ban_user,{"uid":user_id})
        print("pwned")
        db.session.commit()

def unban_user(user_id):
    db.session.execute(q.unban_user,{"uid":user_id})
    db.session.commit()

def get_stations():
    result = db.session.execute(q.get_stations)
    return result.fetchall()

def get_prices():
    result = db.session.execute(q.get_prices)
    return result.fetchall()

def get_all_prices():
    result = db.session.execute(q.get_all_prices)
    return result.fetchall()

def get_price(price_id):
    #get single price info for "/price/id" pages
    result = db.session.execute(q.get_one_price,{"pid":price_id})
    return result.fetchone()

def get_avg_today():
    #average price for today
    result = db.session.execute(q.get_avg_today)
    return result.fetchone()

def get_avg_daily():
    #average daily prices of all time
    result = db.session.execute(q.get_avg_daily)
    return result.fetchall()

def get_avg_monthly():
    #average daily prices of all time
    result = db.session.execute(q.get_avg_monthly)
    return result.fetchall()

def is_admin(username):
    result = db.session.execute(q.is_admin,{"username":username})
    value = result.fetchall()
    return value[0][0] == 1

def getuser(username):
    result = db.session.execute(q.get_user_id,{"username":username})
    value = result.fetchone()

    return value[0]

def is_user(username):
    result = db.session.execute(q.is_user,{"username":username})
    if result.fetchone()[0] == 1:
        return True
    return False

def banned(username):
    result = db.session.execute(q.is_banned,{"username":username})
    if result.fetchone()[0] == False:
        return True
    return False

def get_user_info(user_id):
    result = db.session.execute(q.get_user_info,{"id":user_id})
    return result.fetchone()

def getpassword(username):
    result = db.session.execute(q.get_password,{"username":username})
    value = result.fetchone()
    return value[0]

def postchatmessage(username, message):
    db.session.execute(q.post_chat_message,{"username":username, "message":message})
    db.session.commit()


def get_chat_messages():
    result = db.session.execute(q.get_chat_messages)
    return result

def get_requests():
    result = db.session.execute(q.get_requests)
    return result

def add_request(sender_id, message):
    db.session.execute(q.add_request,{"sender_id":sender_id, "message":message})
    db.session.commit()

def hide_request(request_id):
    db.session.execute(q.hide_request,{"request_id":request_id})
    db.session.commit()
    
def get_areas():
    results = db.session.execute(q.get_areas)
    return results.fetchall()

def get_roads():
    results = db.session.execute(q.get_roads)
    return results.fetchall()

def get_station_info(station_id):
    result = db.session.execute(q.get_station_info,{"station_id":station_id})
    return result.fetchone()

def get_station_prices(station_id):
    result = db.session.execute(q.get_station_prices,{"station_id":station_id})
    return result.fetchall()