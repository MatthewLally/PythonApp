import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('sqlite:///userData.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
user = User("matthew","password")
session.add(user)
 
user = User("datarep","gmit")
session.add(user)

 
# commit the record the database
session.commit()
 
session.commit()