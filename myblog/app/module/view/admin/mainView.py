'''
Created on 2014. 1. 2.

@author: dev.s
'''
from flask import render_template
from app import app

@app.route('/bootstrap')
def bootstrap():
    return render_template("/admin/bootstrap.html")

@app.route('/admin')
def admin():
    return render_template("/admin/login.html")
