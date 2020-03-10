from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=True)
    is_farmer   = models.BooleanField(default=False)
    is_vet   = models.BooleanField(default=False)
    phoneNumber = models.CharField(max_length=20, blank=True)

class VetProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='vet_profile')
	bio = models.CharField(max_length=30, blank=True)
	specialistIn = models.CharField(max_length=30, blank=True)
	experience = models.CharField(max_length=30, blank=True)
	rating = models.CharField(max_length=30, blank=True)
	location = models.CharField(max_length=30, blank=True)
  
class CustomerProfile(models.Model):
  	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='customer_profile')

class FarmerProfile(models.Model):
  	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='farmer_profile')
	
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	print('****', created)
	if instance.is_customer:
		CustomerProfile.objects.get_or_create(user = instance)
	if instance.is_farmer:
		FarmerProfile.objects.get_or_create(user = instance)
	else:
		VetProfile.objects.get_or_create(user = instance)
	
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	print('_-----')	
	# print(instance.internprofile.bio, instance.internprofile.location)
	if instance.is_customer:
		instance.customer_profile.save()
	if instance.is_farmer:
		instance.farmer_profile.save()
	else:
		VetProfile.objects.get_or_create(user = instance)
