from django.shortcuts import render, redirect
from django.views import View
from decorators import signin_required, customer_required, inject_authenticated_user
from shop.services import wishlist_service 



# Wishlist List View
class WishlistListView(View):
    @signin_required
    @customer_required
    @inject_authenticated_user
    def get(self, request):
        wishlist_items = wishlist_service.get_user_wishlist(request.user)
        return render(request, "wishlist/wishlist.html", {"wishlist": wishlist_items})


# Wishlist Add View
class WishlistAddView(View):
    @signin_required
    @customer_required
    @inject_authenticated_user
    def get(self, request, product_id):
        return render(request, "wishlist/wishlist_add.html", {"product_id": product_id})
    
    @signin_required
    @customer_required
    @inject_authenticated_user
    def post(self, request, product_id):
        item = wishlist_service.add_to_wishlist(request.user, product_id)
        if item:
            return redirect("wishlist")
        return redirect("wishlist")

        
# Wishlist Remove View
class WishlistRemoveView(View):
    @signin_required
    @customer_required
    @inject_authenticated_user
    def get(self, request, product_id):
        return render(request, "wishlist/wishlist_remove.html", {"product_id": product_id})

    @signin_required
    @customer_required
    @inject_authenticated_user
    def post(self, request, product_id):
        success = wishlist_service.remove_from_wishlist(request.user, product_id)
        return redirect("wishlist")


