# Generated by Django 2.0.5 on 2018-07-25 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_messenger', '0004_auto_20180724_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appmessenger',
            name='app_id',
        ),
        migrations.DeleteModel(
            name='AppMessenger',
        ),
    ]
