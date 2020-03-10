from django.contrib import admin
from multiple.models import User, HRProfile, InternProfile
# Register your models here.

admin.site.register(User)
admin.site.register(HRProfile)
admin.site.register(InternProfile)
