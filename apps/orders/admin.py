from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model  = OrderItem
    extra  = 0
    fields = ['menu_item', 'quantity', 'unit_price', 'subtotal']
    readonly_fields = ['subtotal']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display  = ['id', 'table', 'status', 'total_amount', 'created_at']
    list_filter   = ['status']
    search_fields = ['table__table_number']
    ordering      = ['-created_at']
    inlines       = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'menu_item', 'quantity', 'unit_price', 'subtotal']