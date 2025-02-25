from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    This serializer converts User model instances into JSON format and vice versa.
    It includes the following fields:
    - id: The unique identifier for the user.
    - username: The username of the user.
    - email: The email address of the user.
    - password: The password of the user (write-only).
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}