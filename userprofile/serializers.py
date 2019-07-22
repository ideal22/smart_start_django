from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import UserProfile


class GetUser(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
        ]


class AccountCreateSerializer(ModelSerializer):

    class Meta:
        model = UserProfile
        fields = [
             "user",
             "phone",
              "dob",
              "degree",
             "job"
        ]
