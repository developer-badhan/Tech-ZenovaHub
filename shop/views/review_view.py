from django.shortcuts import render, redirect
from django.views import View
from decorators import signin_required, customer_required, inject_authenticated_user
from shop.services import review_service

class ProductReviewListView(View):
    @inject_authenticated_user
    def get(self, request, product_id):
        reviews = review_service.get_product_reviews(product_id)
        return render(request, "review/review_list.html", {"reviews": reviews, "product_id": product_id})

class ProductReviewCreateView(View):
    @signin_required
    @customer_required
    @inject_authenticated_user
    def get(self, request, product_id):
        return render(request, "review/review_form.html", {"product_id": product_id})

    @signin_required
    @customer_required
    @inject_authenticated_user
    def post(self, request, product_id):
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        review_service.create_or_update_review(request.user, product_id, rating, comment)
        return redirect("review_list", product_id=product_id)

class ProductReviewUpdateView(View):
    @signin_required
    @customer_required
    @inject_authenticated_user
    def get(self, request, product_id):
        return render(request, "review/review_form.html", {"product_id": product_id})

    @signin_required
    @customer_required
    @inject_authenticated_user
    def post(self, request, product_id):
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        review_service.create_or_update_review(request.user, product_id, rating, comment)
        return redirect("review_list", product_id=product_id)

class ProductReviewDeleteView(View):
    @signin_required
    @customer_required
    @inject_authenticated_user
    def post(self, request, product_id):
        review_service.delete_review(request.user, product_id)
        return redirect("review_list", product_id=product_id)



# shop/views/product_view.py
from django.views import View
from django.shortcuts import render
from django.http import HttpResponseNotFound
from shop.services import product_service, review_service

class ProductDetailView(View):
    def get(self, request, product_id):
        product = product_service.get_product_by_id(product_id)
        if not product:
            return HttpResponseNotFound("Product not found.")
        reviews = review_service.get_product_reviews(product_id)
        user_review = None
        if request.user.is_authenticated:
            user_review = reviews.filter(user=request.user).first()

        context = {
            "product": product,
            "reviews": reviews,
            "user_review": user_review,
        }
        return render(request, "product/product_detail.html", context)
