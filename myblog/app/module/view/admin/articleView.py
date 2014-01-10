'''
Created on 2014. 1. 10.

@author: dev.s
'''
from flask import render_template
from app import app

@app.route('/article/articleList')
def articleList():
    return render_template("/admin/article/articleList.html")