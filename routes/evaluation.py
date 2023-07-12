from flask import render_template, flash, request, Blueprint, session, redirect, url_for
from models.common import db
from models.classes import Classes
from models.subjects import Subjects
from models.assignment_1_details import Assignment_1_details
from models.assignment_2_details import Assignment_2_details

evaluations = Blueprint('marks', __name__)

@evaluations.route('/marks', methods = ["POST", "GET"])
def evaluation():
	arows = db.session.execute(db.select(Subjects.subject, Subjects.theclass)).all()
	evallist = ['Assignment 1', 'Assignment 2', 'First internals', 'Second internals', 'Endsem']
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
		if theevaluation == 'Assignment 1':
			thecheck = db.session.execute(db.select(\
				Assignment_1_details.theclass, Assignment_1_details.subject).filter_by(\
					theclass = theclass, subject = thesubject)).all()
			if len(thecheck) == 0:
				return redirect('details_assignment')
			else:
				sc = db.session.execute(db.select(Assignment_1_details.score).filter_by(\
					theclass = theclass, subject = thesubject)).all()
				thescore = sc[0][0]
				session['score'] = thescore
				return redirect('marks_assignment')
		if theevaluation == 'Assignment 2':
			thecheck = db.session.execute(db.select(\
				Assignment_2_details.theclass, Assignment_2_details.subject).filter_by(\
					theclass = theclass, subject = thesubject)).all()
			if len(thecheck) == 0:
				return redirect('details_assignment')
			else:
				return redirect('marks_assignment')
		if theevaluation == 'First internals' or theevaluation == 'Second internals':
			return redirect('details_internals')
		return redirect('endsem_details')