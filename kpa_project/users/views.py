from rest_framework import generics
from .models import User
from .serializers import UserSerializer

# View to handle creation of a new User instance
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()  # Queryset of all User objects
    serializer_class = UserSerializer  # Serializer to use for User

# View to handle retrieval of a single User instance
class GetUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()  # Queryset of all User objects
    serializer_class = UserSerializer  # Serializer to use for User
