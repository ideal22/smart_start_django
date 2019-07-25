from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, mixins
from api.serializers import StartupsListSerializer,StartupsCreateSerializer, StartupStatusesSerializer, StartupFilesSerializer, StartupCommentSerializer, StartupReplySerializer, GetUser
from startups.models import Startups, StartupStatuses, StartupFiles, Comments, StartupReply

class StartupsListAPIView(generics.ListAPIView):
    serializer_class = StartupsListSerializer

    def get_queryset(self):
        return Startups.objects.all()


class StartupsCreateAPIView(generics.CreateAPIView):
    serializer_class = StartupsCreateSerializer
    queryset = Startups.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class StartupStatusesAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = StartupStatusesSerializer

    def get_queryset(self):
        return StartupStatuses.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StartupFilesAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = StartupFilesSerializer

    def get_queryset(self):
        return StartupFiles.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StartupCommentAPIView(generics.CreateAPIView):  
    queryset = Comments.objects.all()
    serializer_class = StartupCommentSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class StartupCommentList(generics.ListAPIView):   
    serializer_class =  StartupCommentSerializer
    model = Comments
    queryset = Comments.objects.all()


class StartupReplyAPIView(generics.CreateAPIView):
    queryset = StartupReply.objects.all()  
    serializer_class = StartupReplySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class StartupReplyList(generics.ListAPIView):
    serializer_class = StartupReplySerializer 
    model = StartupReply
    queryset = StartupReply.objects.all()


class UserList(generics.ListAPIView):
    serializer_class = GetUser
    model = User
    queryset = User.objects.all()