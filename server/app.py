# pylint: disable=E0401, R0903, R1705
"""Backend"""
import os
import flask
from flask import session
from model import Users
from database import db
from api_setup import get_data
import flask_login as fl
from werkzeug.security import generate_password_hash, check_password_hash
from config import ApplicationConfig
from flask_socketio import SocketIO, send

app = flask.Flask(__name__)
app.config.from_object(ApplicationConfig)

db.init_app(app)
with app.app_context():
    db.create_all()
    all_user = Users.query.all()

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
    is_user = Users.query.filter_by(gsu_id=gsu_id).first()
    if not is_user:
        return flask.jsonify({"error": "Not Found"}), 404
    else:
        if not check_password_hash(is_user.password, password):
            return flask.jsonify({"error": "Unauthorized"}), 401
    session["user"] = f"{is_user.f_name } {is_user.l_name }"
    session["gsu_id"] = f"{is_user.gsu_id}"
    return flask.jsonify({"id": is_user.id, "username": is_user.gsu_id})


@app.route("/user")
def user():
    """Sends User's first and last name to frontend"""
    if "user" in session:
        my_user = session["user"]
        return flask.jsonify(my_user)
    else:
        return flask.jsonify({"error": "Unauthorized"}), 401


@login_manager.user_loader
def load_user(user_id):
    """Load user for login manager"""
    return Users.query.get(int(user_id))


@socketIo.on("message")
def handle_message(msg):
    """sends message to clients using socket"""
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


@app.route("/profile_query", methods=["POST", "GET"])
def profile_query():
    """Profile query from db"""
    gsu_id = session["gsu_id"]
    my_user = Users.query.filter_by(gsu_id=gsu_id).first()
    return flask.jsonify(
        {
            "GSU ID": my_user.gsu_id,
            "f_name": my_user.f_name,
            "l_name": my_user.l_name,
            "level": my_user.level,
            "major": my_user.primary_major,
            "alt_email": my_user.alt_email,
            "phone": my_user.phone,
        }
    )


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


@app.route("/logout", methods=["GET"])
def logout():
    """Logs out users"""
    session.pop("user", None)
    return flask.jsonify("logout Successful")


@bp.route("/search_bar", methods=["GET", "POST"])
@fl.login_required
def search_bar():
    """defines search bar for yelp api"""
    if flask.request.method == "POST":
        rest_name = flask.request.json["name"]

    data = get_data(rest_name)

    return flask.jsonify(data)


# app.register_blueprint(bp)

if __name__ == "__main__":
    socketIo.run(app)
