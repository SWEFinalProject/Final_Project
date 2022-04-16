import os
import flask
from model import User, Restaurant, Chatroom, Ct
# import session, request, jsonify
from sqlalchemy import PrimaryKeyConstraint
from api_setup import get_data
from flask_sqlalchemy import SQLAlchemy
import flask_login as fl
import hashlib
from dotenv import load_dotenv, find_dotenv
from werkzeug.security import generate_password_hash, check_password_hash


"""FLASK-login manager"""


load_dotenv(find_dotenv())


app = flask.Flask(__name__)
# Point SQLAlchemy to your Heroku database
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB")
# Gets rid of a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = os.getenv("secret_key")


db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB")
if app.config["SQLALCHEMY_DATABASE_URI"].startswith("postgres://"):
    app.config["SQLALCHEMY_DATABASE_URI"] = app.config[
        "SQLALCHEMY_DATABASE_URI"
    ].replace("postgres://", "postgresql://")

login_manager = fl.LoginManager(app)
login_manager.login_view = "login"
login_manager.init_app(app)


bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

"""Database classes + table"""

db.init_app(app)
with app.app_context():
    db.create_all()
    user = User.query.all()


class Ct(db.Model):
    id = db.Column(db.Integer, primary_key=True)


@app.route("/get_all_restaurants",methods=["GET"])
def get_all_restaurants():
    rest_list = db.engine.execute(f""" select * from "restaurant"  """).all()
    pass
    #rest_name = [rest1, rest2, ...]

@app.route("/get_business_data/<name>",methods=["GET"]) # name is a value (restaurant's name)
def get_business_data(name):
    """Usage: localhost:5000/get_business_data/cafe lucia """
    return get_data(name)
   

@app.route("/", methods=["POST", "GET"])
def login():
    if flask.request.method == "POST":
        username = flask.request.json["username"]
        pd = flask.request.json["password"]
        pd_hash = hashlib.md5(pd.encode("utf-8")).hexdigest()
        isUser = user.query.filter_by(username=username).first()
        if not isUser:
            return flask.jsonify({"error": "Not found"}), 404
        if not check_password_hash(isUser.password, pd_hash):
            return flask.jsonify({"error": "Unathorized"}), 401
        return flask.jsonify({"id": isUser.id, "username": isUser.username})
    return flask.jsonify("Not post request")


@login_manager.user_loader
def load_user(user_id):
    """Load user for login manager"""
    return User.query.get(int(user_id))


"""PLACEHOLDER for the route to the main page"""


@app.route("/pmain", methods=["POST", "GET"])  # was /loggeduser
@fl.login_required
def main():
    if flask.request.method == "POST":
        # if flask.request.json.get("action") == "profile":
        #     return flask.redirect("/profile")
        # elif flask.request.json.get("action") == "submit":
        #     # funtion call to handle functionality for submit action(similar to else below)
        #     pass
        review_page(flask.request.form)
        return flask.redirect("/on_submit_button")

    else:
        """This function creating a template using .html file
        and pass values to the variables in a template"""
        name, tagline, genres, poster_path, mov_url, movie_id = get_data()
        base_url, poster_sizes = get_config()
        review = db.engine.execute(
            f""" select * from "review" where movie_id = '{movie_id}' """
        ).all()
        print(review)
        flask.flash(review)
        return flask.render_template(
            ["index.html"],
            name=name,
            tagline=tagline,
            genres=genres,
            poster_path=poster_path,
            base_url=base_url,
            poster_sizes=poster_sizes,
            url=base_url + poster_sizes + poster_path,
            movie_url=mov_url,
            movie_id=movie_id,
        )


"""PLACEHOLDER for the route to the restaurant page
~coming from a SEARCH bar"""


@app.route("/restaurant", methods=["POST", "GET"])
@fl.login_required
def restaurant():
    return flask.render_template("restaurant.html")


"""PLACEHOLDER for the route to the profile page
~coming from a button on main page"""


@app.route("/profile", methods=["POST", "GET"])
def profile():
    return flask.render_template("profile.html")


"""PLACEHOLDER for the route to the chat page (REACT)
~coming from a button
SHOULD BE A REACT PAGE"""
# route for serving React page
@bp.route("/")
@fl.login_required
def index():
    # NB: DO NOT add an "index.html" file in your normal templates folder
    # Flask will stop serving this React page correctly
    return flask.render_template("index.html")


# CREATED NEW ROUTE for serving Flask page
@bp.route("/chat", methods=["POST"])
@fl.login_required
def chat():  # should return a JSON file with a fun fact in it
    chats = ["Hi there! It is our chat page"]
    return flask.jsonify(chats)


# register function implemented with hashing
@app.route("/register", methods=["GET", "POST"])
def register():
    """registration"""
    # pylint: disable=no-member
    if flask.request.method == "POST":
        f_name =  flask.request.json["f_name"]
        l_name =  flask.request.json["l_name"]
        gsu_id =  flask.request.json["gsu_id"]
        level =  flask.request.json["level"]
        phone =  flask.request.json["phone"]
        password =  flask.request.json["password"]
        primary_major =  flask.request.json["primary_major"]

        hashed_password = generate_password_hash(password, method="sha256")
        user_exists = User.query.filter_by(gsu_id=gsu_id).first()
        if user_exists:
             return flask.jsonify({"error": "Unauthorized"}), 401

        new_user = User(
            f_name=f_name,
            l_name=l_name,
            gsu_id=gsu_id,
            level=level,
            primary_major = primary_major,

        )
        db.session.add(new_user)
        db.session.commit()
    return flask.jsonify({"id": new_user.id, "gsu_id": new_user.gsu_id})
    # return flask.jsonify({"message": "success"})


app.register_blueprint(bp)

# @app.route("/loggeduser", methods=["POST", "GET"])


app.run(debug=True)

if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True
    )
    
# {
#     "f_name" : "Nur",
#     "l_name": "Haque",
#     "gsu_id" : "1234",
#     "level": "undergrad",
#     "primary_major" : "Computer science"
# }