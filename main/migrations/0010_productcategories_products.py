# Generated by Django 4.0.3 on 2023-03-12 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_products_category_delete_productcategories_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.franchisemanager')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('item', models.CharField(max_length=50)),
                ('unit_price', models.IntegerField(default=0)),
                ('product_code', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('stock', models.IntegerField(default=0)),
                ('sold', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productcategories')),
            ],
        ),
    ]
