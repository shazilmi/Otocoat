from flask import render_template, flash, request, Blueprint, redirect, url_for, session
from models.common import db
from models.classes import Classes
from models.subjects import Subjects
from models.students import Students
from models.assignment_1 import Assignment_1
from models.assignment_2 import Assignment_2
from models.assignment_1_details import Assignment_1_details
from models.assignment_2_details import Assignment_2_details

massign = Blueprint('marks_assignment', __name__)

@massign.route('/marks_assignment', methods = ["GET", "POST"])
def mark_input():
	a_class = session['theclass']
	a_subject = session['subject']
	evaluation = session['evaluation']
	thescore = session['score']
	arows = db.session.execute(db.select(Students.uid).filter_by(theclass = a_class)).all()
	brows = []
	for i in arows:
		brows.append(i[0])
	if request.method == "GET":
		return render_template('assignmentmarks.html', studentlist = brows, score = thescore)
	if request.method == "POST":
		if evaluation == 'Assignment 1':
			for i in brows:
				thename = 'mark_' + str(i)
				total = request.form[thename]
				crows = db.session.execute(db.select(Assignment_1).filter_by(\
					uid = i, subject = a_subject)).first()
				if crows is None:
					anobject = Assignment_1(uid = i, subject = a_subject, marks = total)
					db.session.add(anobject)
					db.session.commit()
					return redirect('result_assignment')
				if len(crows) == 0:
					anobject = Assignment_1(uid = i, subject = a_subject, marks = total)
					db.session.add(anobject)
					db.session.commit()
					return redirect('result_assignment')
				else:
					crows[0].marks = total
					db.session.commit()
			return redirect('result_assignment')
		if evaluation == 'Assignment 2':
			for i in brows:
				thename = 'mark_' + str(i)
				total = request.form[thename]
				crows = db.session.execute(db.select(Assignment_2).filter_by(\
					uid = i, subject = a_subject)).first()
				if crows is None:
					anobject = Assignment_2(uid = i, subject = a_subject, marks = total)
					db.session.add(anobject)
					db.session.commit()
					return redirect('result_assignment')
				if len(crows) == 0:
					anobject = Assignment_2(uid = i, subject = a_subject, marks = total)
					db.session.add(anobject)
					db.session.commit()
					return redirect('result_assignment')
				else:
					crows[0].marks = total
					db.session.commit()
			return redirect('result_assignment')