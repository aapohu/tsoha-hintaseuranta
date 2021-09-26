from re import S
from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

def adduser(username, password):

    sql = "INSERT INTO users (username, password)VALUES(:name, :password);"
    db.session.execute(sql, {"name":username, "password":password})
    db.session.commit()
    

def addprice(user, station, price1, price2, price3):
    sql = "INSERT INTO prices (station_id, user_id, time, visible, type1_price, type2_price, type3_price) VALUES (:station, :user, NOW(), TRUE, :price1, :price2, :price3);"
    db.session.execute(sql,{"station":station, "user":user, "price1":price1, "price2":price2, "price3":price3})
    db.session.commit()

def addstation(name, address, city, postnr, road):
    sql = "INSERT INTO stations (station_name, addr, city, postnr, road, operational, visible) VALUES (:name, :address, :city, :postnr, :road, TRUE, TRUE);"
    db.session.execute(sql, {"name":name, "address":address,"city":city, "postnr":postnr, "road":road})
    db.session.commit()

def hideprice(price_id):
    sql = "UPDATE prices SET visible=FALSE WHERE id=:pid;"
    db.session.execute(sql,{"pid":price_id})

def closestation(station_id):
    sql = "UPDATE stations SET operational=FALSE WHERE id=:stid;"
    db.session.execute(sql,{"stid":station_id})

def hidestation(station_id):
    sql = "UPDATE stations SET visible=FALSE WHERE id=:stid;"
    db.session.execute(sql,{"stid":station_id})

def hideuser(user_id):
    sql = "UPDATE users SET visible=FALSE WHERE id=:uid;"
    db.session.execute(sql,{"uid":user_id})


def getstations():
    sql = "SELECT * FROM stations;"
    result = db.session.execute(sql)
    return result.fetchall()

def getprices():
    sql = "SELECT S.station_name, S.id, P.type1_price, P.type2_price, P.type3_price, P.time FROM prices P, stations S WHERE S.id = P.station_id ORDER BY time DESC LIMIT 20;"
    result = db.session.execute(sql)
    return result.fetchall()

def isadmin(username):
    sql = "SELECT COUNT(*) FROM admin_users A, users U WHERE A.user_id=U.id AND U.username=:username;"
    result = db.session.execute(sql,{"username":username})
    value = result.fetchall()
    
    return value[0][0] == 1

def getuser(username):
    sql = "SELECT id FROM users WHERE username =:username;"
    result = db.session.execute(sql,{"username":username})
    value = result.fetchone()

    return value[0]

def isuser(username):
    sql = "SELECT COUNT(*) FROM users WHERE username =:username;"
    result = db.session.execute(sql,{"username":username})
    if result.fetchone()[0] == 1:
        return True
    return False

def getpassword(username):
    sql = "SELECT password FROM users WHERE username =:username;"
    result = db.session.execute(sql,{"username":username})
    value = result.fetchone()
    return value[0]





    
    
