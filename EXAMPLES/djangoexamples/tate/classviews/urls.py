"""
URL Configuration for classviews
"""
from django.urls import path
from . import views   # import views from app

app_name = "classviews"

urlpatterns = [
    # add more url patterns for the classviews app here
    path('', views.home, name='home'),
    path('artists/', views.ArtistFilterView.as_view(), name="artists"), 
    path('artist/<str:pk>', views.ArtistDetailView.as_view(), name="artistdetail"), 
    path('artworks/', views.ArtworkFilterView.as_view(), name="artworks"), 
    path('artwork/<str:pk>', views.ArtworkDetailView.as_view(), name="artworkdetail"), 
]
