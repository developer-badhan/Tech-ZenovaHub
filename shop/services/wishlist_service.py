from shop.models import Wishlist, Product
from django.core.exceptions import ObjectDoesNotExist

def get_user_wishlist(user):
    try:
        return Wishlist.objects.filter(user=user).select_related('product').order_by('-added_at')
    except Exception as e:
        print(f"Error fetching wishlist: {e}")
        return []

def add_to_wishlist(user, product_id):
    try:
        product = Product.objects.get(id=product_id)

        existing = Wishlist.objects.filter(user=user, product=product).exists()
        if existing:
            print("Product already in wishlist.")
            return None

        return Wishlist.objects.create(user=user, product=product)
    except Product.DoesNotExist:
        print(f"Product with ID {product_id} not found.")
        return None
    except Exception as e:
        print(f"Error adding to wishlist: {e}")
        return None

def remove_from_wishlist(user, product_id):
    try:
        item = Wishlist.objects.get(user=user, product_id=product_id)
        item.delete()
        return True
    except ObjectDoesNotExist:
        print(f"Wishlist item not found.")
        return False
    except Exception as e:
        print(f"Error removing from wishlist: {e}")
        return False

def is_product_in_wishlist(user, product_id):
    try:
        return Wishlist.objects.filter(user=user, product_id=product_id).exists()
    except Exception as e:
        print(f"Error checking wishlist: {e}")
        return False