# Importing the necessary packages.
from flask import Flask, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Import the SQLAlchemy extension.
from models.common import db

# Import the created models and 
from models.users import Users
from models.auser import Auser
from models.classes import Classes
from models.students import Students
from models.subjects import Subjects
from models.assignment_1 import Assignment_1
from models.assignment_2 import Assignment_2
from models.endsem import Endsem
from models.internals_1 import Internals_1
from models.internals_2 import Internals_2
from models.assignment_1_details import Assignment_1_details
from models.assignment_2_details import Assignment_2_details
from models.internals_1_details import Internals_1_details
from models.internals_2_details import Internals_2_details
from models.endsem_details import Endsem_details
from models.overall import Overall
from models.feedback import Feedback

# Create the flask app.1
app = Flask(__name__)

# Configure the database.
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///rajagiri.db"

# Initialize the app with the extension.
db.init_app(app)

print("Hello world from the models.\n")

# Create the tables in the database.
with app.app_context():
	db.create_all()
	print("Created tables successfully.\n")

# Adding blueprint for homepage.
from routes.home import homes
app.register_blueprint(homes)

# Adding blueprint for signup page.
from routes.signup import signups
app.register_blueprint(signups)

# Adding blueprint for login page.
from routes.login import logins
app.register_blueprint(logins)

# Adding blueprint for classes page.
from routes.classes import classs
app.register_blueprint(classs)

# Adding blueprint for faculty dashboard.
from routes.dash import dashs
app.register_blueprint(dashs)

# Adding blueprint for admin dashboard.
from routes.admindash import adashs
app.register_blueprint(adashs)

# Adding blueprint for students page.
from routes.student import students
app.register_blueprint(students)

# Adding blueprint for about page.
from routes.about import abouts
app.register_blueprint(abouts)

# Adding blueprint for contact page.
from routes.contact import contacts
app.register_blueprint(contacts)

# Adding blueprint for subjects page.
from routes.subject import subjects
app.register_blueprint(subjects)

# Adding blueprint for evaluation method choice page.
from routes.evaluation import evaluations
app.register_blueprint(evaluations)

# Adding blueprint for assignment details page.
from routes.details_assignment import dassign
app.register_blueprint(dassign)

# Adding blueprint for assignment marks input page.
from routes.marks_assignment import massign
app.register_blueprint(massign)

# Adding blueprint for assignment results page.
from routes.result_assignment import rassign
app.register_blueprint(rassign)

# Adding blueprint for internals details page.
from routes.details_internals import dint
app.register_blueprint(dint)

# Adding blueprint for internals marks page.
from routes.marks_internals import mint
app.register_blueprint(mint)

# Adding blueprint for internals results page.
from routes.result_internals import rint
app.register_blueprint(rint)

# Adding blueprint for endsem details page.
from routes.details_endsem import dend
app.register_blueprint(dend)

# Adding blueprint for endsem marks page.
from routes.marks_endsem import mend
app.register_blueprint(mend)

# Adding blueprint for endsem results page.
from routes.result_endsem import rend
app.register_blueprint(rend)

# Adding blueprint for feedback page.
from routes.details_feedback import feedb
app.register_blueprint(feedb)

# Adding blueprint for overall page.
from routes.overall import over
app.register_blueprint(over)

# Adding blueprint for logout.
from routes.logout import logouts
app.register_blueprint(logouts)

# Setting up login.
lm = LoginManager()
lm.init_app(app)

# Setting up how to load a user from a request and from its session.
@lm.user_loader
def user_loader(email):
	theusers = db.session.execute(db.select(Users.email)).all()
	users = []
	for i in theusers:
		users.append(i[0])
	if email not in users:
		return
	user = Auser()
	user.id = email
	return user

@lm.request_loader
def request_loader(request):
	theusers = db.session.execute(db.select(Users.email)).all()
	users = []
	email = request.form.get('email')
	for i in theusers:
		users.append(i[0])
	if email not in users:
		return
	user = Auser()
	user.id = email
	return user

# Handling unauthorized requests.
@lm.unauthorized_handler
def uh():
	flash('The page you tried to access requires you to login.')
	return redirect('login')

# Redirect to homepage from the root URL.
@app.route('/', methods = ['GET', 'POST'])
def hello():
	return redirect(url_for('index.home'))

# Setting secret key is mandatory for flash.
app.secret_key = 'secret_panda'
app.run(
	debug = True
)