from django.contrib import admin
from .models import MenuCategory, MenuItem


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display  = ['name', 'display_order', 'is_active']
    list_filter   = ['is_active']
    search_fields = ['name']
    ordering      = ['display_order']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display  = ['name', 'category', 'price', 'is_veg', 'is_available']
    list_filter   = ['category', 'is_veg', 'is_available']
    search_fields = ['name']
    ordering      = ['category', 'display_order']