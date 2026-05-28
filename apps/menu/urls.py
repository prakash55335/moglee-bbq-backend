from django.urls import path
from .views import (
    MenuListView,
    MenuItemCreateView,
    MenuItemDetailView,
    MenuItemToggleView,
)

urlpatterns = [
    path('',                      MenuListView.as_view(),       name='menu-list'),
    path('items/',                MenuItemCreateView.as_view(), name='menu-item-create'),
    path('items/<int:item_id>/',  MenuItemDetailView.as_view(), name='menu-item-detail'),
    path('<int:item_id>/toggle/', MenuItemToggleView.as_view(), name='menu-item-toggle'),
]