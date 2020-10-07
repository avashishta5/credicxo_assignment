from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class Student(models.Model):
	YEARS = (
		('I', 'First'),
		('II', 'Second'),
		('III', 'Third'),
		('IV', 'Fourth'),
		)
	name = models.CharField(max_length=100)
	registration_no = models.CharField(max_length=6, null=True, unique=True)
	dob = models.DateField()
	year = models.CharField(max_length=3, choices=YEARS, default=YEARS[0])
	branch = models.CharField(max_length=3, choices=settings.BRANCHES, default=settings.BRANCHES[0])
	guardian_name = models.CharField(max_length=100)
	phone_no = models.CharField(max_length=10)


	def __str__(self):
		return self.name

@receiver(post_save, sender=Student)
def update_student_reg_no(sender, instance, created, **kwargs):
	if created:
		instance.registration_no = "S%05d" % instance.id
		instance.save()


class Teacher(models.Model):
	name = models.CharField(max_length=100)
	registration_no = models.CharField(max_length=6, null=True, unique=True)
	dob = models.DateField()
	branch = models.CharField(max_length=3, choices=settings.BRANCHES, default=settings.BRANCHES[0])
	phone_no = models.CharField(max_length=10)
	

	def __str__(self):
		return self.name

@receiver(post_save, sender=Teacher)
def update_teacher_reg_no(sender, instance, created, **kwargs):
	if created:
		instance.registration_no = "T%05d" % instance.id
		instance.save()