# Generated by Django 5.1.5 on 2025-01-25 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solaris_app', '0003_character_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='user',
        ),
    ]
