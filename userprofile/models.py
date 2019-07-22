from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=50)
	dob = models.DateField()
	degree = models.CharField(max_length=255, blank=True, null=True)
	job = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.user)






