from django.shortcuts import render
import django_filters
from .models import *
from rest_framework import viewsets,filters
from .serializers import UserSerializer,TaskSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer