from flask import render_template, flash, request, Blueprint, redirect, url_for, session
from models.common import db
from models.classes import Classes
from models.subjects import Subjects
from models.students import Students
from models.endsem import Endsem
from models.endsem_details import Endsem_details
from models.overall import Overall
from flask_login import login_required

rend = Blueprint('result_endsem', __name__)

@rend.route('/result_endsem', methods = ['GET', 'POST'])
@login_required
def result_endsem():
	a_class = session['theclass']
	a_subject = session['subject']
	arows = db.session.execute(db.select(Students.uid).filter_by(theclass = a_class)).all()
	# print('studentlist:', arows, sep = '\n')
	studentlist = []
	for i in arows:
		studentlist.append(i[0])
	diff = db.session.execute(db.select(Endsem_details.d1, Endsem_details.d2, \
		Endsem_details.d3, Endsem_details.d4, Endsem_details.d5, \
			Endsem_details.d6, Endsem_details.d7, Endsem_details.d8, \
				Endsem_details.d9, Endsem_details.d10, Endsem_details.d11, \
					Endsem_details.d12, Endsem_details.d13, Endsem_details.d14, \
						Endsem_details.d15, Endsem_details.d16, Endsem_details.d17, \
							Endsem_details.d18, Endsem_details.d19, Endsem_details.d20).filter_by(\
							theclass = a_class, subject = a_subject)).first()
	# print('Difficulty list:', diff, sep = '\n')
	co = db.session.execute(db.select(Endsem_details.co1, Endsem_details.co2, \
		Endsem_details.co3, Endsem_details.co4, Endsem_details.co5, \
			Endsem_details.co6, Endsem_details.co7, Endsem_details.co8, \
				Endsem_details.co9, Endsem_details.co10, Endsem_details.co11, \
					Endsem_details.co12, Endsem_details.co13, Endsem_details.co14, \
						Endsem_details.co15, Endsem_details.d16, Endsem_details.d17, \
							Endsem_details.d18, Endsem_details.d19, Endsem_details.d20).filter_by(\
							theclass = a_class, subject = a_subject)).first()
	# print('Co mapped list:', co, sep = '\n')
	colist = []
	for i in range(20):
		if i < 5:
			totalmarks = 3
		else:
			totalmarks = 7
		if diff[i] == 1:
			threshold = 70
		elif diff[i] == 2:
			threshold = 60
		else:
			threshold = 50
		# print('Threshold:', threshold, sep = '\n')
		students = 0
		passed = 0
		for j in studentlist:
			query = db.session.execute(db.select(Endsem.q1, Endsem.q2, Endsem.q3, \
				Endsem.q4, Endsem.q5, Endsem.q6, Endsem.q7, Endsem.q8, \
					Endsem.q9, Endsem.q10, Endsem.q11, Endsem.q12, \
						Endsem.q13, Endsem.q14, Endsem.q15, Endsem.q16, Endsem.q17, \
							Endsem.q18, Endsem.q19, Endsem.q20).filter_by(\
							uid = j, subject = a_subject)).first()
			if query[i] == -1:
				students += 1
			else:
				students += 1
				if (query[i]/totalmarks) * 100 > threshold:
					passed += 1
			#print('Passed, number of students:', passed, students, sep = '\n')
		if students > 0:
			coscore = (passed / students) * 100
			if coscore >= 70:
				colist.append(3)
			elif coscore >= 60:
				colist.append(2)
			else:
				colist.append(1)
		else:
			colist.append(1)
	#print('Co score for each question:', colist, sep = '\n')
	comap = {1:0, 2:0, 3:0, 4:0, 5:0}
	conum = {1:0, 2:0, 3:0, 4:0, 5:0}
	coscorelist = []
	for i in range(len(co)):
		for j in range(1, 6):
			if co[i] == j:
				comap[j] += colist[i]
				conum[j] += 1
	#print('Total score for each co, number of questions for each co:', comap, conum, sep = '\n')
	for k in range(1, 6):
		if conum[k] == 0:
			coscorelist.append(0)
		else:
			coscorelist.append(comap[k] / conum[k])
	theover = db.session.execute(db.select(Overall).filter_by(\
		theclass = a_class, subject = a_subject, evaluation = session['evaluation'])).first()
	if theover is None:
		anover = Overall(theclass = a_class, subject = a_subject, evaluation = session['evaluation'], \
			co1 = coscorelist[0], co2 = coscorelist[1], co3 = coscorelist[2], co4 = coscorelist[3], co5 = coscorelist[4])
		db.session.add(anover)
		db.session.commit()
	else:
		theover[0].co1 = coscorelist[0]
		theover[0].co2 = coscorelist[1]
		theover[0].co3 = coscorelist[2]
		theover[0].co4 = coscorelist[3]
		theover[0].co5 = coscorelist[4]
		db.session.commit()
	return render_template('endsemresults.html', colist = coscorelist)