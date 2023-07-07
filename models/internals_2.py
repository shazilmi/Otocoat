from models.common import db

class Internals_2(db.Model):
	uid = db.Column(db.String, db.ForeignKey("students.uid"), primary_key = True)
	subject = db.Column(db.String, db.ForeignKey("subjects.subject"), primary_key = True)
	q1 = db.Column(db.Float, default = 0)
	d1 = db.Column(db.Integer)
	co1 = db.Column(db.Integer)
	q2 = db.Column(db.Float, default = 0)
	d2 = db.Column(db.Integer)
	co2 = db.Column(db.Integer)
	q3 = db.Column(db.Float, default = 0)
	d3 = db.Column(db.Integer)
	co3 = db.Column(db.Integer)
	q4 = db.Column(db.Float, default = 0)
	d4 = db.Column(db.Integer)
	co4 = db.Column(db.Integer)
	q5 = db.Column(db.Float, default = 0)
	d5 = db.Column(db.Integer)
	co5 = db.Column(db.Integer)
	q6 = db.Column(db.Float, default = 0)
	d6 = db.Column(db.Integer)
	co6 = db.Column(db.Integer)
	q7 = db.Column(db.Float, default = 0)
	d7 = db.Column(db.Integer)
	co7 = db.Column(db.Integer)
	q8 = db.Column(db.Float, default = 0)
	d8 = db.Column(db.Integer)
	co8 = db.Column(db.Integer)
	q9 = db.Column(db.Float, default = 0)
	d9 = db.Column(db.Integer)
	co9 = db.Column(db.Integer)
	q10 = db.Column(db.Float, default = 0)
	d10 = db.Column(db.Integer)
	co10 = db.Column(db.Integer)
	q11 = db.Column(db.Float, default = 0)
	d11 = db.Column(db.Integer)
	co11 = db.Column(db.Integer)
	q12 = db.Column(db.Float, default = 0)
	d12 = db.Column(db.Integer)
	co12 = db.Column(db.Integer)
	q13 = db.Column(db.Float, default = 0)
	d13 = db.Column(db.Integer)
	co13 = db.Column(db.Integer)
	q14 = db.Column(db.Float, default = 0)
	d14 = db.Column(db.Integer)
	co14 = db.Column(db.Integer)
	q15 = db.Column(db.Float, default = 0)
	d15 = db.Column(db.Integer)
	co15 = db.Column(db.Integer)