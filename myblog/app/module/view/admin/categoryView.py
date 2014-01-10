'''
Created on 2014. 1. 10.

@author: dev.s
'''

from flask import render_template
from app import app

@app.route('/category/categoryList')
def categoryList():
    
    
    return render_template("/admin/category/categoryList.html")