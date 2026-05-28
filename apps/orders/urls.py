# new one 

from django.urls import path
from .views import (
    PlaceOrderView,
    PendingOrdersView,
    ReadyOrdersView,
    UpdateOrderStatusView,
    OrderDetailView,
    EditOrderView,
    TableOrdersView,
)

urlpatterns = [
    path('place/',                         PlaceOrderView.as_view(),        name='place-order'),
    path('pending/',                       PendingOrdersView.as_view(),     name='pending-orders'),
    path('ready/',                         ReadyOrdersView.as_view(),       name='ready-orders'),
    path('table/<int:table_id>/',          TableOrdersView.as_view(),       name='table-orders'),   # ← MUST be before <int:order_id>/
    path('<int:order_id>/',                OrderDetailView.as_view(),       name='order-detail'),
    path('<int:order_id>/status/',         UpdateOrderStatusView.as_view(), name='update-status'),
    path('<int:order_id>/edit/',           EditOrderView.as_view(),         name='edit-order'),
]













# from django.urls import path
# from .views import (
#     PlaceOrderView,
#     PendingOrdersView,
#     ReadyOrdersView,
#     UpdateOrderStatusView,
#     OrderDetailView,
#     EditOrderView,         # ← NEW
#     TableOrdersView         # ← NEW
# )

# urlpatterns = [
#     path('place/',                  PlaceOrderView.as_view(),        name='place-order'),
#     path('pending/',                PendingOrdersView.as_view(),     name='pending-orders'),
#     path('ready/',                  ReadyOrdersView.as_view(),       name='ready-orders'),
#     path('<int:order_id>/',         OrderDetailView.as_view(),       name='order-detail'),
#     path('<int:order_id>/status/',  UpdateOrderStatusView.as_view(), name='update-status'),
#     path('<int:order_id>/edit/',    EditOrderView.as_view(),         name='edit-order'),  # ← NEW
#     path('table/<int:table_id>/',   TableOrdersView.as_view(), name='table-orders'),   # ← NEW


# ]












# old one


# from django.urls import path
# from .views import PlaceOrderView, PendingOrdersView, ReadyOrdersView, UpdateOrderStatusView, OrderDetailView

# urlpatterns = [
#     path('place/', PlaceOrderView.as_view(), name='place-order'),
#     path('pending/', PendingOrdersView.as_view(), name='pending-orders'),
#     path('ready/', ReadyOrdersView.as_view(), name='ready-orders'),
#     path('<int:order_id>/', OrderDetailView.as_view(), name='order-detail'),
#     path('<int:order_id>/status/', UpdateOrderStatusView.as_view(), name='update-status'),
# ]
