# shop/services/wishlist_service.py
from django.db import transaction, IntegrityError
from shop.models import Wishlist, Product
from constants import Role

def _is_customer(user) -> bool:
    return getattr(user, "is_authenticated", False) and int(getattr(user, "role", 0)) == int(Role.ENDUSER_CUSTOMER)

def get_user_wishlist(user):
    if not _is_customer(user):
        return Wishlist.objects.none()
    return Wishlist.objects.filter(user=user).select_related("product").order_by("-added_at")

def add_to_wishlist(user, product_id):
    if not _is_customer(user):
        return None
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return None

    try:
        with transaction.atomic():
            item, created = Wishlist.objects.get_or_create(user=user, product=product)
            return item if created else None
    except IntegrityError:
        return None

def remove_from_wishlist(user, product_id):
    if not _is_customer(user):
        return False
    deleted, _ = Wishlist.objects.filter(user=user, product_id=product_id).delete()
    return deleted > 0

def is_product_in_wishlist(user, product_id):
    if not _is_customer(user):
        return False
    return Wishlist.objects.filter(user=user, product_id=product_id).exists()
