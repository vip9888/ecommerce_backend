from rest_framework.routers import DefaultRouter
from apps.orders.views import OrderViewSet



from django.urls import path, include

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename= 'orders')

urlpatterns = [
    path('', include(router.urls)),
]