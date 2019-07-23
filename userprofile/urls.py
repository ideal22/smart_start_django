from django.urls import path
from .views import RegisterUser, AccountCreateAPIView, UserLogin

urlpatterns = [
     path('register/', RegisterUser.as_view(), name='register'),
     path('full/', AccountCreateAPIView.as_view(), name='account'),
     path('login/', UserLogin.as_view(), name='login')
]
