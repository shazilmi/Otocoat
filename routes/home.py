# Importing necessary libraries.
from flask import Blueprint, request, render_template

# Create a blueprint for the homepage.
homes = Blueprint('index', __name__)

# Define the function to be called when homepage is requested.
@homes.route('/index', methods = ["POST", "GET"])
def home():
	if request.method == "GET":
		return render_template("index.html")