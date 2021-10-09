import werkzeug.security
from app import app
import flask
import db



@app.route("/")
def index():
    if(flask.session):
        print(flask.session)
        print(db.isadmin(flask.session["username"]))
        print(db.getuser(flask.session["username"]))
    
    return flask.render_template("index.html", prices = db.getprices(), chats = db.getchatmessages())


@app.route("/login",methods=["POST"])
def login():
    username = flask.request.form["username"]
    password = flask.request.form["password"]
    if db.isuser(username):
        user_id = db.getuser(username)
        hash = db.getpassword(username)
        if werkzeug.security.check_password_hash(hash, password):
            flask.session["username"] = username
            flask.session["user_id"] = user_id
            if db.isadmin(username):
                flask.session["role"] = "admin"
            else:
                flask.session["role"] = "user"

            print("User", username, "logged in.")
            return flask.redirect("/")
        else:
            return flask.render_template("error.html",message = "Väärä salasana!")
    else:
        return flask.render_template("error.html",message = "Käyttäjätunnusta ei löydy.")

@app.route("/logout")
def logout():
    username = flask.session["username"]
    
    del flask.session["username"]
    del flask.session["role"]
    del flask.session["user_id"]


    print("User", username, "logged out.")
    return flask.redirect("/")

@app.route("/error")
def error():
    flask.render_template("error.html")
    return flask.redirect("/")

@app.route("/addstation")
def addstation():
    #if db.isadmin(flask.session["username"]):
    return flask.render_template("addstation.html",requests=db.getrequests())
    #else:
    #   return flask.redirect("/")

@app.route("/newstation",methods=["POST"])
def newstation():
    st_name = flask.request.form["station_name"]
    st_address = flask.request.form["address"]
    st_city = flask.request.form["city"]
    st_postnr = flask.request.form["postnr"]
    st_road = flask.request.form["road"]

    db.addstation(st_name, st_address, st_city, st_postnr, st_road)
    return flask.redirect("/newprice")

@app.route("/newprice")
def newprice():
    if flask.session:
        stations = db.getstations()
        return flask.render_template("newprice.html", stations=stations)
    else:
        return flask.redirect("/")

@app.route("/addprice",methods=["POST"])
def addprice():
    user_id = db.getuser(flask.session["username"])
    st_id = flask.request.form["station_number"]
    price1 = flask.request.form["price1"]
    price2 = flask.request.form["price2"]
    price3 = flask.request.form["price3"]
    price4 = flask.request.form["price4"]

    #TODO check quality of input

    db.addprice(user_id,st_id, price1, price2, price3, price4)
    print("User", flask.session["username"], "posted new price.")

    return flask.redirect("/")

@app.route("/newuser")
def newuser():
    if not flask.session:
        return flask.render_template("registration.html")
    return flask.redirect("/")

@app.route("/register", methods=["POST"])
def register():
    username = flask.request.form["username"]
    password1 = flask.request.form["password1"]
    password2 = flask.request.form["password2"]

    if db.isuser(username):
        return flask.render_template("error.html",message = "Käyttäjätunnus on jo varattu. Valitse jokin muu tunnus!")

    if password1 == password2:
        hash_value = werkzeug.security.generate_password_hash(password1)
        db.adduser(username, hash_value)
        print("new user", username, "registered")
        return flask.redirect("/")
    else:
        return flask.render_template("error.html",message = "Salasanat eivät olleet samat. Olehan tarkkana.")


@app.route("/chatmessage", methods=["POST"])
def chatmessage():
    if flask.session:
        user = db.getuser(flask.session["username"])
        message = flask.request.form["message"]
        db.postchatmessage(user, message)
    return flask.redirect("/")

@app.route("/requeststation", methods=["POST"])
def requeststation():
    if flask.session:
        user = flask.session["user_id"]
        message = flask.request.form["message"]
        db.addrequest(user,message)
    return flask.redirect("/")

@app.route("/hiderequest", methods = ["POST"])
def hiderequest():
    if flask.session["role"] == "admin":
        request_id = flask.request.form["request_id"]
        db.hiderequest(request_id)
        return flask.redirect("/addstation")
    else:
        return flask.redirect("/")

# @app.route("/search", methods = ["POST"])
# def search():
#     #TODO
#     roads = db.get_roads()
#     cities = db.get_areas()

@app.route("/station/<int:id>")
def station(id):
    station_id = int(id)
    station = db.get_station_info(station_id)
    prices = db.get_station_prices(station_id)
    return flask.render_template("station.html", station=station, prices=prices)

def hello():
    return "onnennumero: " + str(randint(0,100))