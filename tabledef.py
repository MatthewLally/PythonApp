#all code adapted from https://pythonspot.com/en/flask-web-app-with-python/comment-page-1/ and also from https://pythonspot.com/en/login-authentication-with-flask/
#imports
from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///userData.db', echo=True) #Creates a file called userData
Base = declarative_base()


 


 class User(Base): #creates user class
    """"""
    __tablename__ = "users" #sets the table name as users
 
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
 
    def __init__(self, username, password):
        """"""
        self.username = username
        self.password = password
 

 
 
 # create tables
Base.metadata.create_all(engine)