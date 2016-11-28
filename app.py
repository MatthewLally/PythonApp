#Imports 
#all code adapted from https://pythonspot.com/en/flask-web-app-with-python/comment-page-1/ and also from https://pythonspot.com/en/login-authentication-with-flask/

from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from random import randint
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///userData.db', echo=True)
 
app = Flask(__name__)
 
@app.route('/') #first route app takes, brings you too the login screen
def home():
    if not session.get('logged_in'):
        return render_template('login.html') #if not logged in show login hmtl page
    else:
        return render_template ('test.html') #if logged in show test.html page
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    #requests the username and password
    POST_USERNAME = str(request.form['username']) 
    POST_PASSWORD = str(request.form['password'])
 
    Session = sessionmaker(bind=engine)
    s = Session() #creates a new Session s
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) ) #creates query for username and password, they both must be correct
    result = query.first() #returns true if username and password match the database
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()
 
@app.route("/logout") #creates a logout route
def logout():
    session['logged_in'] = False #clears session variable and returns to login screen
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run()
