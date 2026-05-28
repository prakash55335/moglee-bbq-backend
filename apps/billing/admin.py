from django.contrib import admin
from .models import Bill


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display  = ['id', 'order', 'total_amount', 'cgst', 'sgst', 'grand_total', 'is_paid']
    list_filter   = ['is_paid']
    ordering      = ['-created_at']
    readonly_fields = ['cgst', 'sgst', 'grand_total']