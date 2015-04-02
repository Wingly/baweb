from flask import render_template
from app import app


@app.route('/sporrtNews')
@app.route('/baStory')
@app.route('/index')
@app.route('/')
def index():
    """
    Catches paths from the old site. Mostly refered to from search engines.
    """
    return render_template("index.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")
