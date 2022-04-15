import os
import flask

# import session, request, jsonify
from sqlalchemy import PrimaryKeyConstraint
from api_setup import get_data, get_config
from flask_sqlalchemy import SQLAlchemy
import flask_login as fl
import hashlib
from dotenv import load_dotenv, find_dotenv


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

chat_table = db.Table(
    # Table combining many to many relationship with reviews table
    "chat_table",
    db.Column("ct_id", db.Integer, db.ForeignKey("ct.id"), primary_key=True),
    db.Column("user_id", db.String(30), db.ForeignKey("user.gsu_id"), primary_key=True),
    db.Column(
        "chatroom_id", db.Integer, db.ForeignKey("chatroom.id"), primary_key=True
    ),
)


class User(fl.UserMixin, db.Model):
    """Defines each user of program, connects to Comments"""

    __tablename__ = "user"
    id = db.Column(db.Integer, unique=True)
    gsu_id = db.Column(db.String(30), unique=True, primary_key=True, nullable=False)
    f_name = db.Column(db.String(30), unique=False, nullable=False)
    l_name = db.Column(db.String(50), unique=False, nullable=False)
    level = db.Column(db.String(20), unique=False, nullable=False)
    primary_major = db.Column(
        db.String(30), unique=False, nullable=False, default="undecided"
    )
    chat_table = db.relationship(
        "Ct",
        secondary="chat_table",
        lazy="subquery",
        backref=db.backref("users", lazy=True),
    )

    def __repr__(self):
        return f"{self.gsu_id}"


class Restaurant(db.Model):
    __tablename__ = "restaurant"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(80), unique=False, nullable=False)
    rating = db.Column(db.Float, default=0)
    price = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.name}"


class Chatroom(db.Model):
    __tablename__ = "chatroom"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    chat_table = db.relationship(
        "Ct",
        secondary="chat_table",
        lazy="subquery",
        backref=db.backref("chatrooms", lazy=True),
    )

    def __repr__(self):
        return f"{self.name}"


class Ct(db.Model):
    id = db.Column(db.Integer, primary_key=True)


db.create_all()


@app.route("/", methods=["POST", "GET"])
def login():
    if flask.request.method == "POST":
        username = flask.request.json["username"]
        pd = flask.request.json["password"]
        pd_hash = hashlib.md5(pd.encode("utf-8")).hexdigest()
        isUser = Users.query.filter_by(username=username).first()
        if not isUser:
            return flask.jsonify({"error": "Not found"}), 404
        if not check_password_hash(isUser.password, pd_hash):
            return flask.jsonify({"error": "Unathorized"}), 401
        return flask.jsonify({"id": isUser.id, "username": isUser.username})
    return flask.jsonify("Not post request")

@app.route("/register", methods=["POST", "GET"])
def register():
    pass




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
# @app.route("/register", methods=["POST", "GET"])
# def register():
#     if flask.request.method == "POST":

#         sign_inp = flask.request.form.get("username")
#         pd = flask.request.form.get("password")
#         #us = User.query.filter_by(username = login_inp).first()
#         db.engine.execute('SELECT * FROM "user";').all()


#         if User.query.filter_by(username = sign_inp).first():

#             flask.flash('User already present. Try logging in !!')

#             return flask.redirect("/")
#         else:
#             db.session.add(User(username=sign_inp, password=hashlib.md5(pd.encode("utf-8")).hexdigest()))
#             db.session.commit()
#             flask.flash('User successfully created!!!')
#             return flask.redirect("/")

#     return flask.render_template(
#         ["register.html"],
#         #log_
#         )


app.register_blueprint(bp)

# @app.route("/loggeduser", methods=["POST", "GET"])


app.run(debug=True)

if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True
    )
    