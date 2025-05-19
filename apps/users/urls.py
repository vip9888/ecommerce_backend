from django.urls import path
from apps.users.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]

# When we call RegisterView.as_view():
# 1. It creates a function that:
#    - Instantiates the RegisterView class
#    - Handles the HTTP request
#    - Returns the appropriate response

# What it does:
# This file defines the URLs for the users app
# It includes a single URL for user registration
# The RegisterView is a pre-built view in Django REST Framework that:
# Only handles POST requests (creating new resources)
# Automatically handles the creation process

# Why we are not using router.register?
# We are not using router.register because we are not using a ViewSet
# We are using a CreateAPIView
# A CreateAPIView is more specific and cleaner than a full ViewSet
# when using a generic view, we can use the path function to create the URL
# when using a ViewSet, we need to use the router.register function to create the URL   

# What is the difference between CreateAPIView and CreateModelMixin?
# CreateAPIView is a pre-built view in Django REST Framework that:
# Only handles POST requests (creating new resources)
# Automatically handles the creation process
# Returns appropriate status codes (201 for creation, 400 for errors)
# Provides a clean, focused API endpoint

