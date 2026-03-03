"""
URL Configuration for charts
"""
from django.urls import path
from . import views   # import views from app

app_name = "charts"

urlpatterns = [
    # add url patterns for the charts app here

    # Examples:
    path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
]
