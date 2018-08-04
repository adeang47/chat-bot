from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    pass


# Base User, currently unused, but can be linked to Question Responses
class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=timezone.now)
