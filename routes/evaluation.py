from flask import render_template, flash, request, Blueprint, session, redirect, url_for
from models.common import db
from models.classes import Classes
from models.subjects import Subjects

evaluations = Blueprint('marks', __name__)

@evaluations.route('/marks', methods = ["POST", "GET"])
def evaluation():
	arows = db.session.execute(db.select(Subjects.subject, Subjects.theclass)).all()
	evallist = ['Assignment 1', 'Assignment 2', 'First internals', 'Second internals', 'Endsem']
	if request.method == "GET":
		return render_template('marks.html', subjectlist = arows, \
			evaluationlist = evallist)
	if request.method == "POST":
		if not request.form['subject']:
			flash("Subject is mandatory!")
			return render_template("marks.html", evaluationlist = evallist, subjectlist = arows)
		if not request.form['classes']:
			flash("Class is mandatory!")
			return render_template("marks.html", evaluationlist = evallist, subjectlist = arows)
		if not request.form['evaluation']:
			flash("Evaluation method is mandatory!")
			return render_template("marks.html", evaluationlist = evallist, subjectlist = arows)
		thesubject = request.form['subject']
		theclass = request.form['classes']
		theevaluation = request.form['evaluation']
		asubjectlist = db.session.execute(db.select(Subjects.subject)).all()
		thesubjectlist = []
		for i in asubjectlist:
			thesubjectlist.append(i[0])
		if thesubject not in thesubjectlist:
			flash("Invalid subject entered!")
			return render_template("marks.html", evaluationlist = evallist, subjectlist = arows)
		aclasslist = db.session.execute(db.select(Subjects.theclass)).all()
		theclasslist = []
		for i in aclasslist:
			theclasslist.append(i[0])
		if theclass not in theclasslist:
			flash("Invalid class entered!")
			return render_template("marks.html", evaluationlist = evallist, subjectlist = arows)
		if theevaluation not in evallist:
			flash("Invalid evaluation method entered!")
			return render_template("marks.html", evaluationlist = evallist, subjectlist = arows)
		thecheck = 0
		for i in arows:
			if i[0] == thesubject and i[1] == theclass:
				thecheck += 1
		if thecheck == 0:
			flash("The given subject is not taught at the given class. \
				Kindly check the input or go to the subject page.")
			return render_template("marks.html", evaluationlist = evallist, subjectlist = arows)
		session['theclass'] = theclass
		session['subject'] = thesubject
		session['evaluation'] = theevaluation
		if theevaluation == 'Assignment 1' or theevaluation == 'Assignment 2':
			return redirect(url_for('details_assignment'))
		if theevaluation == 'First internals' or theevaluation == 'Second internals':
			return redirect(url_for('details_internals'))
		return redirect(url_for('details_endsem'))