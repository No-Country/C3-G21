# Generated by Django 4.1.dev20220219193601 on 2022-03-09 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyprofile',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='companyprofile',
            name='password2',
        ),
    ]
