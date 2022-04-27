from django.shortcuts import render
from datetime import datetime

from .models import Semester

from rest_framework.generics import ListAPIView
from .serializers import SemesterSerializer

# Create your views here.

class SemestersList(ListAPIView):
	queryset = Semester.objects.all()
	serializer_class = SemesterSerializer
