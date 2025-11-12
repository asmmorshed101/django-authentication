# django-authentication
Session Based authentication

```
python -m venv env
env\Scripts\activate
django-admin startproject core
python mamage.py startapp home

```

# For static files

```

import os # at top of file

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,  'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
```
# Follow the html files in templates

# MySQL Database connections
```
pip install mysqlclient

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME":"mydb",
        "USER":"postgres",
        "PASSWORD":"morshed",
        "HOST":"localhost",
        "PORT":"5432"
    }
}

```
