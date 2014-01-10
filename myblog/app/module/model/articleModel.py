'''
Created on 2014. 1. 9.

@author: dev.s
'''
from sqlalchemy import Column,Integer,String,DateTime,Text
from app.module.properties.database import Base
class Article(Base):
    __tablename__ = 'tb_article'
    
    idx             = Column(Integer , primary_key = True)
    memberId        = Column(String(30))
    title           = Column(String(200))
    content         = Column(Text)
    hit             = Column(Integer)
    status          = Column(Integer)
    category        = Column(Integer)
    writeDate       = Column(DateTime)
    
    
    def __init__(self
                 ,idx=None
                 ,memberId=None
                 ,title=None
                 ,content=None
                 ,hit=None
                 ,status=None
                 ,category=None
                 ,writeDate=None
                 ):
        self.idx             = idx
        self.memberId        = memberId
        self.title           = title
        self.content         = content
        self.hit             = hit
        self.status          = status
        self.category        = category
        self.writeDate       = writeDate