from django.shortcuts import render
from rest_framework import viewsets
from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# What it does: permission_classes = [IsAuthenticated]
# IsAuthenticated is a permission class that checks if the user making the request is logged in
# If a user is not logged in, they will receive a 401 Unauthorized error
# Only users who have logged in can access the orders API endpoints
    
    permission_classes = [IsAuthenticated]


# get_queryset(self):
# This function overrides the default queryset behavior of the ModelViewSet. Here's what it does:
# Instead of returning all orders in the database (which would be the default behavior), it filters the orders to only show orders belonging to the currently logged-in user
# self.request.user gets the authenticated user making the request
# This is a security measure to ensure users can only see their own orders
# For example, if user John is logged in, he will only see orders where he is the user, not orders belonging to other users
# perform_create(self, serializer):
# This function overrides the default creation behavior of the ModelViewSet. Here's what it does:
# When a new order is being created, it automatically sets the current user as the owner of that order
# serializer.save(user=self.request.user) saves the order with the authenticated user as the owner
# This ensures that every new order is automatically associated with the user who created it
# For example, when John creates a new order, he doesn't need to specify himself as the user - it's automatically done
# These two functions work together to implement a common security pattern where:
# Users can only see their own orders (get_queryset)
# Users can only create orders for themselves (perform_create)


    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



