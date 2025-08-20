from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseNotFound
from shop.services import review_service
from shop.models import Product

# class ProductReviewListView(View):
#     def get(self, request, product_id):
#         reviews = review_service.get_reviews_for_product(product_id)
#         return render(request, 'shop/review_list.html', {
#             'reviews': reviews,
#             'product_id': product_id
#         })

# class ProductReviewCreateView(View):
#     def get(self, request, product_id):
#         try:
#             product = Product.objects.get(id=product_id)
#             return render(request, 'shop/review_create.html', {'product': product})
#         except Product.DoesNotExist:
#             return HttpResponseNotFound("Product not found.")

#     def post(self, request, product_id):
#         rating = request.POST.get('rating')
#         comment = request.POST.get('comment', '')

#         review = review_service.create_review(
#             user=request.user,
#             product_id=product_id,
#             rating=rating,
#             comment=comment
#         )

#         if review:
#             messages.success(request, "Review submitted.")
#         else:
#             messages.error(request, "You already reviewed this product or something went wrong.")
#         return redirect('shop:review_list', product_id=product_id)

# class ProductReviewUpdateView(View):
#     def get(self, request, product_id):
#         review = review_service.get_review_by_user_and_product(request.user, product_id)
#         if review:
#             return render(request, 'shop/review_update.html', {'review': review})
#         return HttpResponseNotFound("Review not found.")

#     def post(self, request, product_id):
#         rating = request.POST.get('rating')
#         comment = request.POST.get('comment', '')

#         updated = review_service.update_review(
#             user=request.user,
#             product_id=product_id,
#             rating=rating,
#             comment=comment
#         )

#         if updated:
#             messages.success(request, "Review updated.")
#         else:
#             messages.error(request, "Failed to update review.")
#         return redirect('shop:review_list', product_id=product_id)

# class ProductReviewDeleteView(View):
#     def post(self, request, product_id):
#         success = review_service.delete_review(user=request.user, product_id=product_id)
#         if success:
#             messages.success(request, "Review deleted.")
#         else:
#             messages.error(request, "Failed to delete review.")
#         return redirect('shop:review_list', product_id=product_id)




class ProductReviewListView(View):
    def get(self, request, product_id):
        try:
            reviews = review_service.get_reviews_for_product(product_id)
            return render(request, 'shop/review_list.html', {
                'reviews': reviews,
                'product_id': product_id
            })
        except Exception as e:
            print(f"[ProductReviewListView] Error: {e}")
            messages.error(request, "Failed to load reviews.")
            return redirect('shop:product_detail', product_id=product_id)

class ProductReviewCreateView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            return render(request, 'shop/review_create.html', {'product': product})
        except Product.DoesNotExist:
            return HttpResponseNotFound("Product not found.")

    def post(self, request, product_id):
        rating = request.POST.get('rating')
        comment = request.POST.get('comment', '')

        try:
            review = review_service.create_review(
                user=request.user,
                product_id=product_id,
                rating=rating,
                comment=comment
            )
            if review:
                messages.success(request, "Review submitted.")
            else:
                messages.error(request, "You already reviewed this product or something went wrong.")
        except Exception as e:
            print(f"[ProductReviewCreateView] Error: {e}")
            messages.error(request, "Error submitting review.")

        return redirect('shop:review_list', product_id=product_id)


class ProductReviewUpdateView(View):
    def get(self, request, product_id):
        review = review_service.get_review_by_user_and_product(request.user, product_id)
        if review:
            return render(request, 'shop/review_update.html', {'review': review})
        return HttpResponseNotFound("Review not found.")

    def post(self, request, product_id):
        rating = request.POST.get('rating')
        comment = request.POST.get('comment', '')

        try:
            updated = review_service.update_review(
                user=request.user,
                product_id=product_id,
                rating=rating,
                comment=comment
            )
            if updated:
                messages.success(request, "Review updated.")
            else:
                messages.error(request, "Failed to update review.")
        except Exception as e:
            print(f"[ProductReviewUpdateView] Error: {e}")
            messages.error(request, "An error occurred while updating the review.")

        return redirect('shop:review_list', product_id=product_id)

class ProductReviewDeleteView(View):
    def post(self, request, product_id):
        try:
            success = review_service.delete_review(user=request.user, product_id=product_id)
            if success:
                messages.success(request, "Review deleted.")
            else:
                messages.error(request, "Failed to delete review.")
        except Exception as e:
            print(f"[ProductReviewDeleteView] Error: {e}")
            messages.error(request, "Error occurred while deleting review.")
        return redirect('shop:review_list', product_id=product_id)

