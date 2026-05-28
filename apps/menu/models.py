from django.db import models


class MenuCategory(models.Model):
    name          = models.CharField(max_length=100)
    display_order = models.IntegerField(default=0)
    is_active     = models.BooleanField(default=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        db_table  = 'menu_categories'
        ordering  = ['display_order']
        verbose_name        = 'Menu Category'
        verbose_name_plural = 'Menu Categories'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category      = models.ForeignKey(
        MenuCategory,
        on_delete=models.CASCADE,
        related_name='items'
    )
    name          = models.CharField(max_length=200)
    description   = models.TextField(blank=True, null=True)
    price         = models.DecimalField(max_digits=10, decimal_places=2)
    is_veg        = models.BooleanField(default=False)
    is_available  = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    image         = models.URLField(max_length=500, blank=True, null=True)  # Add this line
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'menu_items'
        ordering = ['display_order']
        verbose_name        = 'Menu Item'
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        return f"{self.name} - ₹{self.price}"