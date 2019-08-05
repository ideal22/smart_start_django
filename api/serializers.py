from rest_framework import serializers
from django.contrib.auth.models import User
from startups.models import Notifications, Comments, Startups, StartupFiles, StartupStatuses, StartupReply
# from userprofile.models import Expert

class GetUser(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'first_name', 'last_name')

class GetUsername(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username',)

class GetSuperUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email')

	def get_queryset(self):
		s = User.objects.filter(is_superuser=True)
		return s

class StartupReplySerializer(serializers.ModelSerializer):
	class Meta:
		model = StartupReply
		fields = ('id', 'user','text' , 'date','reply')

	def create(self, validated_data):
		s = StartupReply.objects.create(**validated_data)
		s.user = self.context['request'].user
		s.save()
		print(self.context['request'].user)
		return s
	
class StartupCommentSerializer(serializers.ModelSerializer):
	reply = StartupReplySerializer(many=True, required=False)
	user = GetUsername(read_only=True,many=False)
	class Meta:
		model = Comments
		fields = ('id', 'user', 'text' , 'date', 'startup', 'reply')

	def create(self, validated_data):
		s = Comments.objects.create(**validated_data)
		s.user = self.context['request'].user
		s.save()
		print(self.context['request'].user)
		return s

class StartupsListSerializer(serializers.ModelSerializer):
	user = GetUser(read_only=True, many=False)
	comments_set = StartupCommentSerializer(many=True)

	class Meta:
		model = Startups
		fields = ('id', 'user', 'title', 'description','how_long', 'file', 'comments_set')

class StartupsCreateSerializer(serializers.ModelSerializer):
	user = GetUser(read_only=True, many=False)

	class Meta:
		model = Startups
		fields = ('id', 'user', 'title', 'description','how_long')

	def create(self, validated_data):
		s = Startups.objects.create(**validated_data)
		file = self.context['request'].FILES.get('file')
		s.file = file
		s.user = self.context['request'].user
		s.save()
		print(self.context['request'].user)
		return s

class StartupStatusesSerializer(serializers.ModelSerializer):
	class Meta:
		model = StartupStatuses
		fields = ('id', 'status')

class StartupFilesSerializer(serializers.ModelSerializer):
	class Meta:
		model = StartupFiles
		fields = ('id', 'fileType')


# class ExpertSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Expert
# 		fields = ('id', 'full_name', 'username', 'age', 'occupation')