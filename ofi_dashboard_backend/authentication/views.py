from django.shortcuts import render
from rest_framework.views import APIView as ApiView
from rest_framework.response import Response


class login(ApiView):
    def get(self, request):
        return Response({"message": "Login"})
    
class signup(ApiView):
    def get(self, request):
        return Response({"message": "Signup"})

class logout(ApiView):
    def get(self, request):
        return Response({"message": "Logout"})