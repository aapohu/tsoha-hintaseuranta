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
    
    return flask.render_template("index.html", prices = db.getprices())


@app.route("/login",methods=["POST"])
def login():
    username = flask.request.form["username"]
    password = flask.request.form["password"]
    if db.isuser(username):
        hash = db.getpassword(username)
        if werkzeug.security.check_password_hash(hash, password):
            flask.session["username"] = username
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
    print("User", username, "logged out.")
    return flask.redirect("/")

@app.route("/error")
def error():
    flask.render_template("error.html")
    return flask.redirect("/")

@app.route("/addstation")
def addstation():
    if db.isadmin(flask.session["username"]):
        return flask.render_template("addstation.html")
    else:
        return flask.redirect("/")

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

    #TODO check quality of input

    db.addprice(user_id,st_id, price1, price2, price3)
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

        
@app.route("/test")
def test():
    data = db.isuser("BOSS")
    print(data)
    return flask.render_template("test.html", message = data)

def hello():
    return "onnennumero: " + str(randint(0,100))