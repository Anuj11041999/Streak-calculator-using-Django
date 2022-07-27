# Generated by Django 4.0.4 on 2022-07-25 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('description_html', models.TextField(blank=True, default='', editable=False)),
                ('totalDays', models.IntegerField(blank=True, null=True)),
                ('remainingDays', models.IntegerField(editable=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ChallengeMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='challenges.challenge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_challenges', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('challenge', 'user')},
            },
        ),
    ]
