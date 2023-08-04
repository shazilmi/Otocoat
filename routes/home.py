# Importing necessary libraries.
from flask import Blueprint, request, render_template, flash, session, redirect
from models.common import db
from models.users import Users
from models.auser import Auser
from flask_login import login_user

# Create a blueprint for the homepage.
homes = Blueprint('index', __name__)

# Define the function to be called when homepage is requested.
@homes.route('/index', methods = ["POST", "GET"])
def home():
	if request.method == "GET":
		print('Something happened.')
		if session['admin'] == 0:
			print("ivide ethi")
			return render_template('findex.html')
		elif session['admin'] == 1:
			print("Ivide ethi 3")
			return render_template('aindex.html')
		else:
			return render_template('index.html')
	if request.method == "POST":
		if not request.form['user']:
			flash('Username is mandatory!')
			return render_template('index.html')
		if not request.form['user_pass']:
			flash('Password is mandatory!')
			return render_template('index.html')
		username = request.form['user']
		password = request.form['user_pass']
		rows = db.session.execute(db.select(Users.password).filter_by(email = username)).all()
		if len(rows) == 0:
			flash("Invalid login credentials!")
			return render_template('index.html')
		if rows[0][0] == password:
			auser = Auser()
			auser.id = username
			login_user(auser)
			isadmin = db.session.execute(db.select(Users.admin).filter_by(email = username)).first()
			if isadmin[0] == 0:
				session['admin'] = 0
				return redirect("dash")
			else:
				session['admin'] = 1
				return redirect("adash")
		flash("Invalid login credentials!")
		return render_template('index.html')