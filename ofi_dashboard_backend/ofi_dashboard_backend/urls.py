from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
    path('auth/', include('authentication.urls')),
]

"""
URL patterns for the main project.

This module defines the URL patterns for the main project, mapping each URL to the corresponding app's URL configuration.

Endpoints:
- api/ : Includes the URL patterns for the API endpoints.
- auth/ : Includes the URL patterns for the authentication endpoints.
"""