from flask import render_template, flash, request, Blueprint, redirect, url_for, session
from models.common import db
from models.classes import Classes
from models.subjects import Subjects
from models.assignment_1 import Assignment_1
from models.assignment_2 import Assignment_2

dassign = Blueprint('details_assignment', __name__)

@dassign.route('/details_assignment', methods = ["GET", "POST"])
def details_1():
	theevaluation = session['evaluation']
	theclass = session['theclass']
	thesubject = session['subject']
	if theevaluation == 'Assignment 1':
		
	else:
		return "Huhuhu"