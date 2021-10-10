#from re import S
from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

def add_user(username, password):
    sql = "INSERT INTO users (username, password, joindate, visible) VALUES (:name, :password, NOW(), TRUE);"
    db.session.execute(sql, {"name":username, "password":password})
    db.session.commit()
    

def add_price(user, station, price1, price2, price3, price4):
    sql = "INSERT INTO prices (station_id, user_id, time, visible, type1_price, type2_price, type3_price, type4_price) VALUES (:station, :user, NOW(), TRUE, :price1, :price2, :price3, :price4);"
    db.session.execute(sql,{"station":station, "user":user, "price1":price1, "price2":price2, "price3":price3, "price4":price4})
    db.session.commit()

def addstation(name, address, city, postnr, road):
    sql = "INSERT INTO stations (station_name, addr, city, postnr, road, operational, visible) VALUES (:name, :address, :city, :postnr, :road, TRUE, TRUE);"
    db.session.execute(sql, {"name":name, "address":address,"city":city, "postnr":postnr, "road":road})
    db.session.commit()

def hideprice(price_id):
    sql = "UPDATE prices SET visible=FALSE WHERE id=:pid;"
    db.session.execute(sql,{"pid":price_id})
    db.session.commit()

def close_station(station_id):
    print("suljetaan asema",station_id)
    sql = "UPDATE stations SET operational = FALSE WHERE id=:stid;"
    db.session.execute(sql,{"stid":station_id})
    db.session.commit()

def ban_user(user_id):
    sql = "UPDATE users SET visible = FALSE WHERE id=:uid;"
    db.session.execute(sql,{"uid":user_id})
    print("pwned")
    db.session.commit()

def unban_user(user_id):
    sql = "UPDATE users SET visible = TRUE WHERE id=:uid;"
    db.session.execute(sql,{"uid":user_id})
    print("poistetaan bannit")
    db.session.commit()


def get_stations():
    sql = "SELECT * FROM stations WHERE operational = TRUE;"
    result = db.session.execute(sql)
    return result.fetchall()

def getprices():
    sql2 = "SELECT DISTINCT ON (S.station_name) S.station_name, S.id, P.type1_price, P.type2_price, P.type3_price, P.type4_price, P.time \
            FROM prices P, stations S \
            WHERE S.id = P.station_id \
            ORDER BY S.station_name, time DESC;"
    result = db.session.execute(sql2)
    return result.fetchall()

def get_all_prices():
    sql = "SELECT S.station_name, S.id, P.type1_price, P.type2_price, P.type3_price, P.type4_price, P.time\
           FROM prices P, stations S\
           WHERE S.id = P.station_id\
           ORDER BY time DESC LIMIT 20;"
    result = db.session.execute(sql)
    return result.fetchall()

def avg_prices_today():
    #average price for today
    sql = "SELECT ROUND(AVG(type1_price)::numeric,3), ROUND(AVG(type2_price)::numeric,3), ROUND(AVG(type3_price)::numeric,3), ROUND(AVG(type4_price)::numeric,3) \
            FROM prices \
            WHERE date_trunc('day', time) = CURRENT_DATE;"
    result = db.session.execute(sql)
    return result.fetchall()

def avg_prices_oat():
    #average daily prices of all time
    sql = "SELECT ROUND(AVG(type1_price)::numeric,3) AS type1_avg, ROUND(AVG(type2_price)::numeric,3) AS type2_avg, ROUND(AVG(type3_price)::numeric,3) AS type3_avg, ROUND(AVG(type4_price)::numeric,3) AS type4_avg, date_trunc('day', time) \
            FROM prices \
            GROUP BY date_trunc('day', time);"
    result = db.session.execute(sql)
    return result.fetchall()

def is_admin(username):
    sql = "SELECT COUNT(*)\
           FROM admin_users A, users U \
           WHERE A.user_id=U.id AND U.username=:username;"
    result = db.session.execute(sql,{"username":username})
    value = result.fetchall()
    
    return value[0][0] == 1

def getuser(username):
    sql = "SELECT id FROM users WHERE username =:username;"
    result = db.session.execute(sql,{"username":username})
    value = result.fetchone()

    return value[0]

def is_user(username):
    sql = "SELECT COUNT(*) FROM users WHERE username =:username;"
    result = db.session.execute(sql,{"username":username})
    if result.fetchone()[0] == 1:
        return True
    return False

def banned(username):
    sql = "SELECT visible FROM users WHERE username =:username;"
    result = db.session.execute(sql,{"username":username})
    if result.fetchone()[0] == False:
        return True
    return False

def get_user_info(user_id):
    sql = "SELECT id, username, visible, (SELECT COUNT(*) FROM prices WHERE user_id = :id) AS pricecount, (SELECT COUNT(*) FROM chat WHERE sender_id = :id) AS chatcount FROM users WHERE id = :id;"
    result = db.session.execute(sql,{"id":user_id})
    return result.fetchone()


def getpassword(username):
    sql = "SELECT password FROM users WHERE username =:username;"
    result = db.session.execute(sql,{"username":username})
    value = result.fetchone()
    return value[0]


def postchatmessage(username, message):
    sql = "INSERT INTO chat (sender_id, message, time) VALUES (:username, :message, NOW());"
    db.session.execute(sql,{"username":username, "message":message})
    db.session.commit()


def getchatmessages():
    sql = "SELECT C.message, U.username, C.time FROM chat C, users U WHERE U.id = C.sender_id ORDER BY time DESC LIMIT 7;"
    result = db.session.execute(sql)
    return result

def getrequests():
    sql = "SELECT id, sender_id, message, time FROM requests WHERE visible = TRUE;"
    result = db.session.execute(sql)
    return result

def addrequest(sender_id, message):
    sql = "INSERT INTO requests (sender_id, message, visible, time) VALUES (:sender_id, :message, TRUE, NOW());"
    db.session.execute(sql,{"sender_id":sender_id, "message":message})
    db.session.commit()

def hiderequest(request_id):
    sql = "UPDATE requests SET visible=FALSE WHERE id=:request_id;"
    db.session.execute(sql,{"request_id":request_id})
    db.session.commit()
    
def get_areas():
    sql = "SELECT UNIQUE city \
        FROM stations \
        WHERE visible = TRUE;"
    results = db.session.execute(sql)
    return results.fetchall()

def get_roads():
    sql = "SELECT UNIQUE road \
        FROM stations \
        WHERE visible = TRUE;"
    results = db.session.execute(sql)
    return results.fetchall()

def get_station_info(station_id):
    sql = "SELECT id, station_name, addr, postnr, city, road, operational \
        FROM stations \
        WHERE id = :station_id;"
    result = db.session.execute(sql,{"station_id":station_id})
    return result.fetchone()

def get_station_prices(station_id):
    sql = "SELECT id, user_id, date_trunc('day', time) AS date, type1_price, type2_price, type3_price, type4_price \
        FROM prices \
        WHERE station_id = :station_id AND visible = TRUE \
        ORDER BY date;"
    result = db.session.execute(sql,{"station_id":station_id})
    return result.fetchall()