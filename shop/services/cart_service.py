from shop.models import Cart, CartItem, Product
from django.core.exceptions import ObjectDoesNotExist


# User Validation
def is_valid_user(user):
    return user and hasattr(user, 'id') and isinstance(user.id, int)


# User ID Validation
def is_valid_id(value):
    try:
        return int(value) > 0
    except (TypeError, ValueError):
        return False


# Quantity Validation
def is_valid_quantity(value):
    try:
        return int(value) > 0
    except (TypeError, ValueError):
        return False


# Get Cart
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


# Get Cart Items
def get_cart_items(user):
    cart = get_cart(user)
    if not cart:
        return []
    try:
        return cart.items.select_related('product').all()
    except Exception as e:
        print(f"Error fetching cart items: {e}")
        return []


# Add Item to Cart
def add_item(user, product_id, quantity=1):
    if not is_valid_user(user) or not is_valid_id(product_id) or not is_valid_quantity(quantity):
        print("Invalid input for adding item.")
        return None
    try:
        cart = get_cart(user)
        product = Product.objects.get(id=int(product_id))

        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        item.quantity = item.quantity + int(quantity) if not created else int(quantity)
        item.save()
        return item
    except ObjectDoesNotExist:
        print(f"Product with ID {product_id} not found.")
        return None
    except Exception as e:
        print(f"Error adding item to cart: {e}")
        return None


# SKU Validation
def is_valid_sku(sku):
    """
    Returns True for a non-empty string SKU. Strips whitespace.
    """
    if not sku:
        return False
    if not isinstance(sku, str):
        return False
    return bool(sku.strip())


# Update  Item to the Cart 
def update_item(user, product_sku, quantity, expected_sku=None):
    if not is_valid_user(user) or not is_valid_sku(product_sku) or not is_valid_quantity(quantity):
        print("Invalid input for updating item.")
        return None
    if expected_sku:
        if not is_valid_sku(expected_sku):
            print("Invalid expected_sku provided.")
            return None
        if product_sku.strip().lower() != expected_sku.strip().lower():
            print("SKU mismatch between expected and provided SKU.")
            return None
    sku = product_sku.strip()
    try:
        cart = get_cart(user)
        if not cart:
            print("Could not fetch cart for user.")
            return None
        try:
            product = Product.objects.get(sku=sku, is_active=True)
        except Product.DoesNotExist:
            print(f"Product not found for SKU: {sku}")
            return None
        try:
            item = CartItem.objects.get(cart=cart, product=product)
        except CartItem.DoesNotExist:
            print(f"Cart item not found for product SKU: {sku}")
            return None
        item.quantity = int(quantity)
        item.save()
        return item
    except Exception as e:
        print(f"Error updating cart item: {e}")
        return None


# Remove Item from the Cart
def remove_item(user, product_sku, expected_sku=None):
    if not is_valid_user(user) or not is_valid_sku(product_sku):
        print("Invalid input for removing item.")
        return False
    if expected_sku:
        if not is_valid_sku(expected_sku):
            print("Invalid expected_sku provided.")
            return False
        if product_sku.strip().lower() != expected_sku.strip().lower():
            print("SKU mismatch between expected and provided SKU.")
            return False
    sku = product_sku.strip()
    try:
        cart = get_cart(user)
        if not cart:
            print("Could not fetch cart for user.")
            return False
        try:
            product = Product.objects.get(sku=sku, is_active=True)
        except Product.DoesNotExist:
            print(f"Product not found for SKU: {sku}")
            return False
        try:
            item = CartItem.objects.get(cart=cart, product=product)
        except CartItem.DoesNotExist:
            print(f"Cart item not found for product SKU: {sku}")
            return False
        item.delete()
        return True
    except Exception as e:
        print(f"Error removing item from cart: {e}")
        return False


# Clear Cart
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


