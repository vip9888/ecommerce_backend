from rest_framework.routers import DefaultRouter
from apps.products.views import ProductViewSet


from django.urls import path, include

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
