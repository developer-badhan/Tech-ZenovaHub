from django.shortcuts import get_object_or_404
from user.models import User



def create_user(data):
    user = User.objects.create(
        first_name=data['first_name'],
        middle_name=data.get('middle_name'),
        last_name=data['last_name'],
        dob=data['dob'],
        email=data['email'],
        phone=data.get('phone'),
        gender=data.get('gender'),
        profile_photo=data.get('profile_photo'),
        role=int(data.get('role'))
    )
    return user


def update_user(user, data):
    user.first_name = data['first_name']
    user.middle_name = data.get('middle_name')
    user.last_name = data['last_name']
    user.dob = data['dob']
    user.phone = data.get('phone')
    user.gender = data.get('gender')
    user.profile_photo = data.get('profile_photo')
    user.save()
    return user


def delete_user(user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()


def get_user_by_id(user_id):
    return get_object_or_404(User, pk=user_id)


from django.contrib.auth import authenticate

def authenticate_user(email, password):
    return authenticate(email=email, password=password)
