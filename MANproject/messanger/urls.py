from django.contrib import admin
from django.urls import include, path
from .views import SignUpView
from .views import SignInView
from .views import StartView
urlpatterns = [
	path('sign_up/', SignUpView.as_view(), name='sign_up'),
	path('sign_in/', SignInView.as_view(), name='sign_in'),
	path('start/', StartView.as_view(), name='start')
			]
