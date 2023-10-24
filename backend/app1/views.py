from django.shortcuts import render

#ViewSet은 여러 가지 API의 기능을 통합해서 하나의 API Set로 제공
from rest_framework import viewsets
from .serializers import LoginSerializer
from .models import Login

# Create your views here.
class LoginView(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    queryset = Login.objects.all()

