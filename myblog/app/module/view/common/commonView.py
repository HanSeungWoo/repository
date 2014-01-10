'''
Created on 2014. 1. 10.

@author: dev.s
'''
from app.module.properties.database import db_session
from app import app
@app.before_request
def before_request():
    None
    #print("before request")

@app.teardown_request
def teardown_request(exception=None):
    #print("request End")
    db_session.remove()
