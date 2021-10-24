import os
import logging
from flask import Flask, redirect, request, url_for, render_template
from flask_caching import Cache
from firebase import firebase
import firebase_admin
from firebase_admin import credentials, db

# Change the format of messages logged to Stackdriver
logging.basicConfig(format="%(message)s", level=logging.INFO)

config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300,
}


app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

cred = credentials.Certificate(
    "D:/User/Documents/GitHub/CSC 172/Dandyhacks2021/Flask/leelo-329900-firebase-adminsdk-fbb7w-a0d372179e.json"
)
firebase_admin.initialize_app(cred)
ref = db.reference("/")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/signin.html")
def signin():
    return render_template("signin.html")


@app.route("/home.html")
def homepage():
    return render_template("home.html")


@app.route("/libros.html")
def bookstuff():
    return render_template("libros.html")


@app.route("/literatura.html")
def books():
    return render_template("literatura.html")


@app.route("/messages")
def messages():
    return "Messages"


@app.route("/pitmarket.html")
def bookmarket():
    return render_template("pitmarket.html")


@app.route("/submit_message", methods=["POST"])
def submit_message():
    print(request.form)
    return redirect(url_for("messages"))


@app.route("/cache")
@cache.cached(timeout=50)
def cachedpage():
    return "Cached for 50 seconds"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))