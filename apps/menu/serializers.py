from rest_framework import serializers
from .models import MenuCategory, MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MenuItem
        fields = [
            'id', 'category', 'name', 'description',
            'price', 'image', 'is_veg',
            'is_available', 'display_order',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class MenuCategorySerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = MenuCategory
        fields = ['id', 'name', 'display_order', 'is_active', 'items']