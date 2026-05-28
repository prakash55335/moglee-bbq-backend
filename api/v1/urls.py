from django.urls import path, include

urlpatterns = [
    path('auth/',    include('apps.authentication.urls')),
    path('menu/',    include('apps.menu.urls')),
    path('tables/',  include('apps.tables.urls')),
    path('orders/',  include('apps.orders.urls')),
    path('billing/', include('apps.billing.urls')),
]
