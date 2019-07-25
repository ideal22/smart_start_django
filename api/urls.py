from django.urls import path
from api.views import UserList, StartupsListAPIView,StartupsCreateAPIView, StartupCommentAPIView , StartupCommentList, StartupReplyAPIView , StartupReplyList

urlpatterns = [
	path('startups/list',StartupsListAPIView.as_view(), name='api-startups'),
	path('startups/create', StartupsCreateAPIView.as_view(), name='api-startups-create'),
	path('comment/create', StartupCommentAPIView.as_view(), name='api-comment'),
	path('comment/list', StartupCommentList.as_view(), name = 'api-comment-list'),
	path('reply/create',StartupReplyAPIView.as_view(), name='api-reply'),
	path('reply/list', StartupReplyList.as_view(), name='api-reply-list'),
	path('users/list/', UserList.as_view(), name='api-users'),
]