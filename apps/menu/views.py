from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from .models import MenuCategory, MenuItem
from .serializers import MenuCategorySerializer, MenuItemSerializer


class MenuListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        categories = MenuCategory.objects.filter(
            is_active=True
        ).prefetch_related('items').order_by('display_order')
        return Response({
            'success': True,
            'data': MenuCategorySerializer(categories, many=True).data
        })


class MenuItemCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            item = serializer.save()
            return Response({
                'success': True,
                'message': f'{item.name} created.',
                'data': MenuItemSerializer(item).data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class MenuItemDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, item_id):
        try:
            return MenuItem.objects.get(id=item_id)
        except MenuItem.DoesNotExist:
            return None

    def patch(self, request, item_id):
        item = self.get_object(item_id)
        if not item:
            return Response(
                {'success': False, 'message': 'Item not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = MenuItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data})
        return Response(
            {'success': False, 'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, item_id):
        item = self.get_object(item_id)
        if not item:
            return Response(
                {'success': False, 'message': 'Item not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        name = item.name
        item.delete()
        return Response({'success': True, 'message': f'{name} deleted.'})


class MenuItemToggleView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, item_id):
        try:
            item = MenuItem.objects.get(id=item_id)
            item.is_available = not item.is_available
            item.save()
            return Response({
                'success': True,
                'message': f'{item.name} availability updated.',
                'is_available': item.is_available
            })
        except MenuItem.DoesNotExist:
            return Response(
                {'success': False, 'message': 'Item not found.'},
                status=status.HTTP_404_NOT_FOUND
            )