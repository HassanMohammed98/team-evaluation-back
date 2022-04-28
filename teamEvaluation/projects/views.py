from django.shortcuts import render
from datetime import datetime

from .models import Project

from semesters.models import Semester
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import ProjectSerializer, UpdateProjectSerializer

# Create your views here.

class ProjectsList(ListAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer

class UserCreateAPIView(CreateAPIView):
    serializer_class = UpdateProjectSerializer
    
    def perform_create(self, serializer):
        semester_id = self.kwargs['semester_id']
        serializer.save(
			semester= Semester.objects.get(id=semester_id),
		)
