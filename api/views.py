from django.shortcuts import render
from rest_framework import generics, mixins
from api.serializers import StartupsSerializer, StartupStatusesSerializer, StartupFilesSerializer
from startups.models import Startups, StartupStatuses, StartupFiles

class StartupsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = StartupsSerializer

    def get_queryset(self):
        return Startups.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

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
