import django.contrib.auth.urls
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('test/', views.TestPage.as_view(), name="test"),
    path('thanks/', views.ThanksPage.as_view(), name="thanks"),
    path('challenges/', include("challenges.urls", namespace="challenges")),
    path('challenges/', include("django.contrib.auth.urls")),
]