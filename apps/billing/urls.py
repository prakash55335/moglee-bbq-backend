from django.urls import path
from .views import (
    GenerateBillView,
    BillDetailView,
    MarkPaidView,
    CompleteBillView,  # 🌟 ADDED THIS IMPORT HERE
    TodayBillsView,
    TaxSettingsView,
)

urlpatterns = [
    # 1. Place static paths and explicit structural endpoints at the TOP 🔝
    path('today/',                   TodayBillsView.as_view(),    name='today-bills'),
    path('tax-settings/',            TaxSettingsView.as_view(),   name='tax-settings'),
    path('generate/<int:order_id>/', GenerateBillView.as_view(),  name='generate-bill'),
    
    # 2. Place specific action resource updates next
    path('<int:bill_id>/complete/',  CompleteBillView.as_view(),  name='complete-bill'),
    path('<int:bill_id>/paid/',      MarkPaidView.as_view(),      name='mark-paid'),
    
    # 3. Keep generic fallback tracking IDs at the bottom
    path('<int:order_id>/',          BillDetailView.as_view(),    name='bill-detail'),
]