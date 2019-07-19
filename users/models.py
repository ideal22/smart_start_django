from django.db import models

class Users(models.Model):
	userRole = models.CharField(max_length=255)
	email = models.EmailField()

	def __str__(self):
		return self.email

class UserProfiles(models.Model):
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	phone = models.IntegerField()
	dob = models.DateField()
	degree = models.CharField(max_length=255, blank=True, null=True)
	job = models.CharField(max_length=255,blank=True, null=True)




