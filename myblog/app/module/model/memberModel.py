'''
Created on 2014. 1. 9.

@author: dev.s
'''
from sqlalchemy import Column,Integer,String,DateTime
from app.module.properties.database import Base

class Member(Base):
    __tablename__ = 'tb_member'
    
    idx             = Column(Integer , primary_key = True)
    memberId        = Column(String(30))
    password        = Column(String(50))
    email           = Column(String(100))
    auth            = Column(Integer)
    status          = Column(Integer)
    writeDate       = Column(DateTime)
    lastLoginDate   = Column(DateTime)
    
    
    def __init__(self,memberId=None,password=None,email=None,auth=None,status=None,writeDate=None,lastLoginDate=None):
        self.memberId        =  memberId 
        self.password        =  password 
        self.email           =  email 
        self.auth            =  auth 
        self.status          =  status 
        self.writeDate       =  writeDate 
        self.lastLoginDate   =  lastLoginDate 
        
    #def __repr__(self):
    #    return '<User %r>' % (self.id)