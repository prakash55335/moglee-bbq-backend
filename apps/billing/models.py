from django.db import models
from apps.orders.models import Order


class TaxSettings(models.Model):
    cgst_percent   = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    sgst_percent   = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    is_gst_enabled = models.BooleanField(default=False)
    updated_at     = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tax_settings'

    def __str__(self):
        return f'GST: CGST {self.cgst_percent}% + SGST {self.sgst_percent}%'

    @classmethod
    def get_active(cls):
        obj, _ = cls.objects.get_or_create(
            id=1,
            defaults={
                'cgst_percent':   0,
                'sgst_percent':   0,
                'is_gst_enabled': False,
            }
        )
        return obj


class Bill(models.Model):
    order        = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name='bill'
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    cgst         = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sgst         = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    grand_total  = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid      = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table            = 'bills'
        ordering            = ['-created_at']
        verbose_name        = 'Bill'
        verbose_name_plural = 'Bills'

    def __str__(self):
        return f"Bill #{self.id} - Order #{self.order.id} - ₹{self.grand_total}"

    def calculate_gst(self):
        from decimal import Decimal
        tax = TaxSettings.get_active()
        if tax.is_gst_enabled:
            cgst_rate = tax.cgst_percent / Decimal('100')
            sgst_rate = tax.sgst_percent / Decimal('100')
            self.cgst = round(self.total_amount * cgst_rate, 2)
            self.sgst = round(self.total_amount * sgst_rate, 2)
        else:
            self.cgst = Decimal('0.00')
            self.sgst = Decimal('0.00')
        self.grand_total = self.total_amount + self.cgst + self.sgst
        return self.grand_total