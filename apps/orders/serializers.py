from rest_framework import serializers
from .models import Order, OrderItem
from apps.menu.models import MenuItem


class OrderItemInputSerializer(serializers.Serializer):
    menu_item_id = serializers.IntegerField()
    quantity     = serializers.IntegerField(min_value=1)


class PlaceOrderSerializer(serializers.Serializer):
    table_id       = serializers.IntegerField()
    customer_note  = serializers.CharField(required=False, allow_blank=True)
    customer_name  = serializers.CharField(required=False, allow_blank=True)
    customer_phone = serializers.CharField(required=False, allow_blank=True)
    items          = OrderItemInputSerializer(many=True)


class OrderItemSerializer(serializers.ModelSerializer):
    # ── these are what CustomerOrdersPage needs ──
    name       = serializers.CharField(source='menu_item.name',  read_only=True)
    image      = serializers.CharField(source='menu_item.image', read_only=True)
    menu_item_id = serializers.IntegerField(source='menu_item.id', read_only=True)

    # ── keep item_name for admin OrderPage compatibility ──
    item_name  = serializers.CharField(source='menu_item.name',  read_only=True)

    class Meta:
        model  = OrderItem
        fields = [
            'id',
            'menu_item_id',   # ← for edit order
            'name',           # ← for customer orders page
            'item_name',      # ← for admin orders page (keep for compatibility)
            'image',          # ← for customer orders page thumbnails
            'quantity',
            'unit_price',
            'subtotal',
        ]


class OrderSerializer(serializers.ModelSerializer):
    items        = OrderItemSerializer(many=True, read_only=True)
    table_number = serializers.IntegerField(source='table.table_number', read_only=True)

    class Meta:
        model  = Order
        fields = [
            'id',
            'table_number',
            'status',
            'total_amount',
            'customer_note',
            'customer_name',
            'customer_phone',
            'created_at',
            'items',
        ]






























# from rest_framework import serializers
# from .models import Order, OrderItem
# from apps.menu.models import MenuItem


# class OrderItemInputSerializer(serializers.Serializer):
#     menu_item_id = serializers.IntegerField()
#     quantity     = serializers.IntegerField(min_value=1)


# class PlaceOrderSerializer(serializers.Serializer):
#     table_id       = serializers.IntegerField()
#     customer_note  = serializers.CharField(required=False, allow_blank=True)
#     customer_name  = serializers.CharField(required=False, allow_blank=True)   # ← NEW
#     customer_phone = serializers.CharField(required=False, allow_blank=True)   # ← NEW
#     items          = OrderItemInputSerializer(many=True)


# class OrderItemSerializer(serializers.ModelSerializer):
#     item_name = serializers.CharField(source='menu_item.name', read_only=True)

#     class Meta:
#         model  = OrderItem
#         fields = ['id', 'item_name', 'quantity', 'unit_price', 'subtotal']


# class OrderSerializer(serializers.ModelSerializer):
#     items          = OrderItemSerializer(many=True, read_only=True)
#     table_number   = serializers.IntegerField(source='table.table_number', read_only=True)

#     class Meta:
#         model  = Order
#         fields = [
#             'id', 'table_number', 'status',
#             'total_amount', 'customer_note',
#             'customer_name', 'customer_phone',   # ← NEW
#             'created_at', 'items'
#         ]