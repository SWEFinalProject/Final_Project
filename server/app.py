from flask import Flask, render_template
import os

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)

