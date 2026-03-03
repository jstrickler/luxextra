"""
URL Configuration for users
"""
from django.urls import path
from . import views   # import views from app

app_name = "users"

urlpatterns = [
    # add url patterns for the users app here

    # Examples:
    path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
]
