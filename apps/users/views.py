from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer
from apps.users.serializers import UserRegistrationSerializer

# What it does:
# This view is used to register a new user
# It creates a new user with the provided username, email, and password
# The password is written only (not read) during the creation process
# The create method is overridden to handle the creation of the user
# The user is created using the User.objects.create_user method
# The user is then returned

# CreateAPIView is a pre-built view in Django REST Framework that:
# Only handles POST requests (creating new resources)
# Automatically handles the creation process
# Returns appropriate status codes (201 for creation, 400 for errors)
# Provides a clean, focused API endpoint
# Why use CreateAPIView instead of ViewSet?
# Focused Purpose:
# Registration is a single action (creating a user)
# We don't need other CRUD operations (read, update, delete)
# It's more specific and cleaner than a full ViewSet


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

# Create your views here.