from shop.models import Cart, CartItem, Product
from django.core.exceptions import ObjectDoesNotExist

def get_cart(user):
    try:
        cart, created = Cart.objects.get_or_create(user=user)
        return cart
    except Exception as e:
        print(f"Error fetching cart: {e}")
        return None

def get_cart_items(user):
    try:
        cart = get_cart(user)
        if not cart:
            return []
        return cart.items.select_related('product').all()
    except Exception as e:
        print(f"Error fetching cart items: {e}")
        return []

def add_item(user, product_id, quantity=1):
    try:
        cart = get_cart(user)
        product = Product.objects.get(id=product_id)

        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += int(quantity)
        else:
            item.quantity = int(quantity)
        item.save()
        return item
    except Product.DoesNotExist:
        print(f"Product with ID {product_id} not found.")
        return None
    except Exception as e:
        print(f"Error adding item to cart: {e}")
        return None

def update_item(user, product_id, quantity):
    try:
        cart = get_cart(user)
        item = CartItem.objects.get(cart=cart, product_id=product_id)
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
    try:
        cart = get_cart(user)
        item = CartItem.objects.get(cart=cart, product_id=product_id)
        item.delete()
        return True
    except ObjectDoesNotExist:
        print(f"Cart item not found for product ID {product_id}.")
        return False
    except Exception as e:
        print(f"Error removing item from cart: {e}")
        return False

def clear_cart(user):
    try:
        cart = get_cart(user)
        cart.items.all().delete()
        return True
    except Exception as e:
        print(f"Error clearing cart: {e}")
        return False