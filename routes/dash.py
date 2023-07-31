from flask import Blueprint, request, render_template, flash, session, redirect
from models.common import db
from flask_login import login_required

dashs = Blueprint('dash', __name__)

@dashs.route("/dash", methods = ["POST", "GET"])
@login_required	
def dashboard():
	if request.method == "GET":
		if session['admin'] == 1:
			flash('Unauthorized!')
			return redirect('adash')
		return render_template("dash.html")