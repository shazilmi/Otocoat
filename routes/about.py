from flask import Blueprint, render_template, flash, request, session

abouts = Blueprint('about', __name__)

@abouts.route('/about', methods = ["POST", "GET"])
def about():
	if request.method == "GET":
		try:
			if session['admin'] == 0:
				return render_template('fabout.html')
			else:
				return render_template('aabout.html')
		except KeyError:
			return render_template('about.html')