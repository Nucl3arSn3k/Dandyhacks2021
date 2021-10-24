import os
import json
import logging
from flask import Flask, redirect, request, url_for, render_template
from flask_caching import Cache
import requests
import firebase_admin

from translator import translate_html_from


# from firebase import firebase


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


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/transalation")
def transaltor():
    urlv2 = request.url
    list_scrape = translate_html_from(urlv2)
    # open_file = open("/templates/translated.html", "w")
    # open_file.write(list_scrape)
    return "Beans"


@app.route("/signin.html")
def signin():
    return render_template("signin.html")


@app.route("/home.html")
def homepage():
    return render_template("home.html")


@app.route("/libros.html")
def bookstuff():
    # list_scrape = []
    print("This is definitely the current URL" + request.url)

    return render_template("libros.html")


@app.route("/literatura.html")
def books():
    return render_template("literatura.html")


@app.route("/messages")
def messages():
    return "Message sent to backend"


@app.route("/pitmarket.html")
def bookmarket():
    return render_template("pitmarket.html")


@app.route("/submit_message", methods=["POST"])
def submit_message():
    print(request.form)
    message = {"body": request.form["message"], "who": request.form["who"]}
    json_object = json.dumps(message, indent=4)
    open_file = open("demofile2.json", "w")
    open_file.write(json_object)
    requests.put(
        url="https://leelo-329900-default-rtdb.firebaseio.com/.json",
        json=json_object,  # shoves the comments users make on this page to firebase
    )
    return redirect(url_for("messages"))


@app.route("/cache")
@cache.cached(timeout=50)
def cachedpage():
    return "Cached for 50 seconds"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
