from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=50)
	dob = models.DateField()
	degree = models.CharField(max_length=255, blank=True, null=True)
	job = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.user)

# class Expert(models.Model):
# 	user = models.OneToOneField(User,on_delete=models.CASCADE)
# 	age = models.PositiveIntegerField(validators=[MinValueValidator(1)], blank=True, null=True)
# 	user_type = models.CharField(max_length=255, blank=True, null=True)
# 	occupation = models.CharField(max_length=255)

# 	def __str__(self):
# 		return self.full_name




