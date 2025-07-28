# Import the serializers module from Django REST Framework
from rest_framework import serializers
# Import the User model from the current app's models
from .models import User

# Define a serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    # Meta class to specify model and fields to be serialized
    class Meta:
        model = User  # The model to serialize
        fields = ["id", "name", "email", "phone"]  # Fields to include in the serialization
