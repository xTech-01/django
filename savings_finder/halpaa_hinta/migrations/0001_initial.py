# Generated by Django 4.2.2 on 2023-06-28 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('image', models.CharField(blank=True, max_length=100)),
                ('price1', models.IntegerField(blank=True, default=None, null=True)),
                ('source1', models.CharField(max_length=100)),
                ('price2', models.IntegerField(blank=True, default=None, null=True)),
                ('source2', models.CharField(max_length=100)),
                ('price3', models.IntegerField(blank=True, default=None, null=True)),
                ('source3', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=100)),
                ('favourite_music', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('token', models.CharField(max_length=100)),
                ('payment_amount', models.IntegerField(default=0)),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('invoice_number', models.AutoField(primary_key=True, serialize=False)),
                ('payment_status', models.CharField(default='pending', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='halpaa_hinta.users')),
            ],
        ),
    ]