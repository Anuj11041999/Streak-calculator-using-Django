# Generated by Django 4.0.4 on 2022-07-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='money',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
