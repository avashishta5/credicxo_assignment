from rest_framework import serializers
from .models import Student, Teacher

class StudentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Student
		fields = ('name', 'dob', 'year', 'branch', 'guardian_name', 'phone_no')

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Teacher
		fields = ('name', 'dob', 'branch', 'phone_no')