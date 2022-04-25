from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.generics import (
	ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView,
	CreateAPIView,
)
from datetime import datetime

# Create your views here.
