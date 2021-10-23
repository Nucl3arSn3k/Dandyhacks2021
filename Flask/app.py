import os
import logging

from flask import Flask, render_template
from flask_caching import Cache


# Change the format of messages logged to Stackdriver
logging.basicConfig(format="%(message)s", level=logging.INFO)

config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300,
}


TEMPLATE_DIR = "D:/User/Documents/GitHub/CSC 172/Dandyhacks2021/Flask/templates"
STATIC_DIR = "D:/User/Documents/GitHub/CSC 172/Dandyhacks2021/Flask/static"

print(STATIC_DIR)

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.config.from_mapping(config)
cache = Cache(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/homepage")
def homepage():
    return "Homepage placeholder or some shit"


@app.route("/cache")
@cache.cached(timeout=50)
def cachedpage():
    return "Cached for 50 seconds"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))