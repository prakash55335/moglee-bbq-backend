from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AdminUser


@admin.register(AdminUser)
class AdminUserAdmin(UserAdmin):
    list_display  = ['username', 'full_name', 'role', 'is_active']
    list_filter   = ['role', 'is_active']
    search_fields = ['username', 'full_name']
    ordering      = ['username']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('full_name', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'full_name', 'role', 'password1', 'password2'),
        }),
    )