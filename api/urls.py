from django.urls import path
from api.views import StartupsAPIView

urlpatterns = [
	path('startups',StartupsAPIView.as_view(), name='api-startups'),
]