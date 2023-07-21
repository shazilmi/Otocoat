from flask import render_template, flash, request, Blueprint, redirect, url_for, session
from models.common import db
from models.classes import Classes
from models.subjects import Subjects
from models.students import Students
from models.internals_1 import Internals_1
from models.internals_2 import Internals_2
from models.internals_1_details import Internals_1_details
from models.internals_2_details import Internals_2_details

rint = Blueprint('result_internals', __name__)

@rint.route('/result_internals', methods = ["GET", "POST"])
def result_internals():
	a_class = session['theclass']
	a_subject = session['subject']
	evaluation = session['evaluation']
	arows = db.session.execute(db.select(Students.uid).filter_by(theclass = a_class)).all()
	print('studentlist:', arows, sep = '\n')
	studentlist = []
	for i in arows:
		studentlist.append(i[0])
	if evaluation == 'First internals':
		diff = db.session.execute(db.select(Internals_1_details.d1, Internals_1_details.d2, \
			Internals_1_details.d3, Internals_1_details.d4, Internals_1_details.d5, \
				Internals_1_details.d6, Internals_1_details.d7, Internals_1_details.d8, \
					Internals_1_details.d9, Internals_1_details.d10, Internals_1_details.d11, \
						Internals_1_details.d12, Internals_1_details.d13, Internals_1_details.d14, \
							Internals_1_details.d15).filter_by(\
								theclass = a_class, subject = a_subject)).first()
		print('Difficulty list:', diff, sep = '\n')
		co = db.session.execute(db.select(Internals_1_details.co1, Internals_1_details.co2, \
			Internals_1_details.co3, Internals_1_details.co4, Internals_1_details.co5, \
				Internals_1_details.co6, Internals_1_details.co7, Internals_1_details.co8, \
					Internals_1_details.co9, Internals_1_details.co10, Internals_1_details.co11, \
						Internals_1_details.co12, Internals_1_details.co13, Internals_1_details.co14, \
							Internals_1_details.co15).filter_by(\
								theclass = a_class, subject = a_subject)).first()
		print('Co mapped list:', co, sep = '\n')
		colist = []
		for i in range(15):
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
			print('Threshold:', threshold, sep = '\n')
			students = 0
			passed = 0
			for j in studentlist:
				query = db.session.execute(db.select(Internals_1.q1, Internals_1.q2, Internals_1.q3, \
					Internals_1.q4, Internals_1.q5, Internals_1.q6, Internals_1.q7, Internals_1.q8, \
						Internals_1.q9, Internals_1.q10, Internals_1.q11, Internals_1.q12, \
							Internals_1.q13, Internals_1.q14, Internals_1.q15).filter_by(\
								uid = j, subject = a_subject)).first()
				if query[i] is None:
					pass
				else:
					students += 1
					if (query[i]/totalmarks) * 100 > threshold:
						passed += 1
				print('Passed, number of students:', passed, students, sep = '\n')
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
		print('Co score for each question:', colist, sep = '\n')
		comap = {1:0, 2:0, 3:0, 4:0, 5:0}
		conum = {1:0, 2:0, 3:0, 4:0, 5:0}
		coscorelist = []
		for i in range(len(co)):
			for j in range(1, 6):
				if co[i] == j:
					comap[j] += colist[i]
					conum[j] += 1
		print('Total score for each co, number of questions for each co:', comap, conum, sep = '\n')
		for k in range(1, 6):
			if conum[k] == 0:
				coscorelist.append(0)
			else:
				coscorelist.append(comap[k] / conum[k])
		print('Co score for each co:', coscorelist, sep = '\n')
		return render_template('internalresults.html', colist = coscorelist)
	if evaluation == 'Second internals':
		diff = db.session.execute(db.select(Internals_2_details.d1, Internals_2_details.d2, \
			Internals_2_details.d3, Internals_2_details.d4, Internals_2_details.d5, \
				Internals_2_details.d6, Internals_2_details.d7, Internals_2_details.d8, \
					Internals_2_details.d9, Internals_2_details.d10, Internals_2_details.d11, \
						Internals_2_details.d12, Internals_2_details.d13, Internals_2_details.d14, \
							Internals_2_details.d15).filter_by(\
								theclass = a_class, subject = a_subject)).first()
		co = db.session.execute(db.select(Internals_2_details.co1, Internals_2_details.co2, \
			Internals_2_details.co3, Internals_2_details.co4, Internals_2_details.co5, \
				Internals_2_details.co6, Internals_2_details.co7, Internals_2_details.co8, \
					Internals_2_details.co9, Internals_2_details.co10, Internals_2_details.co11, \
						Internals_2_details.co12, Internals_2_details.co13, Internals_2_details.co14, \
							Internals_2_details.co15).filter_by(\
								theclass = a_class, subject = a_subject)).first()
		colist = []
		for i in range(15):
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
			students = 0
			passed = 0
			for j in studentlist:
				query = db.session.execute(db.select(Internals_2.q1, Internals_2.q2, Internals_2.q3, \
					Internals_2.q4, Internals_2.q5, Internals_2.q6, Internals_2.q7, Internals_2.q8, \
						Internals_2.q9, Internals_2.q10, Internals_2.q11, Internals_2.q12, \
							Internals_2.q13, Internals_2.q14, Internals_2.q15).filter_by(\
								uid = j, subject = a_subject)).first()
				if query[i] is None:
					pass
				else:
					students += 1
					if (query[i]/totalmarks) * 100 > threshold:
						passed += 1
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
		comap = {1:0, 2:0, 3:0, 4:0, 5:0}
		conum = {1:0, 2:0, 3:0, 4:0, 5:0}
		coscorelist = []
		for i in range(len(co)):
			for j in range(1, 6):
				if co[i] == j:
					comap[j] += colist[i]
					conum[j] += 1
		for k in range(1, 6):
			if conum[k] == 0:
				coscorelist.append(0)
			else:
				coscorelist.append(comap[k] / conum[k])
		print(coscorelist)
		return render_template('internalresults.html', colist = coscorelist)