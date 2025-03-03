from rest_framework import generics
from rest_framework.views import APIView
from .models import Case, Activity
from .serializers import CaseSerializer, ActivitySerializer
from rest_framework.pagination import PageNumberPagination

class CaseListCreate(generics.ListCreateAPIView):
    """
    View to create a new case.

    Methods:
    - GET: Returns a list of all cases.
    - POST: Creates a new case.
    """
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class activityListCreate(generics.ListCreateAPIView):
    """
    View to create a new activity.

    Methods:
    - GET: Returns a list of all activities.
    - POST: Creates a new activity.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class CaseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, and destroy a specific case.

    Methods:
    - GET: Retrieves a specific case.
    - PUT: Updates a specific case.
    - DELETE: Deletes a specific case.
    """
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    lookup_field = 'id'

class ActivityRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, and destroy a specific activity.

    Methods:
    - GET: Retrieves a specific activity.
    - PUT: Updates a specific activity.
    - DELETE: Deletes a specific activity.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    lookup_field = 'id'

class ActivityList(APIView):
    """
    View to list activities with optional filtering by case and name.

    Methods:
    - GET: Returns a list of activities, optionally filtered by case and name.
    """
    def get(self, request, format=None):
        case_ids = request.query_params.getlist('case')
        names = request.query_params.getlist('name')

        if case_ids and names:
            activities = Activity.objects.filter(case__id__in=case_ids, name__in=names)
        elif case_ids:
            activities = Activity.objects.filter(case__id__in=case_ids)
        elif names:
            activities = Activity.objects.filter(name__in=names)
        else:
            activities = Activity.objects.all()

        activities = activities.order_by('timestamp')

        paginator = PageNumberPagination()
        paginated_activities = paginator.paginate_queryset(activities, request)
        serializer = ActivitySerializer(paginated_activities, many=True)
        return paginator.get_paginated_response(serializer.data)