from django.shortcuts import render
from django.contrib.auth.models import Group

from rest_framework import viewsets

from .serializers import StudentSerializer, TeacherSerializer, UserSerializer, GroupSerializer
from .models import Student, Teacher, CustomUser

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all().order_by('name')
	serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
	queryset = Teacher.objects.all().order_by('name')
	serializer_class = TeacherSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = CustomUser.objects.all()
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer