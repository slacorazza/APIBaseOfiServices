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
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                user = User.objects.get(username=request.data['username'])
                user.set_password(request.data['password'])
                user.save()
                token = Token.objects.create(user=user)
                return Response({"token": token.key}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Error during signup: {e}")
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class logout(ApiView):
    def get(self, request):
        return Response({"message": "Logout"})