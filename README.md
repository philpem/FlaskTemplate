# FlaskTemplate

A simple Flask+SQLAlchemy application template.

To use this:

- Create your initial database model by modifying `myapp/database.py`
- Initialise flask-migrate: `flask db init`
- Add the new `migrations` folder to git
- Create an initial migration: `flask db migrate`
- Apply the migration to the database: `flask db upgrade`

Every time the database models change, repeat the `migrate` and `upgrade` commands. You should review the migration script manually as it will not detect table or column name changes, or anonymously named constraints. See the [Flask-Migrate documentation](https://flask-migrate.readthedocs.io/en/latest/) for more information.

From this point on, user installation should only require the `flask db upgrade` step be run. This will initialise the database automatically.

For more information on flask-migrate, see https://flask-migrate.readthedocs.io/en/latest/ .

## TODO:

- The Docker bootstrap code isn't ideal (especially database initialisation). Ideally look at Dockerfiles for other web apps and improve this.
