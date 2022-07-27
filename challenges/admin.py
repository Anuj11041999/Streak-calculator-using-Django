from django.contrib import admin
from . import models
# Register your models here.


class ChallengeMemberInline(admin.TabularInline):
    model = models.ChallengeMember

admin.site.register(models.Challenge)
admin.site.register(models.ChallengeMember)
