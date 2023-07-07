from flask import Blueprint, render_template, flash, request

abouts = Blueprint('about', __name__)

@abouts.route('/about', methods = ["POST", "GET"])
def about():
	if request.method == "GET":
		return render_template('about.html')