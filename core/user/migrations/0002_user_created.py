# Generated by Django 4.1.7 on 2024-04-19 19:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]