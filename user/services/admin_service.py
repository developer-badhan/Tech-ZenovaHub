# from user.models import User
# from constants import Role
# from django.contrib.auth import authenticate

# # Admin Create
# def create_admin(data):
#     user = User.objects.create_user(
#         username=data['email'], 
#         email=data['email'],
#         first_name=data['first_name'],
#         last_name=data['last_name'],
#         dob=data['dob'],
#         phone=data.get('phone'),
#         gender=data.get('gender'),
#         profile_photo=data.get('profile_photo'),
#         role=Role.ADMIN,
#         is_staff=True,
#         is_superuser=True
#     )
#     user.set_password(data['password'])
#     user.save()
#     return user


# # Admin Authentication
# def authenticate_admin(email, password):
#     user = authenticate(email=email, password=password)
#     if user and user.role == Role.ADMIN:
#         return user
#     return None



# # user/services.py

# from django.shortcuts import get_object_or_404

# # Admin Update
# def update_admin(user_id, data):
#     user = get_object_or_404(User, pk=user_id, role=Role.ADMIN)
#     for field, value in data.items():
#         setattr(user, field, value)
#     user.save()
#     return user

# # Admin Delete
# def delete_admin(user_id):
#     user = get_object_or_404(User, pk=user_id, role=Role.ADMIN)
#     user.delete()
#     return True




from urllib import request
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from user.models import User
from constants.enums import Role


# ────────────── ADMIN SERVICES (FUNCTIONAL) ──────────────

def create_admin(data: dict):
    """Signup new admin"""
    try:
        admin = User.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            dob=data['dob'],
            email=data['email'],
            role=Role.ADMIN,
            is_active=data.get('is_active', True),
            is_staff=True,
            password=make_password(data['password'])
        )
        return admin, None
    except IntegrityError as e:
        return None, f"Email already exists: {str(e)}"
    except Exception as e:
        return None, str(e)


def authenticate_admin(email: str, password: str, request):
    """Authenticate and login admin"""
    try:
        user = User.objects.filter(email=email, role=Role.ADMIN).first()
        if user and check_password(password, user.password):
            request.session['is_authenticated'] = True
            request.session['user_id'] = user.id
            request.session['user_role'] = user.role
            return user, None
        return None, "Invalid email or password"
    except Exception as e:
        return None, str(e)


def logout_admin(request):
    """Logout admin"""
    try:
        request.session.flush()
        logout(request)
        return True, None
    except Exception as e:
        return False, str(e)


def update_admin(pk: int, data: dict):
    """Update admin profile"""
    try:
        admin = get_object_or_404(User, pk=pk, role=Role.ADMIN)
        admin.first_name = data['first_name']
        admin.last_name = data['last_name']
        admin.dob = data['dob']
        admin.email = data['email']
        admin.is_active = data.get('is_active', True)
        admin.save()
        return admin, None
    except Exception as e:
        return None, str(e)


def delete_admin(pk: int):
    """Delete admin account"""
    try:
        admin = get_object_or_404(User, pk=pk, role=Role.ADMIN)
        admin.delete()
        return True, None
    except Exception as e:
        return False, str(e)




from user.models import User
from constants.enums import Role
from shop.models import Product, Category, Review, Shipment


def get_dashboard_data():
    """Fetch stats for admin dashboard"""
    try:
        # Admin Details
        admin = get_object_or_404(User, pk=request.session['user_id'], role=Role.ADMIN)
        # Users
        total_admins = User.objects.filter(role=Role.ADMIN).count()
        total_staff = User.objects.filter(role=Role.ENDUSER_STAFF).count()
        total_customers = User.objects.filter(role=Role.ENDUSER_CUSTOMER).count()

        # Business Objects
        total_products = Product.objects.count()
        total_categories = Category.objects.count()
        total_reviews = Review.objects.count()
        total_shipments = Shipment.objects.count()

        return {
            "admin": admin,
            "total_admins": total_admins,
            "total_staff": total_staff,
            "total_customers": total_customers,
            "total_products": total_products,
            "total_categories": total_categories,
            "total_reviews": total_reviews,
            "total_shipments": total_shipments,
        }, None
    except Exception as e:
        return None, str(e)
