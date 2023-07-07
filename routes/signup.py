from flask import Flask, request, render_template, flash, redirect, url_for, Blueprint
from models.common import db
from models.users import Users

signups = Blueprint('signup', __name__)

@signups.route("/signup", methods = ["POST", "GET"])
def signup():
	if request.method == "GET":
		return render_template("signup.html")
	if request.method == "POST":
		if not request.form['user']:
			flash("Username is mandatory!")
			return render_template('signup.html')
		if not request.form['pass1'] or not request.form['pass2']:
			flash("Password is mandatory!")
			return render_template('signup.html')
		username = request.form['user']
		pass1 = request.form['pass1']
		pass2 = request.form['pass2']
		if pass1 != pass2:
			flash("Given passwords must match!")
			return render_template('signup.html')
		rows = db.session.execute(db.select(Users.password).filter_by(email = username)).all()
		if len(rows) == 0:
			user = Users(email = username, password = pass1)
			db.session.add(user)
			db.session.commit()
			flash('Signup successful! Kindly login with your credentials.')
			return render_template('signup.html')
		else:
			flash("Credentials already in use!")
			return render_template('signup.html')