# Generated by Django 2.0.5 on 2018-07-09 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temp_app', '0022_auto_20180709_1253'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tempappproductcategories',
            unique_together={('app_master', 'category_name')},
        ),
    ]