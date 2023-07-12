from models.common import db

class Assignment_2(db.Model):
	uid = db.Column(db.String, db.ForeignKey('students.uid'), primary_key = True)
	subject = db.Column(db.String, db.ForeignKey('subjects.subject'), primary_key = True)
	marks = db.Column(db.Float)