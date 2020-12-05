from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.IntegerField(unique=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone']
    def __str__(self):
        return self.username