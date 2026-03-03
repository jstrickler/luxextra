"""
URL Configuration for messages demo
"""
from django.urls import path
from . import views   # import views from app

app_name = "messagesdemo"

urlpatterns = [
    # add url patterns for the messages app here

    # Examples:
    path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
]
