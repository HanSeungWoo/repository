'''
Created on 2013. 12. 31.

@author: dev.s
'''

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app.module.view import mainView