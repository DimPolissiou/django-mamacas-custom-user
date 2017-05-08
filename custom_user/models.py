from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):
	#pass
	affiliation = models.CharField(_('affiliation'), max_length=30, blank=False)
