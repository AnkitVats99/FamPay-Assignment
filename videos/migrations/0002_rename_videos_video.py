# Generated by Django 4.1.5 on 2023-01-06 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Videos',
            new_name='Video',
        ),
    ]