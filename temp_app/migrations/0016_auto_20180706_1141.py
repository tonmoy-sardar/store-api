# Generated by Django 2.0.5 on 2018-07-06 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp_app', '0015_auto_20180704_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempappmasters',
            name='business_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]