from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseServerError
from shop.services import cart_service
from decorators import signin_required,customer_required,inject_authenticated_user
from shop.models import Product


# Cart Detail View
class CartDetailView(View):
    @signin_required
    @customer_required
    @inject_authenticated_user
    def get(self, request):
        try:
            items = cart_service.get_cart_items(request.user)
            total_price = sum(item.product.price * item.quantity for item in items)
            return render(request, 'cart/cart_detail.html', {
                'items': items,
                'total_price': total_price
            })
        except Exception as e:
            print(f"Error displaying cart: {e}")
            return HttpResponseServerError("Something went wrong.")


# Add Item to Cart
class CartAddItemView(View):
    @signin_required
    @customer_required
    @inject_authenticated_user
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'cart/cart_additem.html', {'products': products})

    @signin_required
    @customer_required
    @inject_authenticated_user
    def post(self, request):
        product_id = request.POST.get('product_id')
        quantity_raw = request.POST.get('quantity')

        # Safely convert quantity to an integer, fallback to 1
        try:
            quantity = int(quantity_raw)
            if quantity <= 0:
                quantity = 1
        except (TypeError, ValueError):
            quantity = 1

        try:
            item = cart_service.add_item(request.user, product_id, quantity)
            if item:
                messages.success(request, "Item added to cart.")
            else:
                messages.error(request, "Failed to add item to cart.")
        except Exception as e:
            messages.error(request, "Unexpected error occurred while adding item.")
            print(e)

        return redirect('cart_detail')



# Update Item in Cart
class CartUpdateItemView(View):
    @signin_required
    @customer_required
    @inject_authenticated_user
    def get(self, request):
        return render(request, 'cart/cart_updateitem.html')

    @signin_required
    @customer_required
    @inject_authenticated_user
    def post(self, request):
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        try:
            item = cart_service.update_item(request.user, product_id, quantity)
            if item:
                messages.success(request, "Cart updated.")
            else:
                messages.error(request, "Failed to update cart.")
        except Exception as e:
            messages.error(request, "Unexpected error occurred while updating item.")
            print(e)

        return redirect('cart_detail')


# Remove Item from Cart
class CartRemoveItemView(View):
    @signin_required
    @customer_required
    @inject_authenticated_user
    def get(self, request):
        return render(request, 'cart/cart_removeitem.html')

    @signin_required
    @customer_required
    @inject_authenticated_user
    def post(self, request):
        product_id = request.POST.get('product_id')

        try:
            success = cart_service.remove_item(request.user, product_id)
            if success:
                messages.success(request, "Item removed from cart.")
            else:
                messages.error(request, "Failed to remove item.")
        except Exception as e:
            messages.error(request, "Unexpected error occurred while removing item.")
            print(e)

        return redirect('cart_detail')


# Clear Cart
class CartClearView(View):
    @signin_required
    @customer_required
    @inject_authenticated_user
    def get(self, request):
        return render(request, 'cart/cart_clear.html')

    @signin_required
    @customer_required
    @inject_authenticated_user
    def post(self, request):
        try:
            success = cart_service.clear_cart(request.user)
            if success:
                messages.success(request, "Cart cleared.")
            else:
                messages.error(request, "Failed to clear cart.")
        except Exception as e:
            messages.error(request, "Unexpected error occurred while clearing cart.")
            print(e)

        return redirect('cart_detail')
