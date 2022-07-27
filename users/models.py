from re import T
from django.db import models
from django.contrib import auth

# Create your models here.


class User(auth.models.AbstractUser , auth.models.PermissionsMixin):
    money = models.IntegerField(default=0)
    def __str__(self):
        return "@{}".format(self.username)
