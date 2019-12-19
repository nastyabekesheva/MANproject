from django.db import models
from django.contrib.auth.models import User as BaseUser
from django.utils import timezone
from .forms import SignUpForm


class User(models.Model):
	user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)

	tsv = models.BooleanField(default = False)
	last_seen = models.DateTimeField(default=timezone.now, editable=True)

	#def __str__(self):
		#return username
	def update_last_seen(self):
		self.last_seen = timezone.now()


class Message(models.Model):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    message = models.TextField(editable="False", default="True")
    date = models.DateTimeField(default=timezone.now)

    #def __str__(self):
        #return self.message


class Chat(models.Model):
    users = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message


# Create your models here.
