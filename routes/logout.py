from flask_login import logout_user
from flask import Blueprint, redirect, flash, session, url_for
from flask_login import login_required

logouts = Blueprint('logout', __name__)

@logouts.route('/logout', methods = ['GET'])
@login_required
def logout():
	logout_user()
	session['admin'] = 2
	return redirect('index')