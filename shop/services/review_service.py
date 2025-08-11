from shop.models import Review, Product
from django.core.exceptions import ObjectDoesNotExist

def get_reviews_for_product(product_id):
    try:
        return Review.objects.filter(product_id=product_id).select_related('user').order_by('-created_at')
    except Exception as e:
        print(f"Error fetching reviews for product {product_id}: {e}")
        return []

def get_review_by_user_and_product(user, product_id):
    try:
        return Review.objects.get(user=user, product_id=product_id)
    except Review.DoesNotExist:
        return None
    except Exception as e:
        print(f"Error checking existing review: {e}")
        return None

def create_review(user, product_id, rating, comment=''):
    try:
        product = Product.objects.get(id=product_id)

        existing_review = get_review_by_user_and_product(user, product_id)
        if existing_review:
            print("User has already reviewed this product.")
            return None

        return Review.objects.create(
            user=user,
            product=product,
            rating=int(rating),
            comment=comment
        )
    except Product.DoesNotExist:
        print(f"Product with ID {product_id} not found.")
        return None
    except Exception as e:
        print(f"Error creating review: {e}")
        return None

def update_review(user, product_id, rating=None, comment=None):
    try:
        review = Review.objects.get(user=user, product_id=product_id)
        if rating:
            review.rating = int(rating)
        if comment is not None:
            review.comment = comment
        review.save()
        return review
    except Review.DoesNotExist:
        print(f"Review not found for user and product.")
        return None
    except Exception as e:
        print(f"Error updating review: {e}")
        return None

def delete_review(user, product_id):
    try:
        review = Review.objects.get(user=user, product_id=product_id)
        review.delete()
        return True
    except Review.DoesNotExist:
        print(f"Review not found.")
        return False
    except Exception as e:
        print(f"Error deleting review: {e}")
        return False