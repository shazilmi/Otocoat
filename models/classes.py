from models.common import db

class Classes(db.Model):
	theclass = db.Column(db.String, primary_key = True)
	students = db.relationship("Students", lazy = True)
	subjects = db.relationship("Subjects", lazy = True)