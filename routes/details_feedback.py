from flask import Flask, render_template, request, redirect, flash, url_for, session, Blueprint
from models.common import db
from models.classes import Classes
from models.subjects import Subjects
from models.feedback import Feedback
from models.overall import Overall
from flask_login import login_required

feedb = Blueprint('feedback', __name__)

@feedb.route('/feedback', methods=["GET", "POST"])
@login_required
def feed():
    if request.method == "GET":
        return render_template('feedback1.html')
    if request.method == "POST":
        a_class = session['theclass']
        a_subject = session['subject']
        a_co1 = int(request.form['co1'])
        a_co2 = int(request.form['co2'])
        a_co3 = int(request.form['co3'])
        a_co4 = int(request.form['co4'])
        a_co5 = int(request.form['co5'])
        if not (0 <= a_co1 <= 3 and 0 <= a_co2 <= 3 and 0 <= a_co3 <= 3 and 0 <= a_co4 <= 3 and 0 <= a_co5 <= 3):
            flash('Invalid input! Please enter values between 0 and 3.')
            return redirect('feedback')
        theover = db.session.execute(db.select(Overall).filter_by(\
            theclass = a_class, subject = a_subject, evaluation = session['evaluation'])).first()
        if theover is None:
            anover = Overall(theclass = a_class, subject = a_subject, evaluation = session['evaluation'], \
                co1 = a_co1, co2 = a_co2, co3 = a_co3, co4 = a_co4, co5 = a_co5)
            db.session.add(anover)
            db.session.commit()
        else:
            theover[0].co1 = a_co1
            theover[0].co2 = a_co2
            theover[0].co3 = a_co3
            theover[0].co4 = a_co4
            theover[0].co5 = a_co5
            db.session.commit()
        thecheck = db.session.execute(db.select(Feedback).filter_by(theclass=a_class, subject=a_subject)).first()
        if thecheck is None:
            feedback_details = Feedback(
                theclass=a_class,
                subject=a_subject,
                co1=a_co1,
                co2=a_co2,
                co3=a_co3,
                co4=a_co4,
                co5=a_co5
            )
            db.session.add(feedback_details)
            db.session.commit()
            flash('Course feedback details added successfully!')
        else:
            thecheck[0].co1 = a_co1
            thecheck[0].co2 = a_co2
            thecheck[0].co3 = a_co3
            thecheck[0].co4 = a_co4
            thecheck[0].co5 = a_co5
            db.session.commit()
            flash('Course feedback details updated successfully!')
        return redirect('dash')