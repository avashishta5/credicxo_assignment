from rest_framework import serializers
from .models import Student, Teacher


class StudentSerializer(serializers.HyperlinkedModelSerializer):
	registration_no = serializers.ReadOnlyField()

	class Meta:
		model = Student
		fields = "__all__"

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
	registration_no = serializers.ReadOnlyField()
	
	class Meta:
		model = Teacher
		fields = "__all__"