from models.common import db

class Subjects(db.Model):
	theclass = db.Column(db.String, db.ForeignKey('classes.theclass'), primary_key = True)
	subject = db.Column(db.String, primary_key = True)
	assign_1 = db.relationship("Assignment_1", lazy = True)
	assign_2 = db.relationship("Assignment_2", lazy = True)
	endsem = db.relationship("Endsem", lazy = True)
	intern_1 = db.relationship("Internals_1", lazy = True)
	intern_2 = db.relationship("Internals_2", lazy = True)