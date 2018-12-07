from django.contrib import admin
from django.urls import path,include
from .views import *

app='projects'
urlpatterns = [
    path('create/',get_name, name='create'),
    path('new/',NewView.as_view(),name='new'),
]
