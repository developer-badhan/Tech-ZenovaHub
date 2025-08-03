# user/services/admin_service.py
from user.models import User
from constants import Role
from django.contrib.auth import authenticate

def create_admin(data):
    user = User.objects.create_user(
        email=data['email'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        password=data['password'],
        role=Role.ADMIN,
        is_staff=True,
        is_superuser=True
    )
    return user

def authenticate_admin(email, password):
    user = authenticate(email=email, password=password)
    if user and user.role == Role.ADMIN:
        return user
    return None
