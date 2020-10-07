from rest_framework import serializers
from .models import Student, Teacher


class StudentSerializer(serializers.HyperlinkedModelSerializer):
	registration_no = serializers.ReadOnlyField()

	class Meta:
		model = Student
		fields = "__all__"

	def create(self, validated_data):
		return Student.objects.create(**validated_data)

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
	registration_no = serializers.ReadOnlyField()

	class Meta:
		model = Teacher
		fields = "__all__"

	def create(self, validated_data):
		return Teacher.objects.create(**validated_data)