from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils import timezone
from decimal import Decimal

from .models import Bill, TaxSettings
from .serializers import BillSerializer
from apps.orders.models import Order


class GenerateBillView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)

        # Return existing bill if already generated
        existing = Bill.objects.filter(order=order).first()
        if existing:
            return Response({
                'success': True,
                'message': 'Bill retrieved successfully.',
                'data':    BillSerializer(existing).data
            })

        # Get current tax settings from DB
        tax       = TaxSettings.get_active()
        total     = order.total_amount

        if tax.is_gst_enabled:
            cgst_rate = tax.cgst_percent / Decimal('100')
            sgst_rate = tax.sgst_percent / Decimal('100')
            cgst      = round(total * cgst_rate, 2)
            sgst      = round(total * sgst_rate, 2)
        else:
            cgst = Decimal('0.00')
            sgst = Decimal('0.00')

        grand_total = total + cgst + sgst

        bill = Bill.objects.create(
            order        = order,
            total_amount = total,
            cgst         = cgst,
            sgst         = sgst,
            grand_total  = grand_total
        )

        order.status = 'billed'
        order.save()

        return Response({
            'success': True,
            'message': 'Bill generated successfully!',
            'data':    BillSerializer(bill).data
        }, status=status.HTTP_201_CREATED)


class BillDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        bill  = get_object_or_404(Bill, order=order)
        return Response({
            'success': True,
            'data':    BillSerializer(bill).data
        })


class MarkPaidView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, bill_id):
        bill         = get_object_or_404(Bill, id=bill_id)
        bill.is_paid = True
        bill.save()
        return Response({
            'success': True,
            'message': f'Bill #{bill.id} marked as paid.',
            'data':    BillSerializer(bill).data
        })


class TodayBillsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = timezone.now().date()
        bills = Bill.objects.filter(
            created_at__date=today
        ).select_related('order__table').prefetch_related(
            'order__items__menu_item'
        ).order_by('created_at')
        return Response({
            'success': True,
            'data':    BillSerializer(bills, many=True).data
        })


class TaxSettingsView(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        tax = TaxSettings.get_active()
        return Response({
            'success': True,
            'data': {
                'cgst':    float(tax.cgst_percent),
                'sgst':    float(tax.sgst_percent),
                'enabled': tax.is_gst_enabled,
            }
        })

    def patch(self, request):
        tax = TaxSettings.get_active()

        cgst    = request.data.get('cgst', tax.cgst_percent)
        sgst    = request.data.get('sgst', tax.sgst_percent)
        enabled = request.data.get('enabled', tax.is_gst_enabled)

        try:
            cgst = Decimal(str(cgst))
            sgst = Decimal(str(sgst))
        except Exception:
            return Response(
                {'success': False, 'message': 'Invalid tax values.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not (0 <= cgst <= 50 and 0 <= sgst <= 50):
            return Response(
                {'success': False, 'message': 'Tax must be between 0 and 50.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        tax.cgst_percent   = cgst
        tax.sgst_percent   = sgst
        tax.is_gst_enabled = bool(enabled)
        tax.save()

        return Response({
            'success': True,
            'message': 'Tax settings updated successfully.',
            'data': {
                'cgst':    float(tax.cgst_percent),
                'sgst':    float(tax.sgst_percent),
                'enabled': tax.is_gst_enabled,
            }
        })