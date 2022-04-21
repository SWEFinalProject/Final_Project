"""Backend"""
import os
import flask
from model import Users, Restaurant, Chatroom, Ct
from sqlalchemy import PrimaryKeyConstraint
from database import db
from api_setup import get_data
import flask_login as fl
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from config import ApplicationConfig
from flask_socketio import SocketIO, send

app = flask.Flask(__name__)
app.config.from_object(ApplicationConfig)
db.init_app(app)
with app.app_context():
    db.create_all()
    user = Users.query.all()

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB")
if app.config["SQLALCHEMY_DATABASE_URI"].startswith("postgres://"):
    app.config["SQLALCHEMY_DATABASE_URI"] = app.config[
        "SQLALCHEMY_DATABASE_URI"
    ].replace("postgres://", "postgresql://")
login_manager = fl.LoginManager(app)
login_manager.login_view = "login"
login_manager.init_app(app)
socketIo = SocketIO(app, cors_allowed_origins="*")


bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)


@app.route("/get_all_restaurants", methods=["GET"])
def get_all_restaurants():
    """Database classes + table"""
    # rest_list = db.engine.execute(f""" select * from "restaurant"  """).all()
    # rest_name = [rest1, rest2, ...]


@app.route(
    "/get_business_data/<name>", methods=["GET"]
)  # name is a value (restaurant's name)
def get_business_data(name):
    """Usage: localhost:5000/get_business_data/cafe lucia"""
    return get_data(name)


@app.route("/login", methods=["POST", "GET"])
def login():
    """Login"""
    gsu_id = flask.request.json["gsu_id"]
    password = flask.request.json["password"]
    isUser = Users.query.filter_by(gsu_id=gsu_id).first()
    if not isUser:
        return flask.jsonify({"error": "Not Found"}), 404
    else:
        if not check_password_hash(isUser.password, password):
            return flask.jsonify({"error": "Unauthorized"}), 401
    return flask.jsonify({"id": isUser.id, "username": isUser.gsu_id})


@login_manager.user_loader
def load_user(user_id):
    """Load user for login manager"""
    return Users.query.get(int(user_id))


@socketIo.on("message")
def handleMessage(msg):
    print(msg)
    send(msg, broadcast=True)


@app.route("/restaurant", methods=["POST", "GET"])
@fl.login_required
def restaurant():
    """PLACEHOLDER for the route to the restaurant page coming from a SEARCH bar"""
    return flask.render_template("restaurant.html")


# PLACEHOLDER for the route to the profile page coming from a button on main page


@app.route("/profile", methods=["POST", "GET"])
def profile():
    """Profile"""
    return flask.render_template("profile.html")


# route for serving React page
@bp.route("/")
@fl.login_required
def index():
    """PLACEHOLDER for the route to the chat page (REACT)
    ~coming from a button
    SHOULD BE A REACT PAGE"""
    # NB: DO NOT add an "index.html" file in your normal templates folder
    # Flask will stop serving this React page correctly
    return flask.render_template("index.html")


# CREATED NEW ROUTE for serving Flask page
@bp.route("/chat", methods=["POST"])
@fl.login_required
def chat():  # should return a JSON file with a fun fact in it
    """Chat"""
    chats = ["Hi there! It is our chat page"]
    return flask.jsonify(chats)


# register function implemented with hashing
@app.route("/register", methods=["GET", "POST"])
def register():
    """registration"""
    # pylint: disable=no-member
    # pylint: disable=unused-variable
    if flask.request.method == "POST":
        f_name = flask.request.json["f_name"]
        l_name = flask.request.json["l_name"]
        gsu_id = flask.request.json["gsu_id"]
        level = flask.request.json["level"]
        phone = flask.request.json["phone"]
        password = flask.request.json["password"]
        primary_major = flask.request.json["primary_major"]
        alt_email = flask.request.json["alt_email"]

        hashed_password = generate_password_hash(password, method="sha256")
        user_exists = Users.query.filter_by(gsu_id=gsu_id).first()
        if user_exists:
            return flask.jsonify({"error": "Unauthorized"}), 401

        new_user = Users(
            f_name=f_name,
            l_name=l_name,
            gsu_id=gsu_id,
            level=level,
            primary_major=primary_major,
            phone=phone,
            alt_email=alt_email,
            password=hashed_password,
        )
        db.session.add(new_user)
        db.session.commit()
    return flask.jsonify({"message": "No Post Request"})


@bp.route("/new_chatroom", methods=["POST"])
@fl.login_required
def new_chatroom():
    existing_users = []
    if flask.request.method == "POST":
        name = flask.request.json["name"]
        users_to_add = flask.request.json["users_to_add"]

    ls_to_add = users_to_add.split(sep=",")
    for user in ls_to_add:
        user_exists = Users.query.filter_by(gsu_id=user).first()
        existing_users.append(user)

    new_chatroom = Chatroom(name=name)
    db.session.add(new_chatroom)
    db.session.commit()


app.register_blueprint(bp)

# @app.route("/loggeduser", methods=["POST", "GET"])


if __name__ == "__main__":
    socketIo.run(
        app,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )

# Nur Haque
# Please make sure the backend code work. While connecting the fronend to the backend I ran into a lot of problem.
# This doesn't only include compiling error. Please make sure each route has no error in it.
# Hear is great tool for testing the backend: Postman.
# You can use the data below to test your the register route. Use similar types of test cases to test each and everyroute in particular thouse of which require
# a user input
# {
#     "f_name" : "firstName",
#     "l_name": "lastname",
#     "gsu_id" : "342232332",
#     "level": "undergrad",
#     "phone": "1234",
#     "password": "1234",
#     "primary_major" : "Computer science",
#     "alt_email": "Email"
# }
