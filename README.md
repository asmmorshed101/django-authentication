# django-authentication
Session Based authentication


pip install django djangorestframework

pip install -U djoser
pip install django-cors-headers

django-admin startproject config . 

python manage.py startapp todo

change the setting

'todo',
    'rest_framework',
    'djoser',
    'rest_framework.authtoken',


add this in urls.py

path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

add this to the end of settings.py

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

follow this website

https://pypi.org/project/django-cors-headers/


VUE

npm install -g @vue/cli

vue create frontend



http://127.0.0.1:8000/auth/token/login
http://127.0.0.1:8000/auth/users/



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
