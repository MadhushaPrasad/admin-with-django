from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,uniq=true)
    password = models.CharField(max_length=255,uniq=true)
    is_ambassador = models.BooleanField(default=true)
    username = None

    USERNAME_FIELD = 'email'