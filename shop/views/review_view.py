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
