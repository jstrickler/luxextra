"""
URL Configuration for tate_core
"""
from django.urls import path, include

app_name = 'data'

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
