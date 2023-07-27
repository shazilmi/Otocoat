from flask import render_template, flash, request, Blueprint
from models.common import db
from models.classes import Classes
from flask_login import login_required

classs = Blueprint('class', __name__)

@classs.route("/class", methods = ["GET", "POST"])
@login_required
def classes():
	if request.method == "GET":
		rows = db.session.execute(db.select(Classes.theclass)).all()
		therows = []
		for i in rows:
			j = i[0]
			therows.append(j)
		return render_template('class.html', existing = therows)
	if request.method == "POST":
		name = request.form['name']
		rows = db.session.execute(db.select(Classes.theclass)).all()
		for i in rows:
			if i[0] == name:
				flash("Class already exists!")
				therows = []
				for i in rows:
					j = i[0]
					therows.append(j)
				return render_template("class.html", existing = therows)
		aclass = Classes(theclass = name)
		db.session.add(aclass)
		db.session.commit()
		flash("Class added!")
		rows = db.session.execute(db.select(Classes.theclass)).all()
		therows = []
		for i in rows:
			j = i[0]
			therows.append(j)
		return render_template('class.html', existing = therows)