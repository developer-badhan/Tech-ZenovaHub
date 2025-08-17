from user.models import User
from constants import Role
from django.contrib.auth import authenticate

# Admin Create
def create_admin(data):
    user = User.objects.create_user(
        username=data['email'], 
        email=data['email'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        dob=data['dob'],
        phone=data.get('phone'),
        gender=data.get('gender'),
        profile_photo=data.get('profile_photo'),
        role=Role.ADMIN,
        is_staff=True,
        is_superuser=True
    )
    user.set_password(data['password'])
    user.save()
    return user


# Admin Authentication
def authenticate_admin(email, password):
    user = authenticate(email=email, password=password)
    if user and user.role == Role.ADMIN:
        return user
    return None
