from rest_framework import serializers
from .models import RestaurantTable


class RestaurantTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantTable
        fields = ['id', 'table_number', 'qr_token', 'qr_code_url', 'is_active']
        read_only_fields = ['id', 'qr_token', 'qr_code_url']
