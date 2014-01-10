'''
Created on 2014. 1. 9.

@author: dev.s
'''
from sqlalchemy import Column,Integer,String
from app.module.properties.database import Base

class Code(Base):
    __tablename__ = 'tb_code'
        
    code            = Column(Integer,primary_key = True)
    code_type       = Column(int)
    value           = Column(String(50))
    description     = Column(String(300))
    
    
    def __init__(self
                 ,code=None
                 ,code_type=None
                 ,value=None
                 ,description=None):
        self.code          = code
        self.code_type     = code_type
        self.value         = value
        self.description   = description