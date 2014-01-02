
from flask import render_template, flash, redirect
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template("/front/main/index.html")

@app.route('/detail')
def detail():
    return render_template("/front/main/detail.html")

@app.route('/search')
def search():
    return render_template("/front/main/search.html")