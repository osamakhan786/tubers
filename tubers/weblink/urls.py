from unicodedata import name
from django.urls import path

from . import views

urlpatterns =[
    path('', views.weblink, name="weblink"),
]