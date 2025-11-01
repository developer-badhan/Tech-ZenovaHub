from django.db import transaction, IntegrityError
from shop.models import Wishlist, Product
from constants import Role
from shop.services import cart_service

# Check if user is a customer
def _is_customer(user) -> bool:
    return getattr(user, "is_authenticated", False) and int(getattr(user, "role", 0)) == int(Role.ENDUSER_CUSTOMER)


# Get the user's wishlist
def get_user_wishlist(user):
    if not _is_customer(user):
        return Wishlist.objects.none()
    return Wishlist.objects.filter(user=user).select_related("product").order_by("-added_at")


# Add a product to the wishlist
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


# Remove a product from the wishlist
def remove_from_wishlist(user, product_id):
    if not _is_customer(user):
        return False
    deleted, _ = Wishlist.objects.filter(user=user, product_id=product_id).delete()
    return deleted > 0


# Check if a product is in the wishlist
def is_product_in_wishlist(user, product_id):
    if not _is_customer(user):
        return False
    return Wishlist.objects.filter(user=user, product_id=product_id).exists()


# Get the specific product
def get_product(product_id):
    try:
        return Product.objects.filter(pk=product_id).first()
    except Product.DoesNotExist:
        print("Product was not found")


# Move item from Wishlist to Cart
def move_to_cart(user, product_id):
    if not _is_customer(user):
        return False
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        print(f"move_to_cart: Product {product_id} does not exist.")
        return False
    try:
        with transaction.atomic():
            item = cart_service.add_item(user, product_id, quantity=1)
            if not item:
                print(f"move_to_cart: Failed to add product {product_id} to cart.")
                return False
            remove_from_wishlist(user, product_id)
            print(f"move_to_cart: Moved product {product_id} from wishlist to cart.")
            return True
    except Exception as e:
        print(f"move_to_cart: Error moving product to cart: {e}")
        return False
