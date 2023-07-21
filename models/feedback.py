from models.common import db

class Feedback(db.Model):
    theclass = db.Column(db.String, db.ForeignKey('classes.theclass'), nullable=False, primary_key=True)
    subject = db.Column(db.String, db.ForeignKey('subjects.subject'), nullable=False, primary_key=True)
    co1 = db.Column(db.Integer, nullable=False, default=0)
    co2 = db.Column(db.Integer, nullable=False, default=0)
    co3 = db.Column(db.Integer, nullable=False, default=0)
    co4 = db.Column(db.Integer, nullable=False, default=0)
    co5 = db.Column(db.Integer, nullable=False, default=0)