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


app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/libros.html")
def homepage():
    return render_template("libros.html")


@app.route("/cache")
@cache.cached(timeout=50)
def cachedpage():
    return "Cached for 50 seconds"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))