from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.db import models


class User(AbstractUser):
    username = models.CharField(unique=False, max_length=120)
    email = models.EmailField(unique=True, blank=False)
    is_active = models.BooleanField(default=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []
