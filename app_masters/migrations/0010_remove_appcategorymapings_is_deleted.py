# Generated by Django 2.0.5 on 2018-07-09 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_masters', '0009_appcategorymapings_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appcategorymapings',
            name='is_deleted',
        ),
    ]