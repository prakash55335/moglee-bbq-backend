from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Directly link the v1 path wrapper to your existing authentication app
    path('api/v1/auth/', include('apps.authentication.urls')),
    path('api/v1/menu/', include('apps.menu.urls')),
    path('api/v1/tables/', include('apps.tables.urls')),
    path('api/v1/orders/', include('apps.orders.urls')),
    path('api/v1/billing/', include('apps.billing.urls')),
]
