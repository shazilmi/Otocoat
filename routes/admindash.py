from flask import Blueprint, request, render_template, flash, session, redirect
from models.common import db
from flask_login import login_required

adashs = Blueprint('adash', __name__)

@adashs.route("/adash", methods = ["POST", "GET"])
@login_required	
def dashboard():
	if request.method == 'GET':
		if session['admin'] == 0:
			flash("Unauthorized!")
			return redirect('dash')
		else:
			return render_template('adash.html')