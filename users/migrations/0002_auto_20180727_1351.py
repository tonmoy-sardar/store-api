# Generated by Django 2.0.5 on 2018-07-27 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='contact_no',
            field=models.BigIntegerField(unique=True),
        ),
    ]