from rest_framework import serializers
from .models import Order, OrderItem
from apps.products.serializers import ProductSerializer

# This is the special nested used by Djando Rest Framework to serialize nested objects  
# The inner Meta class is a convention used by DRF to specify metadata about the serializer. It's not a regular nested class - it's a special class that DRF looks for to get configuration information. The Meta class tells DRF:
# Which model to use (model = OrderItem)
# Which fields to include in the serialization (fields = ['id', 'product', 'quantity', 'price'])

# The outer class defines that we want to use ProductSerializer for the product field
# The inner Meta class tells DRF to use the OrderItem model and include only the specified fields in the serialization

class OrderItemSerializer(serializers.ModelSerializer):
    # this is the nested serializer for the order item
    # This tells DRF: “When serializing OrderItem, use the full ProductSerializer to show the product’s full info.”
    product = ProductSerializer(read_only=True)
    

    # This is meta class for the order item serializer
    # it is used to tell django that we want to serialize the order item model
    # and we want to show the id, product, quantity and price of the order item
    class Meta:
        model = OrderItem
        # this is the fields that we want to serialize
        # we want to show the id, product, quantity and price of the order item 
        # these fields will be mapped automatically by django
        fields = ['id', 'product', 'quantity', 'price']



class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'is_paid', 'items']
