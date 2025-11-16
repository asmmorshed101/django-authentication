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

core settings.py

```
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]
```
in Middleware

```
"corsheaders.middleware.CorsMiddleware",
```

Installed apps

```
'todo',
    'rest_framework',
    'djoser',
    'rest_framework.authtoken',
    'corsheaders'
```


model.py

```
from django.db import models
from django.conf import settings
# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.title
```

serializers.py
```
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
```

Todo apps views.py

```
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, "user_id":user.id})

class ListCreateTodo(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

class RetrieveUpdateDestroyTodo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
```
urls.py

```
from django.urls import path, include
from .views import ListCreateTodo, Login, RetrieveUpdateDestroyTodo


urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('list-create-todo/', ListCreateTodo.as_view(), name='list-create-todo'),
    path('retrieve-update-destroy-todo/<int:pk>/', RetrieveUpdateDestroyTodo.as_view(), name='retrieve-update-destroy-todo'),
]
```



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
