from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, ElectronicsViewSet, ClothingViewSet, BooksViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'electronics', ElectronicsViewSet)
router.register(r'clothing', ClothingViewSet)
router.register(r'books', BooksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
