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


# Delete a review
def delete_review(user, product_id):
    if not _is_customer(user):
        return False
    deleted, _ = Review.objects.filter(user=user, product_id=product_id).delete()
    return deleted > 0
