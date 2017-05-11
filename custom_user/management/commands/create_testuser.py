from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
#from custom_user.models import User

class Command(BaseCommand):
	help = 'Creates a user for testing'

	def __init__(self, *args, **kwargs):
		super(Command,self).__init__(*args, **kwargs)
		self.UserModel = get_user_model()

	def handle(self, *args, **options):

		user = self.UserModel.objects.create_user('testuser', password='testpass', affiliation='Test Org')
		user.save()

		self.stdout.write(self.style.SUCCESS('Created user with username "testuser" and password "testpass"'))
