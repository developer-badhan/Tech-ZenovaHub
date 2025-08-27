from shop.models import Cart, CartItem, Product
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

def is_valid_user(user):
    return user and hasattr(user, 'id') and isinstance(user.id, int)

def is_valid_id(value):
    try:
        return int(value) > 0
    except (TypeError, ValueError):
        return False

def is_valid_quantity(value):
    try:
        return int(value) > 0
    except (TypeError, ValueError):
        return False

def get_cart(user):
    if not is_valid_user(user):
        print("Invalid user object.")
        return None
    try:
        cart, _ = Cart.objects.get_or_create(user=user)
        return cart
    except Exception as e:
        print(f"Error fetching cart: {e}")
        return None

def get_cart_items(user):
    cart = get_cart(user)
    if not cart:
        return []
    try:
        return cart.items.select_related('product').all()
    except Exception as e:
        print(f"Error fetching cart items: {e}")
        return []

# def add_item(user, product_id, quantity=1):
#     if not is_valid_user(user) or not is_valid_id(product_id) or not is_valid_quantity(quantity):
#         print("Invalid input for adding item.")
#         return None
#     try:
#         cart = get_cart(user)
#         product = Product.objects.get(id=int(product_id))

#         item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#         item.quantity = item.quantity + int(quantity) if not created else int(quantity)
#         item.save()
#         return item
#     except Product.DoesNotExist:
#         print(f"Product with ID {product_id} not found.")
#         return None
#     except Exception as e:
#         print(f"Error adding item to cart: {e}")
#         return None


def add_item(user, product_id, quantity=1):
    print("=== [DEBUG] add_item called ===")
    print(f"[DEBUG] user: {user}")
    print(f"[DEBUG] product_id: {product_id} (type: {type(product_id)})")
    print(f"[DEBUG] quantity: {quantity} (type: {type(quantity)})")

    # Check validations
    is_user_valid = is_valid_user(user)
    is_product_id_valid = is_valid_id(product_id)
    is_quantity_valid = is_valid_quantity(quantity)

    print(f"[DEBUG] is_valid_user: {is_user_valid}")
    print(f"[DEBUG] is_valid_id: {is_product_id_valid}")
    print(f"[DEBUG] is_valid_quantity: {is_quantity_valid}")

    if not is_user_valid or not is_product_id_valid or not is_quantity_valid:
        print("❌ Invalid input for adding item.")
        return None

    try:
        # Fetch or create cart
        cart = get_cart(user)
        print(f"[DEBUG] Retrieved cart: {cart}")

        # Get product
        product = Product.objects.get(id=int(product_id))
        print(f"[DEBUG] Retrieved product: {product}")

        # Add or update cart item
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        print(f"[DEBUG] CartItem {'created' if created else 'found'}: {item}")

        item.quantity = item.quantity + int(quantity) if not created else int(quantity)
        item.save()

        print(f"[DEBUG] Saved item: {item} (new quantity: {item.quantity})")
        return item

    except Product.DoesNotExist:
        print(f"❌ Product with ID {product_id} not found.")
        return None

    except Exception as e:
        print(f"❌ Error adding item to cart: {e}")
        return None


def update_item(user, product_id, quantity):
    if not is_valid_user(user) or not is_valid_id(product_id) or not is_valid_quantity(quantity):
        print("Invalid input for updating item.")
        return None

    try:
        cart = get_cart(user)
        item = CartItem.objects.get(cart=cart, product_id=int(product_id))
        item.quantity = int(quantity)
        item.save()
        return item
    except ObjectDoesNotExist:
        print(f"Cart item not found for product ID {product_id}.")
        return None
    except Exception as e:
        print(f"Error updating cart item: {e}")
        return None

def remove_item(user, product_id):
    if not is_valid_user(user) or not is_valid_id(product_id):
        print("Invalid input for removing item.")
        return False

    try:
        cart = get_cart(user)
        item = CartItem.objects.get(cart=cart, product_id=int(product_id))
        item.delete()
        return True
    except ObjectDoesNotExist:
        print(f"Cart item not found for product ID {product_id}.")
        return False
    except Exception as e:
        print(f"Error removing item from cart: {e}")
        return False

def clear_cart(user):
    if not is_valid_user(user):
        print("Invalid user for clearing cart.")
        return False

    try:
        cart = get_cart(user)
        cart.items.all().delete()
        return True
    except Exception as e:
        print(f"Error clearing cart: {e}")
        return False
