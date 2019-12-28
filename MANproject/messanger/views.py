from django.shortcuts import render
from django.views.generic import View
from .forms import SignUpForm
from django.contrib.auth import authenticate
from .models import User, Chat, Message
from .forms import SignInForm, MessageForm, SignUpForm

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


class StartView(View):
	template_name = 'messanger/start.html'


class ChatListView(View):
    model = Chat
    template_name = 'chatlist.html'
	
    def get(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            if request.user in chat.users.all():
                chat.message_set.filter(is_readed=False).exclude(author=request.user).update(is_readed=True)
            else:
                chat = None
        except Chat.DoesNotExist:
            chat = None
 
        return render(
            request,
            'users/chatlist.html',
            {
                'user': request.user,
                'chat': chat,
                'form': MessageForm()
            }
        )
 
    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()
        return redirect(reverse('users:messages', kwargs={'chat_id': chat_id}))


class DialogsView(View):

    def get(self, request):
        chats = Chat.objects.filter(users__in=[request.user.id])
        return render(request, 'users/chatlist.html', {'user_profile': request.user, 'chats': chats})


class CreateChatView(View):

    def get(self, request, user_id):

        chats = Chat.objects.filter(users__in=[request.user.id, user_id], type=Chat.DIALOG).annotate(c=Count('users')).filter(c=2)
        if chats.count() == 0:
            chat = Chat.objects.create()
            chat.users.add(request.user)
            chat.users.add(user_id)
        else:
            chat = chats.first()
        return redirect(reverse('users:messages', kwargs={'chat_id': chat.id}))
