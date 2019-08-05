from django.urls import path
from api.views import GetSuperUser, UserList,StartupReplyWithIdList,  StartupCommentWithIdList, StartupsListAPIView,StartupsCreateAPIView, StartupCommentAPIView , StartupCommentList, StartupReplyAPIView , StartupReplyList, StartupsWithIdAPIView

urlpatterns = [
	path('startups/list',StartupsListAPIView.as_view(), name='api-startups'),
	path('startups/create', StartupsCreateAPIView.as_view(), name='api-startups-create'),
	path('startups/list/<int:id>/', StartupsWithIdAPIView.as_view(), name='api-startup-with-id'),
	path('comment/create', StartupCommentAPIView.as_view(), name='api-comment'),
	path('comment/list', StartupCommentList.as_view(), name = 'api-comment-list'),
	path('comment/<int:id>/', StartupCommentWithIdList.as_view(), name='api-comment-with-id'),
	path('reply/create',StartupReplyAPIView.as_view(), name='api-reply'),
	path('reply/list', StartupReplyList.as_view(), name='api-reply-list'),
	path('reply/<int:id>/', StartupReplyWithIdList.as_view(), name='api-reply-with-id'),
	path('users/list/', UserList.as_view(), name='api-users'),
	path('superuser/list/', GetSuperUser.as_view(), name='api-superusers'),
	# path('experts/list/', ExpertList.as_view(), name='api-experts-list'),
]