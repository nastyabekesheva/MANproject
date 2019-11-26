from django.shortcuts import render
from django.views.generic import View
from .forms import SignUpForm
from django.contrib.auth import authenticate
from .models import User
from .forms import SignInForm

class SignUpView(View):
	form_class = SignUpForm 
	template_name = 'messanger/sign_up.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			baseuser = authenticate(username=username, password=raw_password)
			user = User.objects.create(user=user)
			login(request, user)
			return redirect('main')
		else:
			return render(request, self.template_name, {'form': form})
	

class SignInView(View):
	form_class = SignInForm 
	template_name = 'messanger/sign_in.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = User.objects.create(user=user)
			login(request, user)
			return redirect('main')
		else:
			return render(request, self.template_name, {'form': form})
# Create your views here.
