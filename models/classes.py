from models.common import db

class Classes(db.Model):
	theclass = db.Column(db.String, primary_key = True)
	students = db.relationship("Students", lazy = True)
	subjects = db.relationship("Subjects", lazy = True)
	deta1 = db.relationship("Internals_1_details", lazy = True)
	deta2 = db.relationship("Assignment_1_details", lazy = True)
	deta3 = db.relationship("Internals_2_details", lazy = True)
	deta4 = db.relationship("Assignment_2_details", lazy = True)
	deta5 = db.relationship("Endsem_details", lazy = True)
	deta6 = db.relationship("Feedback", lazy = True)