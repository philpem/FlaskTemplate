from flask import Blueprint, render_template
from flask_login import current_user, login_required
from ..app import app

ROUTENAME = __name__.split('.')[-1]

blueprint = Blueprint(ROUTENAME, __name__,
		template_folder='templates')

app.add_menu_item("Viewer", f"{ROUTENAME}.index", -1000)

# -- dashboard --
@blueprint.route("/")
def index():
	return render_template('dashboard.html')


# vim: ts=4 sw=4 noet
