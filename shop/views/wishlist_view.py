from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from shop.services import wishlist_service
from shop.models import Product

# class WishlistListView(View):
#     def get(self, request):
#         wishlist = wishlist_service.get_user_wishlist(request.user)
#         return render(request, 'shop/wishlist.html', {'wishlist': wishlist})

# class WishlistAddView(View):
#     def post(self, request, product_id):
#         item = wishlist_service.add_to_wishlist(request.user, product_id)
#         if item:
#             messages.success(request, "Product added to wishlist.")
#         else:
#             messages.warning(request, "Product is already in wishlist or couldn't be added.")
#         return redirect('shop:product_detail', product_id=product_id)

# class WishlistRemoveView(View):
#     def post(self, request, product_id):
#         success = wishlist_service.remove_from_wishlist(request.user, product_id)
#         if success:
#             messages.success(request, "Product removed from wishlist.")
#         else:
#             messages.error(request, "Failed to remove product from wishlist.")
#         return redirect('shop:wishlist')


class WishlistListView(View):
    def get(self, request):
        try:
            wishlist = wishlist_service.get_user_wishlist(request.user)
            return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist})
        except Exception as e:
            print(f"[WishlistListView] Error: {e}")
            messages.error(request, "Failed to load wishlist.")
            return redirect('product_list')


class WishlistAddView(View):
    def post(self, request, product_id):
        try:
            item = wishlist_service.add_to_wishlist(request.user, product_id)
            if item:
                messages.success(request, "Product added to wishlist.")
            else:
                messages.warning(request, "Product is already in wishlist or couldn't be added.")
        except Exception as e:
            print(f"[WishlistAddView] Error: {e}")
            messages.error(request, "Error adding product to wishlist.")
        return redirect('product_detail', product_id=product_id)


class WishlistRemoveView(View):
    def post(self, request, product_id):
        try:
            success = wishlist_service.remove_from_wishlist(request.user, product_id)
            if success:
                messages.success(request, "Product removed from wishlist.")
            else:
                messages.error(request, "Failed to remove product from wishlist.")
        except Exception as e:
            print(f"[WishlistRemoveView] Error: {e}")
            messages.error(request, "Error removing product from wishlist.")
        return redirect('wishlist')
