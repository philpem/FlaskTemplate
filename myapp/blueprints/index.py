from flask import Blueprint, render_template
from flask_login import current_user, login_required

ROUTENAME = __name__.replace('.', '_')

blueprint = Blueprint(ROUTENAME, __name__,
		template_folder='templates')

def init_app(app):
    """
    Initialise this blueprint with the application instance.

    This is called by the application factory to register menu items and
    perform app-specific initialisation.
    """

    # TODO only add menu item if logged in
    app.add_menu_item("Dashboard", f"{ROUTENAME}.index", -1000)

# -- dashboard --
@blueprint.route("/")
#@blueprint.route("/dashboard/")
@login_required
def index():
	return render_template('dashboard.html')

# vim: ts=4 sw=4 noet
