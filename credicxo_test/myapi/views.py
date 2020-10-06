from django.shortcuts import render

from rest_framework import viewsets

from .serializers import StudentSerializer, TeacherSerializer
from .models import Student, Teacher

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
	queryset = Hero.objects.all().order_by('registration_no')
	serializer_class = StudentSerializer