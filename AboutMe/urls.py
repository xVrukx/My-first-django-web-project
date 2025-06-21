from django.urls import path
from .views import *

urlpatterns =[
    path('',about_me,name="aboutMe")
]