from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
admin.site.site_header = 'User Portal Admin'
admin.site.site_title  = 'User Management Portal'
admin.site.index_title = 'Welcome to User Management Portal' 