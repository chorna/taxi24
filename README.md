# Add environment variables

export SECRET_KEY=your-secret-key
export DATABASE_URL=psql://urser:password@host:port/database_name
export DJANGO_SETTINGS_MODULE='taxi24.settings.dev'

# Postgresql

sudo apt-get install postgis postgresql-12-postgis-2.5-scripts
CREATE EXTENSIONS postgis