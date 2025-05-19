from django.shortcuts import render
from rest_framework import viewsets
from apps.products.models import Product
from apps.products.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):

# Product.objects.all() is a Django ORM (Object-Relational Mapping) query that retrieves all records from the Product table in the database. Let's break it down:
# Product is your model class that represents the products table in your database
# .objects is a manager that Django automatically adds to every model class. It's the interface through which you interact with the database
# .all() is a method that returns a QuerySet containing all objects in the database for that model

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Create your views here.
