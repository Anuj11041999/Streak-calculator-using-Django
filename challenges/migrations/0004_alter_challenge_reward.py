# Generated by Django 4.0.4 on 2022-07-26 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0003_challenge_reward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='reward',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]