from flask import render_template, flash, request, Blueprint, redirect, url_for, session
from models.common import db
from models.classes import Classes
from models.subjects import Subjects
from models.students import Students
from models.assignment_1 import Assignment_1
from models.assignment_2 import Assignment_2
from models.assignment_1_details import Assignment_1_details
from models.assignment_2_details import Assignment_2_details
from models.overall import Overall
from flask_login import login_required

rassign = Blueprint('result_assignment', __name__)

@rassign.route('/result_assignment', methods = ["GET", "POST"])
@login_required
def thefunc():
	a_class = session['theclass']
	a_subject = session['subject']
	evaluation = session['evaluation']
	arows = db.session.execute(db.select(Students.uid).filter_by(theclass = a_class)).all()
	studentlist = []
	for i in arows:
		studentlist.append(i[0])
	if evaluation == 'Assignment 1':
		diff = db.session.execute(db.select(Assignment_1_details.difficulty).filter_by(\
			theclass = a_class, subject = a_subject)).all()
		difficulty = diff[0][0]
		total = db.session.execute(db.select(Assignment_1_details.score).filter_by(\
			theclass = a_class, subject = a_subject)).all()
		score = total[0][0]
		students = len(studentlist)
		marklist = []
		for i in studentlist:
			themarks = db.session.execute(db.select(Assignment_1.marks).filter_by(\
				uid = i, subject = a_subject)).all()
			try:
				marks = themarks[0][0]
				marklist.append(marks)
			except:
				pass
		if difficulty == 1:
			threshold = 70
		elif difficulty == 2:
			threshold = 60
		elif difficulty == 3:
			threshold = 50
		cutoff = 0
		for i in marklist:
			percent = i / score
			if percent * 100 > threshold:
				cutoff += 1
		percentage = cutoff / students
		percentage *= 100
		if percentage >= 70:
			co_score = 3
		elif percentage >= 60:
			co_score = 2
		else:
			co_score = 1
		alist = db.session.execute(db.select(Assignment_1_details.co1, Assignment_1_details.co2, \
			Assignment_1_details.co3, Assignment_1_details.co4, Assignment_1_details.co5).filter_by(\
				theclass = a_class, subject = a_subject)).all()
		colist = []
		co = 0
		for i in alist[0]:
			co += 1
			if i == 1:
				colist.append(co)
		blist = []
		for i in range(len(alist[0])):
			if alist[0][i] == 1:
				blist.append(co_score)
			else:
				blist.append(0)
		theover = db.session.execute(db.select(Overall).filter_by(\
			theclass = a_class, subject = a_subject, evaluation = evaluation)).first()
		if theover is None:
			anover = Overall(theclass = a_class, subject = a_subject, evaluation = evaluation, \
				co1 = blist[0], co2 = blist[1], co3 = blist[2], co4 = blist[3], co5 = blist[4])
			db.session.add(anover)
			db.session.commit()
		else:
			theover[0].co1 = blist[0]
			theover[0].co2 = blist[1]
			theover[0].co3 = blist[2]
			theover[0].co4 = blist[3]
			theover[0].co5 = blist[4]
			db.session.commit()
		if request.method == "GET":
			return render_template("assignmentresults.html", percent = percentage, colist = colist, \
				score = co_score)
	if evaluation == 'Assignment 2':
		diff = db.session.execute(db.select(Assignment_2_details.difficulty).filter_by(\
			theclass = a_class, subject = a_subject)).all()
		difficulty = diff[0][0]
		total = db.session.execute(db.select(Assignment_2_details.score).filter_by(\
			theclass = a_class, subject = a_subject)).all()
		score = total[0][0]
		students = len(studentlist)
		marklist = []
		for i in studentlist:
			themarks = db.session.execute(db.select(Assignment_2.marks).filter_by(\
				uid = i, subject = a_subject)).all()
			try:
				marks = themarks[0][0]
				marklist.append(marks)
			except:
				pass
		if difficulty == 1:
			threshold = 70
		elif difficulty == 2:
			threshold = 60
		elif difficulty == 3:
			threshold = 50
		cutoff = 0
		for i in marklist:
			percent = i / score
			if percent * 100 > threshold:
				cutoff += 1
		percentage = cutoff / students
		percentage *= 100
		if percentage >= 70:
			co_score = 3
		elif percentage >= 60:
			co_score = 2
		else:
			co_score = 1
		alist = db.session.execute(db.select(Assignment_2_details.co1, Assignment_2_details.co2, \
			Assignment_2_details.co3, Assignment_2_details.co4, Assignment_2_details.co5).filter_by(\
				theclass = a_class, subject = a_subject)).all()
		colist = []
		co = 0
		for i in alist[0]:
			co += 1
			if i == 1:
				colist.append(co)
		blist = []
		for i in range(len(alist[0])):
			if alist[0][i] == 1:
				blist.append(co_score)
			else:
				blist.append(0)
		theover = db.session.execute(db.select(Overall).filter_by(\
			theclass = a_class, subject = a_subject, evaluation = evaluation)).first()
		if theover is None:
			anover = Overall(theclass = a_class, subject = a_subject, evaluation = evaluation, \
				co1 = blist[0], co2 = blist[1], co3 = blist[2], co4 = blist[3], co5 = blist[4])
			db.session.add(anover)
			db.session.commit()
		else:
			theover[0].co1 = blist[0]
			theover[0].co2 = blist[1]
			theover[0].co3 = blist[2]
			theover[0].co4 = blist[3]
			theover[0].co5 = blist[4]
			db.session.commit()
		if request.method == "GET":
			return render_template("assignmentresults.html", percent = percentage, colist = colist, \
				score = co_score)