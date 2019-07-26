from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth import authenticate, login, logout
import json
from .models import UserProfile
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.permissions import (
    IsAdminUser,
    AllowAny

)
from .serializers import AccountCreateSerializer
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
# from userprofile.models import Expert


@permission_classes((AllowAny,))
class RegisterUser(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        first_name = data['first_name']
        last_name = data['last_name']
        mail = data['email']
        user_type = 'user'
        user_check = User.objects.filter(username=username)
        if not user_check:
            new_user = User.objects.create_user(username, mail, password)
            token, _ = Token.objects.get_or_create(user=new_user)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            return Response("User is created")
        else:
            return Response("We have already the same username")

@permission_classes((AllowAny,))
class RegisterExpert(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        full_name = data['full_name']
        user_type = 'expert'
        user_check = User.objects.filter(username=username)
        if not user_check:
            new_user = User.objects.create_user(username, password)
            token, _ = Token.objects.get_or_create(user=new_user)
            new_user.full_name = full_name
            new_user.save()
            return Response("User is created")
        else:
            return Response("We have already the same username")


@permission_classes((AllowAny,))
class UserLogin(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        user_type = 'user'
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'})
        user = authenticate(username=username, password=password)
        print(user)
        if not user:
            return Response({'error': 'Invalid Credentials'})
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,
                         'user_id':user.id,
                         'username':user.username,
                         'status': user.is_superuser,
                         'user_type':user_type})

@permission_classes((AllowAny,))
class ExpertLogin(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        user_type = 'expert'
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'})
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if not user:
            return Response({'error': 'Invalid Credentials'})
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,
                         'user_id':user.id,
                         'username':user.username,
                         'status': user.is_superuser,
                         'user_type':user_type})





# @permission_classes((AllowAny,))
# class RegisterExpert(APIView):
#     def post(self, request):
#         data = request.data
#         username = data['username']
#         password = data['password']
#         full_name = data['full_name']
#         age = data['age']
#         occupation = data['occupation']
#         expert_check = Expert.objects.filter(username=username)
#         if not expert_check:
#             new_expert = Expert.objects.create(username=username, password=password)
#             token, _ = Token.objects.get_or_create(user=new_expert)
#             new_expert.full_name = full_name
#             new_expert.save()
#             return Response("Expert is created")
#         else:
#             return Response("We have already the same username")


# @permission_classes((AllowAny,))
# class ExpertLogin(APIView):
#     def post(self, request):
#         data = request.data
#         username = data['username']
#         password = data['password']
#         if username is None or password is None:
#             return Response({'error': 'Please provide both username and password'})
#         expert = authenticate(username=username, password=password)
#         if not expert:
#             return Response({'error': 'Invalid Credentials'})
#         token, _ = Token.objects.get_or_create(user=expert)
#         return Response({'token': token.key,
#                          'expert_id':expert.id,
#                          'username':expert.username,
#                          })


class AccountCreateAPIView(CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = AccountCreateSerializer
