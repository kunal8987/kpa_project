# Create your models here.
from django.db import models

# Define a custom User model
class User(models.Model):
    # User's full name
    name = models.CharField(max_length=100)
    # User's email address, must be unique
    email = models.EmailField(unique=True)
    # User's phone number, must be unique
    phone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        # String representation returns the user's name
        return self.name
