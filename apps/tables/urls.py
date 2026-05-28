from django.urls import path
from .views import TableListView, TableQRView, TableMenuView

urlpatterns = [
    path('', TableListView.as_view(), name='table-list'),
    path('<int:table_id>/qr/', TableQRView.as_view(), name='table-qr'),
    path('<int:table_id>/menu/', TableMenuView.as_view(), name='table-menu'),
]
