from flask import render_template, flash, request, Blueprint, session, redirect, url_for
from models.common import db
from models.classes import Classes
from models.subjects import Subjects
from models.assignment_1_details import Assignment_1_details
from models.assignment_2_details import Assignment_2_details
from models.internals_1_details import Internals_1_details
from models.internals_2_details import Internals_2_details
from models.endsem_details import Endsem_details
from flask_login import login_required

evaluations = Blueprint('marks', __name__)

@evaluations.route('/marks', methods = ["POST", "GET"])
@login_required
def evaluation():
	arows = db.session.execute(db.select(Subjects.subject, Subjects.theclass)).all()
	evallist = ['Assignment 1', 'Assignment 2', 'First internals', 'Second internals', 'Course Feedback', 'Endsem']
	brows = db.session.execute(db.select(Classes.theclass)).all()
	crows = []
	for i in brows:
		crows.append(i[0])
	if request.method == "GET":
		return render_template('marks.html', subjectlist = arows, \
			evaluationlist = evallist, classlist = crows)
	if request.method == "POST":
		thesubject = request.form['subject']
		theclass = request.form['classes']
		theevaluation = request.form['evaluation']
		asubjectlist = db.session.execute(db.select(Subjects.subject)).all()
		thesubjectlist = []
		for i in asubjectlist:
			thesubjectlist.append(i[0])
		thecheck = 0
		for i in arows:
			if i[0] == thesubject and i[1] == theclass:
				thecheck += 1
		if thecheck == 0:
			flash("The given subject is not taught at the given class. \
				Kindly check the input or go to the subject page.")
			return render_template("marks.html", evaluationlist = evallist, subjectlist = arows, \
				classlist = crows)
		session['theclass'] = theclass
		session['subject'] = thesubject
		session['evaluation'] = theevaluation
		if theevaluation == 'Assignment 1' or theevaluation == 'Assignment 2':
			return redirect('details_assignment')
		if theevaluation == 'First internals' or theevaluation == 'Second internals':
			return redirect('details_internals')
		if theevaluation == 'Course Feedback':
			return redirect('feedback')
		return redirect('marks_endsem')