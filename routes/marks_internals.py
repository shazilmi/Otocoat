from flask import render_template, flash, request, Blueprint, redirect, url_for, session
from models.common import db
from models.classes import Classes
from models.subjects import Subjects
from models.students import Students
from models.internals_1 import Internals_1
from models.internals_2 import Internals_2
from models.internals_1_details import Internals_1_details
from models.internals_2_details import Internals_2_details
from flask_login import login_required

mint = Blueprint('marks_internals', __name__)

@mint.route('/marks_internals', methods = ["GET", "POST"])
@login_required
def mark_input():
	a_class = session['theclass']
	a_subject = session['subject']
	evaluation = session['evaluation']
	arows = db.session.execute(db.select(Students.uid).filter_by(theclass = a_class)).all()
	brows = []
	for i in arows:
		brows.append(i[0])
	if request.method == "GET":
		return render_template('internalmarks.html', studentlist = brows)
	if request.method == "POST":
		if evaluation == 'First internals':
			for i in brows:
				qlist = []
				for j in range(1, 16):
					qname = str(i) + '_q' + str(j)
					theq = request.form[qname]
					if theq == '':
						theq = -1
						qlist.append(theq)
					else:
						qlist.append(theq)
				crows = db.session.execute(db.select(Internals_1).filter_by(\
					uid = i, subject = a_subject)).first()
				if crows is None:
					themarks = Internals_1(uid = i, subject = a_subject,
					q1 = qlist[0],
					q2 = qlist[1],
					q3 = qlist[2],
					q4 = qlist[3],
					q5 = qlist[4],
					q6 = qlist[5],
					q7 = qlist[6],
					q8 = qlist[7],
					q9 = qlist[8],
					q10 = qlist[9],
					q11 = qlist[10],
					q12 = qlist[11],
					q13 = qlist[12],
					q14 = qlist[13],
					q15 = qlist[14])
					db.session.add(themarks)
					db.session.commit()
				else:
					crows[0].q1 = qlist[0]
					crows[0].q2 = qlist[1]
					crows[0].q3 = qlist[2]
					crows[0].q4 = qlist[3]
					crows[0].q5 = qlist[4]
					crows[0].q6 = qlist[5]
					crows[0].q7 = qlist[6]
					crows[0].q8 = qlist[7]
					crows[0].q9 = qlist[8]
					crows[0].q10 = qlist[9]
					crows[0].q11 = qlist[10]
					crows[0].q12 = qlist[11]
					crows[0].q13 = qlist[12]
					crows[0].q14 = qlist[13]
					crows[0].q15 = qlist[14]
					db.session.commit()
			return redirect('result_internals')
		if evaluation == 'Second internals':
			for i in brows:
				qlist = []
				for j in range(1, 16):
					qname = str(i) + '_q' + str(j)
					theq = request.form[qname]
					if theq == '':
						theq = -1
						qlist.append(theq)
					else:
						qlist.append(theq)
				crows = db.session.execute(db.select(Internals_2).filter_by(\
					uid = i, subject = a_subject)).first()
				if crows is None:
					themarks = Internals_2(uid = i, subject = a_subject,
					q1 = qlist[0],
					q2 = qlist[1],
					q3 = qlist[2],
					q4 = qlist[3],
					q5 = qlist[4],
					q6 = qlist[5],
					q7 = qlist[6],
					q8 = qlist[7],
					q9 = qlist[8],
					q10 = qlist[9],
					q11 = qlist[10],
					q12 = qlist[11],
					q13 = qlist[12],
					q14 = qlist[13],
					q15 = qlist[14])
					db.session.add(themarks)
					db.session.commit()
				else:
					crows[0].q1 = qlist[0]
					crows[0].q2 = qlist[1]
					crows[0].q3 = qlist[2]
					crows[0].q4 = qlist[3]
					crows[0].q5 = qlist[4]
					crows[0].q6 = qlist[5]
					crows[0].q7 = qlist[6]
					crows[0].q8 = qlist[7]
					crows[0].q9 = qlist[8]
					crows[0].q10 = qlist[9]
					crows[0].q11 = qlist[10]
					crows[0].q12 = qlist[11]
					crows[0].q13 = qlist[12]
					crows[0].q14 = qlist[13]
					crows[0].q15 = qlist[14]
					db.session.commit()
			return redirect('result_internals')