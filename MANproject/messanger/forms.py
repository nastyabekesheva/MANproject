from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class SignUpForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')


class SignInForm(AuthenticationForm):

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
