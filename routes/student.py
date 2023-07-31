from flask import Flask, request, render_template, flash, redirect, url_for, Blueprint
from models.common import db
from models.students import Students
from models.classes import Classes
from models.subjects import Subjects
from flask_login import login_required

students = Blueprint('student', __name__)


@students.route("/student", methods = ["GET", "POST"])
@login_required
def student():
	if request.method == "GET":
		alist = db.session.execute(db.select(Students.uid)).all()
		blist = []
		for i in alist:
			blist.append(i[0])
		clist = db.session.execute(db.select(Classes.theclass)).all()
		dlist = []
		for i in clist:
			dlist.append(i[0])
		return render_template("student.html", thelist = blist, alist = dlist)
	if request.method == "POST":
		alist = db.session.execute(db.select(Students.uid)).all()
		blist = []
		for i in alist:
			blist.append(i[0])
		clist = db.session.execute(db.select(Classes.theclass)).all()
		dlist = []
		for i in clist:
			dlist.append(i[0])
		if not request.form['uid']:
			flash("UID is mandatory!")
			return render_template("student.html", thelist = blist, alist = dlist)
		if not request.form['name']:
			flash("Name is mandatory!")
			return render_template("student.html", thelist = blist, alist = dlist)
		if not request.form['classy']:
			flash("Class is mandatory!")
			return render_template("student.html", thelist = blist, alist = dlist)
		theuid = request.form['uid']
		thename = request.form['name']
		aclass = request.form['classy']
		if aclass not in dlist:
			flash("Invalid class entered!")
			return render_template("student.html", thelist = blist, alist = dlist)
		if theuid in blist:
			flash("UID already exists!")
			return render_template("student.html", thelist = blist, alist = dlist)
		thestudent = Students(uid = theuid, name = thename, theclass = aclass)
		db.session.add(thestudent)
		db.session.commit()
		flash("Student details successfully added!")
		alist = db.session.execute(db.select(Students.uid)).all()
		blist = []
		for i in alist:
			blist.append(i[0])
		return render_template("student.html", thelist = blist, alist = dlist)