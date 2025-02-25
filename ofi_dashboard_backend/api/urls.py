from django.urls import path
from . import views

urlpatterns = [
    path("cases/", views.CaseListCreate.as_view(), name="case-list-create"),
    path("activities/", views.activityListCreate.as_view(), name="activity-list-create"),
    path("cases/<int:id>/", views.CaseRetrieveUpdateDestroy.as_view(), name="case-retrieve-update-destroy"),
    path("activities/<int:id>/", views.ActivityRetrieveUpdateDestroy.as_view(), name="activity-retrieve-update-destroy"),
    path("activity-list/", views.ActivityList.as_view(), name="activity-list"),
]

"""
URL patterns for the API.

This module defines the URL patterns for the API endpoints, mapping each URL to the corresponding view.

Endpoints:
- cases/ : Lists all cases.
- activities/ : Lists all activities.
- cases/<int:id>/ : Retrieve, update, and destroy a specific case.
- activities/<int:id>/ : Retrieve, update, and destroy a specific activity.
- activity-list/ : Lists activities with optional filtering.
"""