from models.common import db

class Users(db.Model):
	name = db.Column(db.String)
	email = db.Column(db.String, primary_key = True)
	password = db.Column(db.String)