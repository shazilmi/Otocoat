from flask import Blueprint, request, render_template, flash
from models.common import db
from flask_login import login_required

dashs = Blueprint('dash', __name__)

@dashs.route("/dash", methods = ["POST", "GET"])
@login_required	
def dashboard():
	if request.method == "GET":
		return render_template("dash.html")
	if request.method == "POST":
		if not request.form['branch']:
			flash('class is mandatory!')
			return render_template('dash.html')
		if not request.form['evaluation']:
			flash('evaluation is mandatory!')
			return render_template('dash.html')
		branch = request.form['user']
		evaluation = request.form['user_pass']
		if evaluation == "internal 1":
			return render_template('internal1.html')
		if evaluation == "internal 2":
			return render_template('internal 2.html')
		if evaluation == "endsem":
			return render_template('endsem.html')
		if evaluation == "assignments":
			return render_template('assignments.html')