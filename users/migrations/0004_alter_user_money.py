# Generated by Django 4.0.4 on 2022-07-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='money',
            field=models.IntegerField(default=0),
        ),
    ]
