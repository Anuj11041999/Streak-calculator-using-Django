from xmlrpc.client import NOT_WELLFORMED_ERROR
from django.db import models
from django.contrib import auth
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
import datetime

import misaka


class Challenge(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False,default='', blank=True)
    totalDays = models.IntegerField(null=True,blank=True)
    reward = models.IntegerField(default=0,null=True,blank=True)
    
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        self.remainingDays = self.totalDays
        super().save(*args, **kwargs)
    
    class Meta:
        ordering= ['name']

class ChallengeMember(models.Model):
    challenge = models.ForeignKey(Challenge, related_name="memberships",on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="user_challenges",on_delete=models.CASCADE)
    remaining_days = models.IntegerField(editable=False,null=True,blank=True)
    streak = models.IntegerField(default=0)
    streak_updated_at = models.DateField(default=datetime.date.today())
    def __str__(self):
        return self.user.username

    class Meta:
        unique_together =('challenge','user')
    