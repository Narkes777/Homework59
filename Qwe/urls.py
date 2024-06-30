from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, ElectronicsViewSet, ClothingViewSet, BooksViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'electronics', ElectronicsViewSet)
router.register(r'clothing', ClothingViewSet)
router.register(r'books', BooksViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
