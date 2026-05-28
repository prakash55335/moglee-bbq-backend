from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class AdminUserManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Username is required')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')
        return self.create_user(username, password, **extra_fields)


class AdminUser(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = [
        ('admin',   'Admin'),
        ('kitchen', 'Kitchen'),
        ('billing', 'Billing'),
    ]

    username   = models.CharField(max_length=50, unique=True)
    full_name  = models.CharField(max_length=100)
    role       = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='admin'
    )
    is_active  = models.BooleanField(default=True)
    is_staff   = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AdminUserManager()

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        db_table = 'admin_users'
        verbose_name = 'Admin User'
        verbose_name_plural = 'Admin Users'

    def __str__(self):
        return f"{self.full_name} ({self.role})"