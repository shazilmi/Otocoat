from flask import render_template, flash, Blueprint, redirect, url_for, session, request
from models.common import db
from models.overall import Overall
from models.subjects import Subjects
from models.classes import Classes
from flask_login import login_required

over = Blueprint('overall', __name__)

@over.route('/overall', methods = ["GET", "POST"])
@login_required
def overall():
	arows = db.session.execute(db.select(Subjects.subject, Subjects.theclass)).all()
	brows = db.session.execute(db.select(Classes.theclass)).all()
	crows = []
	for i in brows:
		crows.append(i[0])
	if request.method == "GET":
		return render_template('choice.html', subjectlist = arows, \
			classlist = crows)
	if request.method == "POST":
		a_subject = request.form['subject']
		a_class = request.form['classes']
		asubjectlist = db.session.execute(db.select(Subjects.subject)).all()
		thesubjectlist = []
		for i in asubjectlist:
			thesubjectlist.append(i[0])
		thecheck = 0
		for i in arows:
			if i[0] == a_subject and i[1] == a_class:
				thecheck += 1
		if thecheck == 0:
			flash("The given subject is not taught at the given class. \
				Kindly check the input or go to the subject page.")
			return render_template("choice.html", subjectlist = arows, \
				classlist = crows)
		evallist = ['Assignment 1', 'Assignment 2', 'First internals', 'Second internals', 'Course Feedback', 'Endsem']
		nolist = []
		for i in evallist:
			thecheck = db.session.execute(db.select(Overall).filter_by(\
				theclass = a_class, subject = a_subject, evaluation = i)).first()
			if thecheck is None:
				nolist.append(i)
		if nolist != []:
			return render_template('overall.html', colist = nolist)
		else:
			pass