# Generated by Django 2.0 on 2020-03-10 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('multiple', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hr_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='internprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intern_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
