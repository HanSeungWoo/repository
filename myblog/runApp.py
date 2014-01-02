'''
Created on 2013. 12. 31.

@author: dev.s
'''
from app import app
SERVER_NAME = "127.0.0.1"
SERVER_PORT = 9090

app.run(SERVER_NAME,SERVER_PORT, debug=True)

