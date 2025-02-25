from rest_framework import serializers
from .models import Case, Activity

class CaseSerializer(serializers.ModelSerializer):
    """
    Serializer for the Case model.

    This serializer converts Case model instances into JSON format and vice versa.
    """
    class Meta:
        model = Case
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    """
    Serializer for the Activity model.

    This serializer converts Activity model instances into JSON format and vice versa.
    """
    class Meta:
        model = Activity
        fields = ['case', 'timestamp', 'name']