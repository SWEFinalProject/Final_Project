"""PLACEHOLDER to describe app.py"""
import os
import flask
from sqlalchemy import PrimaryKeyConstraint
from api_setup import get_data, get_config
from flask_sqlalchemy import SQLAlchemy
import hashlib
from dotenv import load_dotenv, find_dotenv


"""FLASK-login manager"""



load_dotenv(find_dotenv())



app = flask.Flask(__name__)
# Point SQLAlchemy to your Heroku database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# Gets rid of a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.config["SECRET_KEY"]=os.getenv('secret_key')


"""ELIZA

we will need a code for transforming postgres to postgresql
for Heroku deployment"""



db = SQLAlchemy(app) # db object

bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

"""ELIZA 

PLACEHOLDER for DB classes

class User
class Restaraunts

feel free to delete commented old classes section"""
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(150), nullable=False)
#     password = db.Column(db.String(100), nullable=False)

# class Review(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     movie_id = db.Column(db.Integer)
#     rating = db.Column(db.Integer)
#     comment = db.Column(db.String(1000))
#     user = db.Column(db.String(100))
db.create_all()   


@app.route("/", methods=["POST", "GET"])
def login():
    if flask.request.method == "POST":
        login_inp = flask.request.form.get("username")
        pd = flask.request.form.get("password")
        pd_hash=hashlib.md5(pd.encode("utf-8")).hexdigest()
        # us = User.query.filter_by(username = login_inp).first()
        # print(User.query.filter_by(username = login_inp).first())

        if db.engine.execute(f""" select * from "user" where username='{login_inp}' and password='{pd_hash}' """).all() :
            print(db.engine.execute(f"""select * from "user" where username='{login_inp}' and password='{pd_hash}' """).all())
            return flask.redirect("/pmain")
        # if User.query.filter_by(username = login_inp).first() and \
        # User.query.filter_by(password=hashlib.md5(pd.encode("utf-8")).hexdigest()):

            
        else:
            print("abracadabra")
            flask.flash('Username or password is incorrect. Please try again!')
            return flask.redirect("/smthwrong")
    
    return flask.render_template(
        ["login.html"],
        )


"""PLACEHOLDER for the route to the main page"""

@app.route("/pmain", methods=["POST", "GET"]) #was /loggeduser
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
        review = db.engine.execute(f""" select * from "review" where movie_id = '{movie_id}' """).all()
        print(review)
        flask.flash(review)
        return flask.render_template(
            ["index.html"],
            name = name,
            tagline = tagline,
            genres = genres,
            poster_path = poster_path,
            base_url = base_url,
            poster_sizes = poster_sizes,
            url=base_url+poster_sizes+poster_path,
            movie_url = mov_url,
            movie_id = movie_id,
            )

"""PLACEHOLDER for the route to the restaurant page
~coming from a SEARCH bar"""

@app.route("/restaurant", methods=["POST", "GET"])
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
def index():
    # NB: DO NOT add an "index.html" file in your normal templates folder
    # Flask will stop serving this React page correctly
    return flask.render_template("index.html")

#CREATED NEW ROUTE for serving Flask page
@bp.route("/chat", methods=["POST"])
def chat(): # should return a JSON file with a fun fact in it
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

#@app.route("/loggeduser", methods=["POST", "GET"])
def review_page(data):
    # if flask.request.method == "POST":
    mov_id = dict(data)["MovieID"]
    uname = dict(data)["uname"]
    Rating = dict(data)["Rating"]
    Comment = dict(data)["Comment"]
    db.session.add(Review(
                    movie_id=mov_id,
                    rating=Rating,
                    comment=Comment,
                    user=uname, ))
    db.session.commit()

        #uname = flask.request.form.get("uname")
        # return flask.render_template(
        #     ["index.html"],
        #     uname=uname)


app.run(debug=True)

#DB - https://dashboard.heroku.com/apps/radiant-waters-19745 
#Heroku app - 