import os
from os import environ
from flask import Flask, flash, render_template, url_for, redirect, request, send_from_directory, abort
from flask import render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', code=404, ctx={'error':e})

@app.route("/")
def index():
    """_summary_
        returns the rendered template of the index page to the server
    """
    return render_template("index.html")

@app.route("/cv")
def cv():
    """_summary_
        returns the rendered template of the cv page to the server
    """
    return render_template("cv.html")

@app.route("/portfolio")
def portfolio():
    """_summary_
        returns the rendered template of the porfolio page to the server
    """
    return render_template("portfolio.html")

@app.route("/mail", methods=['GET', 'POST'])
def mail():
    """_summary_
    form to send a mail to the owner of the website.
    Returns:
        template: form template if GET
        redirect: if POST with 301 status code
    """
    if request.method=="GET":
        return render_template('mailForm.html')
    elif request.method=="POST":    
        # TODO send the mail to me and a copy to the sender
        flash("la fonctionnalité n'est pas encore implémenté veuillez m'écrire via mon adresse mail que vous trouverez en bas sur cette page", "error")
        return redirect(url_for('index'), code=301)
    else:
        flash("vous n'avez pas la possibilité d'utiliser cette méthode sur cette URL", "error")
        return redirect(url_for('index'), code=403)

@app.route("/get-CV/<string:language>", methods=['GET'])
def get_cv(language):
    """ should send CV to the user, in the language he asked

    Args:
        language (string): |'fr'|'en'| language asked by the user
    """
    static = os.path.join(app.root_path, 'static')
    try:
        if language=='fr':
            return send_from_directory(static,path='pdf/cv_fr.pdf', as_attachment=True)
        else:
            return send_from_directory(static,path='pdf/cv_en.pdf', as_attachment=True)
    except FileNotFoundError:
        abort(404)