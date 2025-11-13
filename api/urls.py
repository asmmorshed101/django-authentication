from home.views import book, login, people, index
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('people/', people),
    path('book/', book),
    path('login/', login),
]