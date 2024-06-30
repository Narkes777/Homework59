from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product, Electronics, Clothing, Books, Order
from .serializers import ProductSerializer, ElectronicsSerializer, ClothingSerializer, BooksSerializer, OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'], url_path='by-price/(?P<price>[^/.]+)')
    def get_by_price(self, request, price=None):
        products = Product.objects.filter(price=price)
        page = self.paginate_queryset(products)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='orders')
    def get_orders(self, request, pk=None):
        product = self.get_object()
        orders = product.orders.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
