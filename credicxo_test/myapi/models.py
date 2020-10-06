from django.db import models
from django.conf import settings

# Create your models here.
class Student(model.Model):
	YEARS = (
		('I', 'First'),
		('II', 'Second'),
		('III', 'Third'),
		('IV', 'Fourth'),
		)
	name = models.CharField(max_length=100)
	dob = models.DateField()
	year = models.CharField(max_length=3, choices=YEARS)
	branch = models.CharField(max_length=3, choices=settings.BRANCHES)
	guardian_name = models.CharField(max_length=100)
	phone_no = models.CharField(max_length=10)

	@property
	def registration_no(self):
		return "S%05d" % self.id


	def __str__(self):
		return self.name

class Teacher(model.Model):
	name = models.CharField(max_length=100)
	dob = models.DateField()
	branch = models.CharField(max_length=3, choices=settings.BRANCHES)
	phone_no = models.CharField(max_length=10)

	@property
	def registration_no(self):
		return "T%05d" % self.id
	

	def __str__(self):
		return self.name