## Python quote generator written in the flask framework
This app, written using the programming languages of python(using the flask framework) , javascipt, CSS, and HTML. The user will be presented with a login screen when they launch the app asking for their username and password. To sign in simply use matthew as the username and password as the password. You can also use datarep as the username and gmit as the password. After you log in youll be presented with a screen with two buttons one saying new quote and one saying logout. To get your random quote simply click the new quote button. If you wish to log out simply click the logout button.

## Motivation
This app was created as a project for college for the module Data Repersentation and Querying. This is a module in the course bachelor of science in computing in software development. More can be learned about the course here http://www.gmit.ie/software-development/bachelor-science-computing-software-development . The project was guided by the following excerpt from the project instructions:

You are required to develop a single-page web application(SPA) written in the programming language Python using the Flask framework. You must devise an idea for a web application, write the software, write documentation explaining how the application works, and write a short user guide for it.

## How to run app
1. Download python from https://www.python.org/downloads/release/python-352/ . Download version Python 3.5.2.
2. Open a command prompt window
3. Type pip install flask
4. Next type  sudo pip install Flask-SqlAlchemy 
5. Download this project from github
6. Change directory to where you have the project saved
7. Type python app.py
8. Should say running on http://127.0.0.1:5000/
9. Open a web browser and go to http://127.0.0.1:5000/
10. App should be running there.
11. To log in use matthew as the username and password as password.
12. Otherwise use datarep as username and gmit as password.

## Creator
This application was created by Matthew Lally a third year software development student in GMIT. 

##Architecture
This web application runs in Python 3 using the Flask web micro-framework and uses SQLite as a database. I  chose to use  SQLite as it is easy to use. .

##How the app works
The quotes are generated using the javascript file found in the static folder. This creates a function called new quote. You link the javascript in html and call the function in a button when the button is pressed, a random quote will appear. When you intially open the app python will open the default route. This will bring you to the login screen if you are not logged in. After you log in python tells the app to go too the test.html page which is where you will be able to see your random quote. The pages are syled using the two different CSS files.
