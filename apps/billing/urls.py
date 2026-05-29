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
    path('generate/<int:order_id>/', GenerateBillView.as_view(),  name='generate-bill'),
    path('<int:order_id>/',          BillDetailView.as_view(),    name='bill-detail'),
    path('<int:bill_id>/paid/',      MarkPaidView.as_view(),      name='mark-paid'),
    
    # 🌟 ADDED THIS ROUTE HERE TO MAP THE FRONTEND '/complete/' REQUEST:
    path('<int:bill_id>/complete/',  CompleteBillView.as_view(),  name='complete-bill'),
    
    path('today/',                   TodayBillsView.as_view(),    name='today-bills'),
    path('tax-settings/',            TaxSettingsView.as_view(),   name='tax-settings'),
]
