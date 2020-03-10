# Generated by Django 2.0 on 2020-03-10 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('multiple', '0002_auto_20200310_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='FarmerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='VetProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=30)),
                ('specialistIn', models.CharField(blank=True, max_length=30)),
                ('experience', models.CharField(blank=True, max_length=30)),
                ('rating', models.CharField(blank=True, max_length=30)),
                ('location', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='hrprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='internprofile',
            name='user',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_intern',
            new_name='is_customer',
        ),
        migrations.AddField(
            model_name='user',
            name='is_farmer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_vet',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.DeleteModel(
            name='HRProfile',
        ),
        migrations.DeleteModel(
            name='InternProfile',
        ),
        migrations.AddField(
            model_name='vetprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vet_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='farmerprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='farmer_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
