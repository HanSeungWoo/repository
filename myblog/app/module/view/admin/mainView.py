'''
Created on 2014. 1. 2.

@author: dev.s
'''
from flask import render_template
from app import app

@app.route('/admin')
def admin():
    return render_template("/admin/index.html")

@app.route('/layout')
def layout():
    return render_template("/layout/admin/base.html")