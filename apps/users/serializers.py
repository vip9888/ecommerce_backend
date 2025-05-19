from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# For registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    # What it does:
    # This serializer is used to register a new user
    # It creates a new user with the provided username, email, and password
    # The password is written only (not read) during the creation process
    # The create method is overridden to handle the creation of the user
    # The user is created using the User.objects.create_user method
    # The user is then returned

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



