from models.common import db

class Overall(db.Model):
	theclass = db.Column(db.String, db.ForeignKey('classes.theclass'), primary_key = True)
	subject = db.Column(db.String, db.ForeignKey('subjects.subject'), primary_key = True)
	evaluation = db.Column(db.String, primary_key = True)
	co1 = db.Column(db.Integer)
	co2 = db.Column(db.Integer)
	co3 = db.Column(db.Integer)
	co4 = db.Column(db.Integer)
	co5 = db.Column(db.Integer)