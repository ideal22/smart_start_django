from django.db import models
from django.contrib.auth.models import User


class Notifications(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	text = models.TextField()
	link = models.CharField(max_length=255)

class Comments(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	startup = models.ForeignKey('Startups', on_delete=models.CASCADE)
	text = models.TextField(blank=True, default='', null=True)
	date = models.DateTimeField(auto_now=True)

class Startups(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length=255)
	description = models.TextField()
	how_long = models.IntegerField()
	file = models.FileField(null=True, blank=True, upload_to="media")

	def __str__(self):
		return self.title

class StartupStatuses(models.Model):
	status = models.CharField(max_length=255)

	def __str__(self):
		return self.status

class StartupFiles(models.Model):
	fileType = models.CharField(max_length=255)
	
	def __str__(self):
		return self.fileType

class StartupReply(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	reply = models.ForeignKey('Comments', on_delete=models.CASCADE)
	text = models.TextField(blank=True,default='', null=True)
	date = models.DateTimeField(auto_now=True)