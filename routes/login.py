from flask import Blueprint, request, render_template, flash, redirect, session
from models.common import db
from models.users import Users
from models.auser import Auser
from flask_login import login_user

logins = Blueprint('login', __name__)

@logins.route("/login", methods = ["POST", "GET"])
def login():
	if request.method == "GET":
		return render_template("login.html")
	if request.method == "POST":
		if not request.form['user']:
			flash('Username is mandatory!')
			return render_template('login.html')
		if not request.form['user_pass']:
			flash('Password is mandatory!')
			return render_template('login.html')
		username = request.form['user']
		password = request.form['user_pass']
		rows = db.session.execute(db.select(Users.password).filter_by(email = username)).all()
		if len(rows) == 0:
			flash("Invalid login credentials!")
			return render_template('login.html')
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
		return render_template('login.html')