# Generated by Django 2.0.5 on 2018-07-27 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_masters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppProductCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('app_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_product_categories', to='app_masters.AppMasters')),
            ],
        ),
        migrations.CreateModel(
            name='AppProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('product_code', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('discounted_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('tags', models.TextField(blank=True, null=True)),
                ('hide_org_price_status', models.BooleanField(choices=[('1', 'hide'), ('0', 'None')], default=0)),
                ('packing_charges', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('app_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_masters.AppMasters')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_products.AppProductCategories')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField(default=True)),
                ('app_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_products.AppProducts')),
            ],
        ),
    ]
