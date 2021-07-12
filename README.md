# Taxi24 Installation

## Prerequisities
* Python 3.8+
* Ubuntu 20.04+
* Postgresql 12+
* Postgres extension postgis
** sudo apt-get install postgis postgresql-12-postgis-2.5-scripts
** psql: CREATE EXTENSIONS postgis

## Install requirements
* create virtualenv: python3 -m venv venv_name
* activate vurtualenv: ~/venv_name/bin/activate
* install requirements: pip install -r requirements.txt

## Add environment variables
* export SECRET_KEY=your-secret-key
* export DATABASE_URL=psql://urser:password@host:port/database_name
* export DJANGO_SETTINGS_MODULE='taxi24.settings.dev'

## Run app
* ./manage.py runserver
* ./manage.py test