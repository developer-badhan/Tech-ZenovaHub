from urllib import request
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from user.models import User
from constants.enums import Role
from shop.models import Product, Category, Review, Shipment,Order,Wishlist


# Admin Create
def create_admin(data: dict):
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


# Admin Authentication
def authenticate_admin(email: str, password: str, request):
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


# Admin Logout
def logout_admin(request):
    try:
        request.session.flush()
        logout(request)
        return True, None
    except Exception as e:
        return False, str(e)


# Admin Update
def update_admin(pk: int, data: dict):
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


# Admin Delete
def delete_admin(pk: int):
    try:
        admin = get_object_or_404(User, pk=pk, role=Role.ADMIN)
        admin.delete()
        return True, None
    except Exception as e:
        return False, str(e)


# Admin Dashboard
def get_dashboard_data(request):
    try:
        user_id = request.session.get('user_id')
        if not user_id:
            return None, "User not authenticated."

        admin = get_object_or_404(User, pk=user_id, role=Role.ADMIN)
        return {
            "admin": admin,
            "total_admins": User.objects.filter(role=Role.ADMIN).count(),
            "total_staff": User.objects.filter(role=Role.ENDUSER_STAFF).count(),
            "total_customers": User.objects.filter(role=Role.ENDUSER_CUSTOMER).count(),
            "total_products": Product.objects.count(),
            "total_categories": Category.objects.count(),
            "total_reviews": Review.objects.count(),
            "total_shipments": Shipment.objects.count(),
            "total_orders": Order.objects.count(),
            "total_wishlists": Wishlist.objects.count(),
        }, None
    except Exception as e:
        return None, str(e)

