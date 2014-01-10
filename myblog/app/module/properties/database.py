'''
Created on 2014. 1. 9.

@author: dev.s
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#postgresql://scott:tiger@localhost/mydatabase
#mysql://scott:tiger@localhost/mydatabase
#oracle://scott:tiger@127.0.0.1:1521/sidname
#sqlite:////absolute/path/to/foo.db

#DB
DB_VENDOR   = "mysql+pymysql"
DB_USER     = "devs"
DB_PASSWORD = "gksnrhrl"
DB_SERVER   = "192.168.145.128:3306"
DB_NAME     = "myblog"

SQLALCHEMY_DATABASE_URI = DB_VENDOR + "://" + DB_USER + ":" + DB_PASSWORD + "@" + DB_SERVER + "/" + DB_NAME

engine = create_engine(SQLALCHEMY_DATABASE_URI , convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
 
Base = declarative_base()
Base.query = db_session.query_property()
 
def init_db():
    None
    #from app.module.model import memberModel
    #Base.metadata.create_all(bind=engine)
    
'''    
conn = pymysql.connect(host='192.168.145.128', port=3306, user='devs', passwd='gksnrhrl', db='myblog')
cur = conn.cursor()
cur.execute("SELECT * FROM tb_member")

for data in cur.fetchall():
id = data[1]
password = data[2]

cur.close()
conn.close()
'''