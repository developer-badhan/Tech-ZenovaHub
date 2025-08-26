# shop/views/wishlist_views.py
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from mixins.auth_mixins import CustomerRequiredMixin
from shop.services import wishlist_service
from shop.models import Product

class WishlistListView(CustomerRequiredMixin, View):
    def get(self, request):
        wishlist = wishlist_service.get_user_wishlist(request.user)
        if not wishlist.exists():
            messages.info(request, "Your wishlist is empty.")
        return render(request, "wishlist/wishlist.html", {"wishlist": wishlist})


class WishlistAddView(CustomerRequiredMixin, View):
    def post(self, request, product_id):
        item = wishlist_service.add_to_wishlist(request.user, product_id)
        if item:
            messages.success(request, f"'{item.product.name}' added to wishlist.")
        else:
            messages.warning(request, "Product already in wishlist or could not be added.")
        return redirect("product_detail", product_id=product_id)


class WishlistRemoveView(CustomerRequiredMixin, View):
    def post(self, request, product_id):
        ok = wishlist_service.remove_from_wishlist(request.user, product_id)
        if ok:
            messages.success(request, "Product removed from wishlist.")
        else:
            messages.error(request, "Product not found in your wishlist.")
        return redirect("wishlist")
