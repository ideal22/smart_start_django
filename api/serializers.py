from rest_framework import serializers
from users.models import Users, UserProfiles
from startups.models import Notifications, Comments, Startups, StartupFiles, StartupStatuses

class GetUser(serializers.ModelSerializer):
	class Meta:
		model = Users
		fields = ('id', 'email', 'userRole')

class StartupsSerializer(serializers.ModelSerializer):
	user = GetUser(read_only=True, many=False)
	class Meta:
		model = Startups
		fields = ('id', 'title', 'description', 'user', 'startupStatus')

class StartupStatusesSerializer(serializers.ModelSerializer):
	class Meta:
		model = StartupStatuses
		fields = ('id', 'status')

class StartupFilesSerializer(serializers.ModelSerializer):
	class Meta:
		model = StartupFiles
		fields = ('id', 'fileType')




