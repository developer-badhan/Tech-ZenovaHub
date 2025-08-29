from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseNotFound
from shop.services import order_service

# class OrderListView(View):
#     def get(self, request):
#         try:
#             orders = order_service.get_all_orders(user=request.user)
#             return render(request, 'shop/order_list.html', {'orders': orders})
#         except Exception as e:
#             print(f"Error loading orders: {e}")
#             return HttpResponseServerError("Something went wrong.")

# class OrderDetailView(View):
#     def get(self, request, order_id):
#         order = order_service.get_order_by_id(order_id)
#         if order:
#             return render(request, 'shop/order_detail.html', {'order': order})
#         return HttpResponseNotFound("Order not found.")

# class OrderCreateView(View):
#     def get(self, request):
#         return render(request, 'shop/order_create.html')  # Show form/cart summary

#     def post(self, request):
#         try:
#             items = []
#             count = int(request.POST.get('item_count', 0))

#             for i in range(1, count + 1):
#                 product_id = request.POST.get(f'product_id_{i}')
#                 quantity = request.POST.get(f'quantity_{i}')
#                 if product_id and quantity:
#                     items.append({
#                         'product_id': product_id,
#                         'quantity': int(quantity)
#                     })

#             coupon_code = request.POST.get('coupon_code')

#             order = order_service.create_order(user=request.user, items=items, coupon_code=coupon_code)

#             if order:
#                 messages.success(request, "Order placed successfully.")
#                 return redirect('shop:order_detail', order_id=order.id)
#             else:
#                 messages.error(request, "Failed to place order.")
#                 return redirect('shop:order_create')
#         except Exception as e:
#             print(f"Order creation failed: {e}")
#             messages.error(request, "Something went wrong.")
#             return redirect('shop:order_create')

# class OrderDeleteView(View):
#     def post(self, request, order_id):
#         success = order_service.delete_order(order_id)
#         if success:
#             messages.success(request, "Order deleted.")
#         else:
#             messages.error(request, "Failed to delete order.")
#         return redirect('shop:order_list')


class OrderListView(View):
    def get(self, request):
        try:
            orders = order_service.get_all_orders(user=request.user)
            return render(request, 'order/order_list.html', {'orders': orders})
        except Exception as e:
            print(f"[OrderListView] Error: {e}")
            messages.error(request, "Failed to load orders.")
            return render(request, 'order/order_list.html', {'orders': []})

class OrderDetailView(View):
    def get(self, request, order_id):
        order = order_service.get_order_by_id(order_id)
        if order:
            return render(request, 'order/order_detail.html', {'order': order})
        return HttpResponseNotFound("Order not found.")

class OrderCreateView(View):
    def get(self, request):
        return render(request, 'order/order_create.html')

    def post(self, request):
        try:
            items = []
            count = int(request.POST.get('item_count', 0))

            for i in range(1, count + 1):
                product_id = request.POST.get(f'product_id_{i}')
                quantity = request.POST.get(f'quantity_{i}')
                if product_id and quantity:
                    items.append({
                        'product_id': product_id,
                        'quantity': int(quantity)
                    })

            coupon_code = request.POST.get('coupon_code')

            order = order_service.create_order(user=request.user, items=items, coupon_code=coupon_code)

            if order:
                messages.success(request, "Order placed successfully.")
                return redirect('order_detail', order_id=order.id)

        except Exception as e:
            print(f"[OrderCreateView] Error: {e}")
            messages.error(request, "Failed to place order.")

        return redirect('order_create')

class OrderDeleteView(View):
    def post(self, request, order_id):
        try:
            success = order_service.delete_order(order_id)
            if success:
                messages.success(request, "Order deleted.")
            else:
                messages.error(request, "Failed to delete order.")
        except Exception as e:
            print(f"[OrderDeleteView] Error: {e}")
            messages.error(request, "An error occurred while deleting the order.")
        return redirect('order_list')



