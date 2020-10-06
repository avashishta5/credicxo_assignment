from django.shortcuts import render

from rest_framework import viewsets

from .serializers import StudentSerializer, TeacherSerializer
from .models import Student, Teacher

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all().order_by('name')
	serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
	queryset = Teacher.objects.all().order_by('name')
	serializer_class = TeacherSerializer