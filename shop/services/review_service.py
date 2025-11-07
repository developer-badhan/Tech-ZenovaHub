from django.db import transaction
from shop.models import Review, Product
from constants import Role


# Check if user is a customer
def _is_customer(user) -> bool:
    return getattr(user, "is_authenticated", False) and int(getattr(user, "role", 0)) == int(Role.ENDUSER_CUSTOMER)


# Get all reviews for a product
def get_product_reviews(product_id):
    return Review.objects.filter(product_id=product_id).select_related("user").order_by("-created_at")


# Create or update a review
def create_or_update_review(user, product_id, rating, comment):
    if not _is_customer(user):
        return None
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return None
    with transaction.atomic():
        review, created = Review.objects.update_or_create(
            user=user,
            product=product,
            defaults={"rating": rating, "comment": comment}
        )
        return review


# Delete existing review
def delete_review(user, product_id):
    print(f"🧩 delete_review() called for user={user.id}, product={product_id}")
    try:
        review = Review.objects.get(user=user, product_id=product_id)
        review.delete()
        return True
    except Review.DoesNotExist:
        print("Product review deleting fail")
        return False
    except Exception as e:
        return False

