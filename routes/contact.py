from flask import Blueprint, render_template, flash, request, session

contacts = Blueprint('contact', __name__)

@contacts.route('/contact', methods = ["POST", "GET"])
def about():
	if request.method == "GET":
		if session['admin'] == 0:
			return render_template('fcontact.html')
		elif session['admin'] == 1:
			return render_template('acontact.html')
		else:
			return render_template('contact.html')