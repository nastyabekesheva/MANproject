from django.contrib import admin
from django.urls import include, path
from .views import SignUpView
from .views import SignInView
from .views import StartView
urlpatterns = [
	path('sign_up/', SignUpView.as_view(), name='sign_up'),
	path('sign_in/', SignInView.as_view(), name='sign_in'),
	path('start/', StartView.as_view(), name='start'),
	path(r'^chat/$', login_required(views.DialogsView.as_view()), name='chat'),
	path(r'^chat/create/(?P<user_id>\d+)/$', login_required(views.CreateChatView.as_view()), name='create_chat'),
	path(r'^chat/(?P<chat_id>\d+)/$', login_required(views.ChatListView.as_view()), name='messages'),
			]
