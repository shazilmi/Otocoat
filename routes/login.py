from flask import Blueprint, request, render_template, flash, redirect
from models.common import db
from models.users import Users

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
			print("No results returned.")
			return render_template('login.html')
		if rows[0][0] == password:
			return redirect("dash")
		flash("Invalid login credentials!")
		print("Wrong password.")
		print(rows[0][0])
		return render_template('login.html')