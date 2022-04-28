from django.shortcuts import render
from datetime import datetime

from .models import Project

from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import ProjectSerializer

# Create your views here.

class ProjectsList(ListAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer

