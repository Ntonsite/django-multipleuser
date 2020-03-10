from django.contrib import admin
from multiple.models import User, CustomerProfile, VetProfile, FarmerProfile
# Register your models here.

admin.site.register(User)
admin.site.register(CustomerProfile)
admin.site.register(VetProfile)
admin.site.register(FarmerProfile)
