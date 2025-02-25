from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login.as_view(), name='login'),
    path('logout/', views.logout.as_view(), name='logout'),
    path('signup/', views.signup.as_view(), name='signup'),
    path('validate-token/', views.validate_token.as_view(), name='validate-token'),
]

"""
URL patterns for the authentication app.

This module defines the URL patterns for the authentication endpoints, mapping each URL to the corresponding view.

Endpoints:
- login/ : Logs in a user.
- logout/ : Logs out a user.
- signup/ : Registers a new user.
- validate-token/ : Validates the authentication token.
"""