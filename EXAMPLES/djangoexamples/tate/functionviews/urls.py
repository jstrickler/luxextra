"""
URL Configuration for functionviews
"""
from django.urls import path
from . import views   # import views from app

app_name = "functionviews"

urlpatterns = [
    # add url patterns for the functionviews app here

    # Examples:
    path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
]
