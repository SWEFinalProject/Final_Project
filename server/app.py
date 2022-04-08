from flask import Flask, session, request, jsonify
from dotenv import find_dotenv, load_dotenv
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__, static_folder='../build')
CORS(app)
@app.route('/api', methods=["GET"])
@cross_origin()
def index():
    return jsonify("FlaskTest")

CORS(app)
@app.route('/', methods=["GET"])
def serve():
    return send_from_directory(app.static_folder, 'index.html')


def main():
    app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
if __name__ == '__main__':
    main()
