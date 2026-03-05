"""
URL Configuration for celerydemo
"""
from django.urls import path
from .views import FeedbackFormView, SuccessView

app_name = "celerydemo"

urlpatterns = [
    path('', FeedbackFormView.as_view(), name='home'),
    path('success/', SuccessView.as_view(), name='success'),
]
