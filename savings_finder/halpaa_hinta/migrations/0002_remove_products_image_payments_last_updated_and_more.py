# Generated by Django 4.2.2 on 2023-07-06 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halpaa_hinta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
        migrations.AddField(
            model_name='payments',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='image1',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='last_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]