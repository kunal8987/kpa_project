from django.urls import path
from .views import CreateUserView, GetUserView

urlpatterns = [
    path("api/users/", CreateUserView.as_view(), name="create_user"),
    path("api/users/<int:pk>/", GetUserView.as_view(), name="get_user"),
]


"""
URL configuration for user-related API endpoints.
This module defines the URL patterns for user creation and retrieval.
Endpoints:
    - POST /api/users/ : Create a new user. Handled by CreateUserView.
    - GET /api/users/<int:pk>/ : Retrieve details of a user by primary key (pk). Handled by GetUserView.
"""