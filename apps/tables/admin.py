from django.contrib import admin
from .models import RestaurantTable


@admin.register(RestaurantTable)
class RestaurantTableAdmin(admin.ModelAdmin):
    list_display  = ['table_number', 'qr_token', 'is_active']
    list_filter   = ['is_active']
    ordering      = ['table_number']