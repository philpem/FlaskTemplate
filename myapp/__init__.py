import os
from .app import app

from .blueprints import index

def load_blueprints():
	""" Load and register blueprints """
	import pkgutil
	from . import blueprints

	# import all modules and packages in the 'blueprints' directory
	for importer,modname,ispkg in pkgutil.iter_modules(blueprints.__path__):
		try:
			# import the module and add it to 'mods'
			module = __import__(f"myapp.blueprints.{modname}", fromlist=[modname])
			if hasattr(module, 'blueprint'):
				app.register_blueprint(module.blueprint)
				app.logger.info(f"Registered blueprint: {modname}")
			else:
				app.logger.warning(f"Module {modname} has no 'blueprint' attribute")
		except Exception as e:
			app.logger.error(f"Failed to load blueprint {modname}: {e}")


# Load pluggable blueprints
load_blueprints()

# vim: ts=4 sw=4 noet
