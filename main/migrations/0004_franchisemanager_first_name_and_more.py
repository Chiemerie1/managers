# Generated by Django 4.1.5 on 2023-03-12 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_franchisemanager_delete_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='franchisemanager',
            name='First_name',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='franchisemanager',
            name='last_name',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
