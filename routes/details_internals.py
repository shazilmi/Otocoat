from flask import render_template, flash, request, Blueprint, redirect, url_for, session
from models.common import db
from models.classes import Classes
from models.subjects import Subjects
from models.internals_1 import Internals_1
from models.internals_2 import Internals_2
from models.internals_1_details import Internals_1_details
from models.internals_2_details import Internals_2_details
from flask_login import login_required

dint = Blueprint('details_internals', __name__)

@dint.route('/details_internals', methods = ["GET", "POST"])
@login_required
def details_internals():
	if request.method == "GET":
		return render_template('internaldetails.html')
	if request.method == "POST":
		a_class = session['theclass']
		a_subject = session['subject']
		evaluation = session['evaluation']
		dlist = []
		colist = []
		for i in range(1, 16):
			dname = 'd' + str(i)
			coname = 'co' + str(i)
			dlist.append(request.form[dname])
			colist.append(request.form[coname])
		if evaluation == 'First internals':
			thecheck = db.session.execute(db.select(Internals_1_details).filter_by(theclass = a_class, \
				subject = a_subject)).first()
			if thecheck is None:
				int_1_details = Internals_1_details(
					theclass = a_class,
					subject = a_subject,
					d1 = dlist[0],
					co1 = colist[0],
					d2 = dlist[1],
					co2 = colist[1],
					d3 = dlist[2],
					co3 = colist[2],
					d4 = dlist[3],
					co4 = colist[3],
					d5 = dlist[4],
					co5 = colist[4],
					d6 = dlist[5],
					co6 = colist[5],
					d7 = dlist[6],
					co7 = colist[6],
					d8 = dlist[7],
					co8 = colist[7],
					d9 = dlist[8],
					co9 = colist[8],
					d10 = dlist[9],
					co10 = colist[9],
					d11 = dlist[10],
					co11 = colist[10],
					d12 = dlist[11],
					co12 = colist[11],
					d13 = dlist[12],
					co13 = colist[12],
					d14 = dlist[13],
					co14 = colist[13],
					d15 = dlist[14],
					co15 = colist[14]
				)
				db.session.add(int_1_details)
				db.session.commit()
				flash('Internals details added successfully!')
				return redirect('marks_internals')
			else:
				thecheck[0].d1 = dlist[0]
				thecheck[0].co1 = colist[0]
				thecheck[0].d2 = dlist[1]
				thecheck[0].co2 = colist[1]
				thecheck[0].d3 = dlist[2]
				thecheck[0].co3 = colist[2]
				thecheck[0].d4 = dlist[3]
				thecheck[0].co4 = colist[3]
				thecheck[0].d5 = dlist[4]
				thecheck[0].co5 = colist[4]
				thecheck[0].d6 = dlist[5]
				thecheck[0].co6 = colist[5]
				thecheck[0].d7 = dlist[6]
				thecheck[0].co7 = colist[6]
				thecheck[0].d8 = dlist[7]
				thecheck[0].co8 = colist[7]
				thecheck[0].d9 = dlist[8]
				thecheck[0].co9 = colist[8]
				thecheck[0].d10 = dlist[9]
				thecheck[0].co10 = colist[9]
				thecheck[0].d11 = dlist[10]
				thecheck[0].co11 = colist[10]
				thecheck[0].d12 = dlist[11]
				thecheck[0].co12 = colist[11]
				thecheck[0].d13 = dlist[12]
				thecheck[0].co13 = colist[12]
				thecheck[0].d14 = dlist[13]
				thecheck[0].co14 = colist[13]
				thecheck[0].d15 = dlist[14]
				thecheck[0].co15 = colist[14]
				db.session.commit()
				flash('Internals details updated successfully!')
				return redirect('marks_internals')
		if evaluation == 'Second internals':
			thecheck = db.session.execute(db.select(Internals_2_details).filter_by(theclass = a_class, \
				subject = a_subject)).first()
			if thecheck is None:
				int_2_details = Internals_2_details(
					theclass = a_class,
					subject = a_subject,
					d1 = dlist[0],
					co1 = colist[0],
					d2 = dlist[1],
					co2 = colist[1],
					d3 = dlist[2],
					co3 = colist[2],
					d4 = dlist[3],
					co4 = colist[3],
					d5 = dlist[4],
					co5 = colist[4],
					d6 = dlist[5],
					co6 = colist[5],
					d7 = dlist[6],
					co7 = colist[6],
					d8 = dlist[7],
					co8 = colist[7],
					d9 = dlist[8],
					co9 = colist[8],
					d10 = dlist[9],
					co10 = colist[9],
					d11 = dlist[10],
					co11 = colist[10],
					d12 = dlist[11],
					co12 = colist[11],
					d13 = dlist[12],
					co13 = colist[12],
					d14 = dlist[13],
					co14 = colist[13],
					d15 = dlist[14],
					co15 = colist[14]
				)
				db.session.add(int_2_details)
				db.session.commit()
				flash('Internals details added successfully!')
				return redirect('marks_internals')
			else:
				thecheck[0].d1 = dlist[0]
				thecheck[0].co1 = colist[0]
				thecheck[0].d2 = dlist[1]
				thecheck[0].co2 = colist[1]
				thecheck[0].d3 = dlist[2]
				thecheck[0].co3 = colist[2]
				thecheck[0].d4 = dlist[3]
				thecheck[0].co4 = colist[3]
				thecheck[0].d5 = dlist[4]
				thecheck[0].co5 = colist[4]
				thecheck[0].d6 = dlist[5]
				thecheck[0].co6 = colist[5]
				thecheck[0].d7 = dlist[6]
				thecheck[0].co7 = colist[6]
				thecheck[0].d8 = dlist[7]
				thecheck[0].co8 = colist[7]
				thecheck[0].d9 = dlist[8]
				thecheck[0].co9 = colist[8]
				thecheck[0].d10 = dlist[9]
				thecheck[0].co10 = colist[9]
				thecheck[0].d11 = dlist[10]
				thecheck[0].co11 = colist[10]
				thecheck[0].d12 = dlist[11]
				thecheck[0].co12 = colist[11]
				thecheck[0].d13 = dlist[12]
				thecheck[0].co13 = colist[12]
				thecheck[0].d14 = dlist[13]
				thecheck[0].co14 = colist[13]
				thecheck[0].d15 = dlist[14]
				thecheck[0].co15 = colist[14]
				db.session.commit()
				flash('Internals details updated successfully!')
				return redirect('marks_internals')