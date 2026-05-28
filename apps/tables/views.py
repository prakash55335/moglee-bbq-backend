from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from django.http import HttpResponse
from .models import RestaurantTable
from .serializers import RestaurantTableSerializer
import qrcode
import io
import socket


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return '127.0.0.1'


class TableListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tables = RestaurantTable.objects.filter(
            is_active=True
        ).order_by('table_number')
        serializer = RestaurantTableSerializer(tables, many=True)
        return Response({
            'success': True,
            'data': serializer.data
        })

    def post(self, request):
        serializer = RestaurantTableSerializer(data=request.data)
        if serializer.is_valid():
            table = serializer.save()
            return Response({
                'success': True,
                'data': RestaurantTableSerializer(table).data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class TableQRView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, table_id):
        try:
            table = RestaurantTable.objects.get(id=table_id)

            ip = get_local_ip()
            menu_url = f"http://{ip}:5173/menu?tableId={table.id}&token={table.qr_token}"

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_Q,
                box_size=10,
                border=4,
            )
            qr.add_data(menu_url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            buffer = io.BytesIO()
            img.save(buffer, format='PNG')
            buffer.seek(0)

            return HttpResponse(
                buffer.getvalue(),
                content_type='image/png'
            )
        except RestaurantTable.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Table not found.'
            }, status=status.HTTP_404_NOT_FOUND)


class TableMenuView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, table_id):
        try:
            table = RestaurantTable.objects.get(id=table_id)
            return Response({
                'success': True,
                'data': RestaurantTableSerializer(table).data
            })
        except RestaurantTable.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Table not found.'
            }, status=status.HTTP_404_NOT_FOUND)