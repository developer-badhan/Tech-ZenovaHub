from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from user.utils.auth_status import get_user_login_status
from shop.services import review_service
from constants.enums import Role



# Product Review List
class ProductReviewListView(View):
    def get(self, request, product_id):
        reviews = review_service.get_product_reviews(product_id)
        is_logged_in, active_user, user_role = get_user_login_status(request)
        user_review = None
        if is_logged_in and active_user:
            user_review = reviews.filter(user=active_user).first()
        return render(request, "review/review_list.html", {
            "reviews": reviews,
            "product_id": product_id,
            "is_logged_in": is_logged_in,
            "active_user": active_user,
            "user_role": user_role,
            "user_review": user_review
        })


# Product Review Create 
class ProductReviewCreateView(View):
    def get(self, request, product_id):
        is_logged_in, active_user, user_role = get_user_login_status(request)
        if not is_logged_in:
            return redirect(f"{'/user/signin/'}?next={request.path}")
        if int(user_role or 0) != int(Role.ENDUSER_CUSTOMER):
            messages.error(request, "Only customers can post reviews.")
            return redirect("product_detail", product_id=product_id)
        return render(request, "review/review_form.html", {
            "product_id": product_id,
            "user_review": review_service.get_product_reviews(product_id).filter(user=active_user).first(),
        })

    def post(self, request, product_id):
        is_logged_in, active_user, user_role = get_user_login_status(request)
        if not is_logged_in:
            return redirect(f"{'/user/signin/'}?next={request.path}")
        if int(user_role or 0) != int(Role.ENDUSER_CUSTOMER):
            messages.error(request, "Only customers can post reviews.")
            return redirect("product_detail", product_id=product_id)
        rating = request.POST.get("rating")
        comment = request.POST.get("comment", "").strip()
        try:
            rating_int = int(rating)
            if rating_int < 1 or rating_int > 5:
                raise ValueError
        except Exception:
            messages.error(request, "Please provide a valid rating between 1 and 5.")
            return redirect("product_detail", product_id=product_id)
        review = review_service.create_or_update_review(active_user, product_id, rating_int, comment)
        if review:
            messages.success(request, "Your review has been submitted.")
        else:
            messages.error(request, "Failed to save your review.")
        return redirect("product_detail", product_id=product_id)


# Product Review Update View
class ProductReviewUpdateView(View):
    def get(self, request, product_id):
        is_logged_in, active_user, user_role = get_user_login_status(request)
        if not is_logged_in:
            return redirect(f"{'/user/signin/'}?next={request.path}")
        if int(user_role or 0) != int(Role.ENDUSER_CUSTOMER):
            messages.error(request, "Only customers can update reviews.")
            return redirect("product_detail", product_id=product_id)
        user_review = review_service.get_product_reviews(product_id).filter(user=active_user).first()
        if not user_review:
            messages.error(request, "No review found to edit.")
            return redirect("product_detail", product_id=product_id)
        return render(request, "review/review_form.html", {
            "product_id": product_id,
            "user_review": user_review,
        })

    def post(self, request, product_id):
        is_logged_in, active_user, user_role = get_user_login_status(request)
        if not is_logged_in:
            return redirect(f"{'/user/signin/'}?next={request.path}")
        if int(user_role or 0) != int(Role.ENDUSER_CUSTOMER):
            messages.error(request, "Only customers can update reviews.")
            return redirect("product_detail", product_id=product_id)
        rating = request.POST.get("rating")
        comment = request.POST.get("comment", "").strip()
        try:
            rating_int = int(rating)
            if rating_int < 1 or rating_int > 5:
                raise ValueError
        except Exception:
            messages.error(request, "Please provide a valid rating between 1 and 5.")
            return redirect("product_detail", product_id=product_id)
        review = review_service.create_or_update_review(active_user, product_id, rating_int, comment)
        if review:
            messages.success(request, "Your review has been updated.")
        else:
            messages.error(request, "Failed to update your review.")
        return redirect("product_detail", product_id=product_id)


# Product Review Delete View
class ProductReviewDeleteView(View):
    def post(self, request, product_id):
        is_logged_in, active_user, user_role = get_user_login_status(request)
        if not is_logged_in:
            return redirect(f"/user/signin/?next={request.path}")
        if int(user_role or 0) != int(Role.ENDUSER_CUSTOMER):
            messages.error(request, "Only customers can delete reviews.")
            return redirect("product_detail", product_id=product_id)
        ok = review_service.delete_review(active_user, product_id)
        if ok:
            messages.success(request, "Your review has been deleted.")
        else:
            messages.error(request, "No review found to delete.")
        return redirect("product_detail", product_id=product_id)

