# Generated by Django 2.0.5 on 2018-07-31 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_category', '0002_auto_20180731_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appcategories',
            name='category_code',
            field=models.CharField(max_length=20),
        ),
    ]