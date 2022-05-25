from flask import Flask, render_template, url_for, redirect, request
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

@app.route("/mail", methods=['GET', 'POST'])
def mail():
    if request.method=="GET":
        # coucou
        return render_template('mailForm.html')
    elif request.method=="POST":    
        # send the mail to me and a copy to the sender
        return redirect(url_for('index'), code=301)
    else:
        return redirect(url_for('index'), code=403)