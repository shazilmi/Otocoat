from flask import Blueprint, render_template, flash, request

contacts = Blueprint('contact', __name__)

@contacts.route('/contact', methods = ["POST", "GET"])
def about():
	if request.method == "GET":
		return render_template('contact.html')