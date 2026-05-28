from django.db import models
import uuid


class RestaurantTable(models.Model):
    table_number = models.IntegerField(unique=True)
    qr_token     = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )
    qr_code_url  = models.TextField(blank=True, null=True)
    is_active    = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'restaurant_tables'
        ordering = ['table_number']
        verbose_name        = 'Restaurant Table'
        verbose_name_plural = 'Restaurant Tables'

    def __str__(self):
        return f"Table {self.table_number}"