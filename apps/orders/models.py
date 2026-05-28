from django.db import models
from apps.tables.models import RestaurantTable
from apps.menu.models import MenuItem


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('preparing', 'Preparing'),
        ('ready',     'Ready'),
        ('billed',    'Billed'),
    ]

    table         = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE, related_name='orders')
    status        = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount  = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    customer_note = models.TextField(blank=True, default='')
    customer_name = models.CharField(max_length=100, blank=True, default='')   # ← NEW
    customer_phone = models.CharField(max_length=15, blank=True, default='')   # ← NEW
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - Table {self.table.table_number}"


class OrderItem(models.Model):
    order      = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item  = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity   = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal   = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.menu_item.name} × {self.quantity}"