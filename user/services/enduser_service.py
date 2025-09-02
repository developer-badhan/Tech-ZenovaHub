from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, get_user_model
from constants.enums import Role
from user.models import User


# Authentication
def authenticate_user(email, password):
    try:
        return authenticate(email=email, password=password)
    except Exception as e:
        raise Exception(f"Authentication failed: {str(e)}")


# User Retrieval
def get_user_by_id(user_id):
    try:
        return get_object_or_404(User, pk=user_id)
    except Exception as e:
        raise Exception(f"User with ID {user_id} not found. Error: {str(e)}")


# User Create
def create_user(data):
    try:
        user = User(
            email=data['email'],
            first_name=data['first_name'],
            middle_name=data.get('middle_name', ''),
            last_name=data['last_name'],
            dob=data['dob'],
            phone=data.get('phone'),
            gender=data.get('gender'),
            profile_photo=data.get('profile_photo'),
            role=data['role'],
        )
        user.set_password(data['password']) 
        user.save()
        return user
    except Exception as e:
        raise Exception(f"Failed to create user. Error: {str(e)}")


# User Update
def update_user(user, data):
    try:
        user.first_name = data['first_name']
        user.middle_name = data.get('middle_name')
        user.last_name = data['last_name']
        user.dob = data['dob']
        user.phone = data.get('phone')
        user.gender = data.get('gender')
        user.profile_photo = data.get('profile_photo')
        user.save()
        return user
    except Exception as e:
        raise Exception(f"Failed to update user with ID {user.id}. Error: {str(e)}")


# User Delete
def delete_user(user_id):
    try:
        user = get_object_or_404(User, pk=user_id)
        user.delete()
    except Exception as e:
        raise Exception(f"Failed to delete user with ID {user_id}. Error: {str(e)}")


# Get All Customers
def get_all_customers():
    try:
        User = get_user_model()
        return User.objects.filter(role=Role.ENDUSER_CUSTOMER)
    except Exception as e:
        raise Exception(f"Failed to retrieve customers. Error: {str(e)}")

