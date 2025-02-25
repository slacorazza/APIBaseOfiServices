from django.shortcuts import render
from rest_framework.views import APIView as ApiView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token

class login(ApiView):
    def get(self, request):
        return Response({"message": "Login"})
    
class signup(ApiView):
    def get(self, request):
        return Response({"message": "Signup"})

class logout(ApiView):
    def get(self, request):
        return Response({"message": "Logout"})