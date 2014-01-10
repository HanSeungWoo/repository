'''
Created on 2014. 1. 9.

@author: dev.s
'''
from sqlalchemy import Column,Integer,String,DateTime
from app.module.properties.database import Base

class Category(Base):
    __tablename__ = 'tb_category'
    
    idx             = Column(Integer , primary_key = True)
    name            = Column(String(50))
    parentIdx       = Column(Integer)
    writeDate       = Column(DateTime)
    
    
    def __init__(self
                    ,idx=None
                    ,name=None
                    ,parentIdx=None
                    ,writeDate=None
                    ):
        self.idx           =  idx 
        self.name          =  name 
        self.parentIdx     =  parentIdx 
        self.writeDate     =  writeDate 