# Generated by Django 2.0.5 on 2018-07-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp_app', '0019_auto_20180706_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempappmasters',
            name='app_url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]