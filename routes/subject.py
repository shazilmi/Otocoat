from flask import render_template, flash, Blueprint, request
from models.common import db
from models.classes import Classes
from models.subjects import Subjects
from flask_login import login_required

subjects = Blueprint('subject', __name__)

@subjects.route('/subject', methods = ["POST", "GET"])
@login_required
def subject():
	if request.method == "GET":
		rows = db.session.execute(db.select(Classes.theclass)).all()
		therows = []
		for i in rows:
			j = i[0]
			therows.append(j)
		arows = db.session.execute(db.select(Subjects.subject, Subjects.theclass)).all()
		return render_template('subject.html', alist = therows, subjectlist = arows)
	if request.method == "POST":
		rows = db.session.execute(db.select(Classes.theclass)).all()
		therows = []
		for i in rows:
			j = i[0]
			therows.append(j)
		arows = db.session.execute(db.select(Subjects.subject, Subjects.theclass)).all()
		if not request.form['name']:
			flash("Subject name is mandatory!")
			return render_template('subject.html', alist = therows, subjectlist = arows)
		if not request.form['theclass']:
			flash("Class is mandatory!")
			return render_template('subject.html', alist = therows, subjectlist = arows)
		thename = request.form['name'].lower()
		aclass = request.form['theclass']
		if aclass not in therows:
			flash("Invalid class entered!")
			return render_template('subject.html', alist = therows, subjectlist = arows)
		thesubjects = db.session.execute(db.select(Subjects.theclass, Subjects.subject)).all()
		for i in thesubjects:
			if i[0] == aclass and i[1] == thename:
				flash("Subject already exists!")
				return render_template("subject.html", alist = therows, subjectlist = arows)
		asubject = Subjects(theclass = aclass, subject = thename)
		db.session.add(asubject)
		db.session.commit()
		flash("Subject added successfully!")
		return render_template('subject.html', alist = therows, subjectlist = arows)