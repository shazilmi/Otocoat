# Importing the necessary packages.
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Import the SQLAlchemy extension.
from models.common import db

# Import the created models and 
from models.users import Users
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

# Adding blueprint for dashboard.
from routes.dash import dashs
app.register_blueprint(dashs)

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

# Redirect to homepage from the root URL.
@app.route('/', methods = ['GET', 'POST'])
def hello():
	return redirect(url_for('index.home'))

# Setting secret key is mandatory for flash.
app.secret_key = 'secret_panda'
app.run(
	debug = True
)