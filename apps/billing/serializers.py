from rest_framework import serializers
from .models import Bill
from apps.orders.serializers import OrderSerializer


class BillSerializer(serializers.ModelSerializer):
    order_details = OrderSerializer(source='order', read_only=True)

    class Meta:
        model  = Bill
        fields = [
            'id', 'order', 'order_details',
            'total_amount', 'cgst', 'sgst',
            'grand_total', 'is_paid', 'created_at'
        ]