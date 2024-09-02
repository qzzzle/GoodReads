"""
URL configuration for account app.
"""

from django.urls import path

from .api.v1.views import RegisterLoginAPIView


urlpatterns = [
    path("auth/", RegisterLoginAPIView.as_view(), name="auth"),
]
