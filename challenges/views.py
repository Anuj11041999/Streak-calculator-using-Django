from pyexpat import model
from urllib.request import Request
from django.forms import DateField
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
# Create your views here.
from . import models
from .models import Challenge, ChallengeMember
from users.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages
import datetime
from . import forms
from django.template.defaulttags import register
# Create your views here.

@register.filter
def custom_check(user,memberships):
    return user in [membership.user for membership in memberships]

@register.filter
def complete_check(user,memberships):
    for  membership in memberships:
        if user==membership.user:
            if membership.remaining_days == 0:
                return True
    return False


class Signup(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'challenges/signup.html'

class CreateChallenge(LoginRequiredMixin,generic.CreateView):
    fields = ('name', 'description','totalDays','reward')
    model = models.Challenge
    def get_success_url(self):
        return reverse('challenges:all')

class SingleChallenge(generic.DetailView):
    model = models.Challenge

class ListChallenges(generic.ListView):
    model = models.Challenge

    
class JoinChallenge(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('challenges:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        challenge = get_object_or_404(models.Challenge,slug = self.kwargs.get('slug'))

        try:
            user = User.objects.get(id = self.request.user.id)
            models.ChallengeMember.objects.create(user=user, challenge=challenge,remaining_days = challenge.totalDays)
        except IntegrityError:
            messages.warning(self.request,'Warning already a member')
        else:
            messages.success(self.request,'You are a member now')

        return super().get(request,*args,**kwargs)

class LeaveChallenge(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('challenges:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        try:
            membership = models.ChallengeMember.objects.filter(
            user= self.request.user,
            challenge__slug = self.kwargs.get('slug')).get()
        except models.ChallengeMember.DoesNotExist:
            messages.warning(self.request,'Sorry you are not in this challenge')
        else:
            membership.delete()
            messages.success(self.request,'You have left the challenge')
        return super().get(request,*args,**kwargs)

class MyChallenges(generic.ListView):
    def get_queryset(self):
        queryset = Challenge.objects.filter(memberships__user=self.request.user)
        return queryset

class AddChallenge(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('challenges:all',)
    
    def get(self,request,*args,**kwargs):
        try:
            challenge = Challenge.objects.get(slug = self.kwargs.get('slug'))
            challengemember = ChallengeMember.objects.filter(challenge_id=challenge.id,user_id=self.request.user.id).first()
            total = challenge.totalDays
            remaining = challengemember.remaining_days
            day = challengemember.streak_updated_at
            currdate = datetime.date.today()
            
            if day==currdate:
                messages.warning(self.request,'already updated')
            elif day+ datetime.timedelta(days=1) == currdate:
                challengemember.streak = total - remaining+1
                challengemember.remaining_days -=1
                challengemember.streak_updated_at = currdate
            else:
                challengemember.streak = 1
                challengemember.remaining_days = total-1
                challengemember.streak_updated_at = currdate

            if challengemember.remaining_days==0:
                user = User.objects.get(id = self.request.user.id)
                user.money += challenge.reward
                user.save()
            challengemember.save()
        except:
            messages.warning(self.request,'Something went wrong')
        return super().get(request,*args,**kwargs)


class CompletedChallenges(LoginRequiredMixin,generic.ListView):
    def get_queryset(self):
        queryset = Challenge.objects.filter(memberships__user=self.request.user,memberships__remaining_days=0)
        return queryset