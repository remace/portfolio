from flask import Flask, render_template, url_for
from flask import render_template


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
# app.config.from_pyfile('settings/config_dev.py')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cv")
def cv():
    return render_template("cv.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")