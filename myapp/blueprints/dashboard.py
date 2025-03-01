from flask import Blueprint, render_template
from flask_login import current_user, login_required
from ..app import app

ROUTENAME = __name__.split('.')[-1]

blueprint = Blueprint(ROUTENAME, __name__,
		template_folder='templates')

# TODO only add menu item if logged in
app.add_menu_item("Dashboard", f"{ROUTENAME}.dashboard", -1000)

# -- dashboard --
#@blueprint.route("/")
@blueprint.route("/dashboard/")
@login_required
def dashboard():
	return render_template('dashboard.html')


# vim: ts=4 sw=4 noet
