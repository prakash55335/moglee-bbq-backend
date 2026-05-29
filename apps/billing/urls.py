from django.urls import path
from .views import (
    GenerateBillView,
    BillDetailView,
    MarkPaidView,
    TodayBillsView,
    TaxSettingsView,
)

urlpatterns = [
    # Change this line:
    path('generate/<int:order_id>/', GenerateBillView.as_view(), name='generate-bill'),
    
    path('<int:order_id>/',          BillDetailView.as_view(),    name='bill-detail'),
    path('<int:bill_id>/paid/',      MarkPaidView.as_view(),      name='mark-paid'),
    path('today/',                   TodayBillsView.as_view(),    name='today-bills'),
    path('tax-settings/',            TaxSettingsView.as_view(),   name='tax-settings'),
]