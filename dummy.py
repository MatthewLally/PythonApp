#all code adapted from https://pythonspot.com/en/flask-web-app-with-python/comment-page-1/ and also from https://pythonspot.com/en/login-authentication-with-flask/
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('sqlite:///userData.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
database = Session()

#data to test login
user = User("matthew","password")
database.add(user)
 
user = User("datarep","gmit")
database.add(user)

 
# commit the record the database
database.commit()
 
database.commit()
