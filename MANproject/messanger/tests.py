from django.test import TestCase
import datetime
from django.utils import timezone
from .models import User
from django.contrib.auth.models import User as BaseUser

def create_user():
	user = BaseUser.objects.create_user('username', 'example@gmail.com', 'password')
	user = User.objects.create(user=user)
	return user



class UserModelTest(TestCase):

	def test_last_seen(self):
		user = create_user()
		time1 = timezone.now()
		user.update_last_seen()
		self.assertGreater(user.last_seen, time1)




