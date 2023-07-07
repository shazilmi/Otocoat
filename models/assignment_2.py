from models.common import db

class Assignment_2(db.Model):
	uid = db.Column(db.String, db.ForeignKey('students.uid'), primary_key = True)
	subject = db.Column(db.String, db.ForeignKey('subjects.subject'), primary_key = True)
	score = db.Column(db.Float)
	co1 = db.Column(db.Integer, default = 0)
	co2 = db.Column(db.Integer, default = 0)
	co3 = db.Column(db.Integer, default = 0)
	co4 = db.Column(db.Integer, default = 0)
	co5 = db.Column(db.Integer, default = 0)