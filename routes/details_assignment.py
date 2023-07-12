from flask import render_template, flash, request, Blueprint, redirect, url_for, session
from models.common import db
from models.classes import Classes
from models.subjects import Subjects
from models.assignment_1 import Assignment_1
from models.assignment_2 import Assignment_2
from models.assignment_1_details import Assignment_1_details
from models.assignment_2_details import Assignment_2_details

dassign = Blueprint('details_assignment', __name__)

@dassign.route('/details_assignment', methods = ["GET", "POST"])
def details_assignment():
	if request.method == "GET":
		return render_template('assignmentdetails.html')
	if request.method == "POST":
		a_class = session['theclass']
		a_subject = session['subject']
		evaluation = session['evaluation']
		a_difficulty = int(request.form['difficulty'])
		a_score = float(request.form['score'])
		a_co1 = int(request.form['co1'])
		a_co2 = int(request.form['co2'])
		a_co3 = int(request.form['co3'])
		a_co4 = int(request.form['co4'])
		a_co5 = int(request.form['co5'])
		if evaluation == 'Assignment 1':
			assgn_1_details = Assignment_1_details(
                theclass = a_class,
                subject = a_subject,
                difficulty = a_difficulty,
                score = a_score,
                co1 = a_co1,
                co2 = a_co2,
                co3 = a_co3,
                co4 = a_co4,
                co5 = a_co5
            )
			db.session.add(assgn_1_details)
			db.session.commit()
			flash('Assignment details added successfully!')
			session['score'] = a_score
			return redirect('marks_assignment')
		if evaluation == 'Assignment 2':
			assgn_2_details = Assignment_2_details(
                theclass = a_class,
                subject = a_subject,
                difficulty = a_difficulty,
                score = a_score,
                co1 = a_co1,
                co2 = a_co2,
                co3 = a_co3,
                co4 = a_co4,
                co5 = a_co5
            )
			db.session.add(assgn_2_details)
			db.session.commit()
			flash('Assignment details added successfully!')
			session['difficulty'] = a_difficulty
			return redirect('marks_assignment')