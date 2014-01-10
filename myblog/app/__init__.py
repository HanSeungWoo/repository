'''
Created on 2013. 12. 31.

@author: dev.s
'''
from flask import Flask
app = Flask(__name__)

#app.config.from_object('config')

#DB
#db = SQLAlchemy(app)

#**************************View**************************#
#Common Part
from app.module.view.common import commonView
#Admin Part
from app.module.view.admin import mainView
from app.module.view.admin import memberView
from app.module.view.admin import articleView
from app.module.view.admin import categoryView
from app.module.view.admin import codeView

#Front Part
from app.module.view.front import mainView


#**************************Model**************************#
#from app.module.model import memberModel
#from app.module.model import articleModel
#from app.module.model import memberModel
#from app.module.model import memberModel

