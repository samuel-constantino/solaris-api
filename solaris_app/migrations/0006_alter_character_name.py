# Generated by Django 5.1.5 on 2025-01-25 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solaris_app', '0005_character_race'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
