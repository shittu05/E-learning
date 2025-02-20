from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, Permission


from .models import User  # Import your custom User model

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ( 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ( 'email',)
