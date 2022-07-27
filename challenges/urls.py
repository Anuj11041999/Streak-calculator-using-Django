from re import template
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='challenges'

urlpatterns =[
    path('login/', auth_views.LoginView.as_view(template_name = 'challenges/login.html'), 
        name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.Signup.as_view(), name="signup"),
   
    path('', views.ListChallenges.as_view(), name="all"),
    path("challenges/in/<slug>/",views.SingleChallenge.as_view(),name="single"),
    path("new/", views.CreateChallenge.as_view(), name="create"),
    path("mychallenges/",views.MyChallenges.as_view(),name="my"),
    path("join/<slug>/",views.JoinChallenge.as_view(),name="join"),
    path("leave/<slug>/",views.LeaveChallenge.as_view(),name="leave"),
    path("add/<slug>/",views.AddChallenge.as_view(),name="add"),
    path("completed/",views.CompletedChallenges.as_view(),name="completed"),
    

]
