# Generated by Django 4.0.4 on 2022-07-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_remove_challenge_remainingdays_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='reward',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
