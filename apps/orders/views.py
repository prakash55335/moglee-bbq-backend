from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Order, OrderItem
from .serializers import PlaceOrderSerializer, OrderSerializer
from apps.menu.models import MenuItem
from apps.tables.models import RestaurantTable


class PlaceOrderView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PlaceOrderSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'success': False,
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        data  = serializer.validated_data
        table = get_object_or_404(
            RestaurantTable,
            id=data['table_id'],
            is_active=True
        )

        order = Order.objects.create(
            table          = table,
            customer_note  = data.get('customer_note', ''),
            customer_name  = data.get('customer_name', ''),
            customer_phone = data.get('customer_phone', ''),
            status         = 'pending'
        )

        total = 0
        for item_data in data['items']:
            menu_item = get_object_or_404(
                MenuItem,
                id=item_data['menu_item_id'],
                is_available=True
            )
            qty      = item_data['quantity']
            subtotal = menu_item.price * qty

            OrderItem.objects.create(
                order      = order,
                menu_item  = menu_item,
                quantity   = qty,
                unit_price = menu_item.price,
                subtotal   = subtotal
            )
            total += subtotal

        order.total_amount = total
        order.save()

        return Response({
            'success':  True,
            'message':  'Order placed successfully!',
            'order_id': order.id,
            'data':     OrderSerializer(order).data
        }, status=status.HTTP_201_CREATED)


class PendingOrdersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(
            status__in=['pending', 'preparing']
        ).select_related('table').prefetch_related(
            'items__menu_item'
        ).order_by('created_at')

        return Response({
            'success': True,
            'data':    OrderSerializer(orders, many=True).data
        })


class ReadyOrdersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(
            status='ready'
        ).select_related('table').prefetch_related(
            'items__menu_item'
        ).order_by('created_at')

        return Response({
            'success': True,
            'data':    OrderSerializer(orders, many=True).data
        })


class UpdateOrderStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, order_id):
        order      = get_object_or_404(Order, id=order_id)
        new_status = request.data.get('status')

        valid_statuses = ['pending', 'preparing', 'ready', 'billed']
        if new_status not in valid_statuses:
            return Response({
                'success': False,
                'message': f'Invalid status. Choose from {valid_statuses}'
            }, status=status.HTTP_400_BAD_REQUEST)

        order.status = new_status
        order.save()

        return Response({
            'success': True,
            'message': f'Order #{order.id} updated to {new_status}.',
            'data':    OrderSerializer(order).data
        })


class OrderDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        return Response({
            'success': True,
            'data':    OrderSerializer(order).data
        })


class EditOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)

        if order.status == 'billed':
            return Response({
                'success': False,
                'message': 'Cannot edit a billed order.'
            }, status=status.HTTP_400_BAD_REQUEST)

        items_data    = request.data.get('items', [])
        customer_note = request.data.get('customer_note', order.customer_note)

        if not items_data:
            return Response({
                'success': False,
                'message': 'Items cannot be empty.'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Delete existing items and recreate
        OrderItem.objects.filter(order=order).delete()

        total = 0
        for item_data in items_data:
            # ✅ FIX: safely get menu_item_id from different sources
            menu_item_id = item_data.get('menu_item_id') or item_data.get('menu_item')
            quantity     = int(item_data.get('quantity', 1))

            if not menu_item_id:
                return Response({
                    'success': False,
                    'message': f'Missing menu_item_id in item: {item_data}'
                }, status=status.HTTP_400_BAD_REQUEST)

            menu_item = get_object_or_404(MenuItem, id=menu_item_id)
            subtotal  = menu_item.price * quantity

            OrderItem.objects.create(
                order      = order,
                menu_item  = menu_item,
                quantity   = quantity,
                unit_price = menu_item.price,
                subtotal   = subtotal
            )
            total += subtotal

        order.total_amount  = total
        order.customer_note = customer_note
        order.customer_name = request.data.get('customer_name', order.customer_name)
        order.customer_phone = request.data.get('customer_phone', order.customer_phone)
        order.save()

        return Response({
            'success': True,
            'message': f'Order #{order.id} updated successfully!',
            'data':    OrderSerializer(order).data
        })




        # new one



class TableOrdersView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, table_id):
        orders = Order.objects.filter(
            table__id=table_id
        ).prefetch_related('items__menu_item').order_by('-created_at')[:10]
        return Response({
            'success': True,
            'data': OrderSerializer(orders, many=True).data
        })