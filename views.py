from django.shortcuts import render
from rest_framework import viewsets
from.models import Login
from.serializers import LoginSerializer
class Loginviewset(APIVIEW):
  def post(self,request):
     res=response.data
     token=request.get("token")
     token=request.get("token")
     token=request.get("token")
     return response("Login successful")
