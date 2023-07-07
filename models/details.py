from flask import flash, request, redirect, url_for, session, Blueprint
from models.common import db
from models.classes import Classes
from models.subjects import Subjects
from models.assignment_1 import Assignment_1
from models.assignment_2 import Assignment_2
from models.endsem import Endsem
from models.internals_1 import Internals_1
from models.internals_2 import Internals_2

detailss = Blueprint('details', __name__)
@detailss.route("/details", methods = ["GET", "POST"])
def details():
	if not session['evaluation'] or not session['theclass'] or not session['subject']:
		flash("Improper input, try again.")
		return redirect(url_for('marks'))
	theevaluation = session['evaluation']
	theclass = session['theclass']
	thesubject = session['subject']
	evallist = ['Assignment 1', 'Assignment 2', 'Internals 1', 'Internals 2', 'Endsem']