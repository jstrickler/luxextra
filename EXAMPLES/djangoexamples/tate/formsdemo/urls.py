"""
URL Configuration for djforms/superheroes
"""
from django.urls import path
from . import views

app_name = 'formsdemo'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('demo', views.demo, name='demo'),
    # path('heroadd/<str:layout_type>', views.heroadd, name='heroadd'),
    # path('herodelete', views.herodelete, name='herodelete'),
    # path('herodeletedropdown', views.herodeletedropdown, name='herodeletedropdown'),
    # path('herolist', views.herolist, name='herolist'),
    # path('herodetails/<str:pk>', views.herodetails, name='herodetails'),
    # path('heroadded/<str:pk>', views.heroadded, name='heroadded'),
] 

