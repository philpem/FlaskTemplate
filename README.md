# FlaskTemplate

A simple Flask+SQLAlchemy application template.

## Instructions

### Getting started

To use this:

- Create your initial database model by modifying `myapp/database.py`
- Initialise flask-migrate: `flask db init`
- Add the new `migrations` folder to git
- Create an initial migration: `flask db migrate`
- Apply the migration to the database: `flask db upgrade`

### Development

Every time the database models change, repeat the `migrate` and `upgrade` commands. You should review the migration script manually as it will not detect table or column name changes, or anonymously named constraints. See the [Flask-Migrate documentation](https://flask-migrate.readthedocs.io/en/latest/) for more information.

From this point on, user installation should only require the `flask db upgrade` step be run. This will initialise the database automatically.

For more information on flask-migrate, see https://flask-migrate.readthedocs.io/en/latest/ .

### Creating the initial admin user

- Set `SECRET_KEY` and `SQLALCHEMY_DATABASE_URI` in `myapp/myapp.cfg`.
- Run `python3 install.py`.


## Things you might want to do...

### Rename the 'myapp' directory

This needs to be changed in several places:

  - `Dentrypoint.sh`
  - `Dockerfile`
  - `app_venv.wsgi`
  - `instal.py`
  - `myapp/app.py`
  - `myapp/templates/_base.html`

### Change the name of the application, 'MyExampleFlaskApp'

This is in only one place: `myapp/templates/_base.html`.

## TODO:

- The Docker bootstrap code isn't ideal (especially database initialisation). Ideally look at Dockerfiles for other web apps and improve this.

