# Generated by Django 2.0.5 on 2018-07-28 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appproducts',
            name='hide_org_price_status',
            field=models.IntegerField(choices=[('1', 'hide'), ('0', 'None')], default=0),
        ),
    ]
