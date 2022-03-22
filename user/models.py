from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=False,
        blank=True,
        null=True

    )
    email = models.EmailField(blank=False, null=False, unique=True)
    full_name = models.CharField(max_length=55, blank=False, null=False)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']