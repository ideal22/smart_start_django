from django.urls import path
from userprofile.views import RegisterUser, AccountCreateAPIView, UserLogin, ExpertLogin, RegisterExpert

urlpatterns = [
     path('register/', RegisterUser.as_view(), name='register'),
     path('full/', AccountCreateAPIView.as_view(), name='account'),
     path('login/', UserLogin.as_view(), name='login'),
     path('login/expert/', ExpertLogin.as_view(), name='login-expert'),
     path('register/expert/', RegisterExpert.as_view(), name='register-expert'),
]
