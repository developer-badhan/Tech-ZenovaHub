from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseNotFound, HttpResponseServerError
from shop.services import order_service
from shop.models import Order

class OrderItemListView(View):
    def get(self, request, order_id):
        try:
            items = order_service.get_items_by_order(order_id)
            order = Order.objects.get(id=order_id)
            return render(request, 'shop/order_item_list.html', {'items': items, 'order': order})
        except Exception as e:
            print(f"Error displaying order items: {e}")
            return HttpResponseServerError("Something went wrong.")

class OrderItemCreateView(View):
    def get(self, request, order_id):
        return render(request, 'shop/order_item_create.html', {'order_id': order_id})

    def post(self, request, order_id):
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        item = order_service.create_order_item(
            order=Order.objects.get(id=order_id),
            product_id=product_id,
            quantity=int(quantity),
            price=float(price) if price else None
        )

        if item:
            messages.success(request, "Order item added.")
            return redirect('shop:order_item_list', order_id=order_id)
        messages.error(request, "Failed to add order item.")
        return redirect('shop:order_item_create', order_id=order_id)

class OrderItemUpdateView(View):
    def get(self, request, item_id):
        item = order_service.get_item_by_id(item_id)
        if item:
            return render(request, 'shop/order_item_update.html', {'item': item})
        return HttpResponseNotFound("Order item not found.")

    def post(self, request, item_id):
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')

        item = order_service.update_order_item(
            item_id=item_id,
            quantity=int(quantity) if quantity else None,
            price=float(price) if price else None
        )

        if item:
            messages.success(request, "Order item updated.")
            return redirect('shop:order_item_list', order_id=item.order.id)
        messages.error(request, "Failed to update order item.")
        return redirect('shop:order_item_update', item_id=item_id)

class OrderItemDeleteView(View):
    def post(self, request, item_id):
        item = order_service.get_item_by_id(item_id)
        if not item:
            messages.error(request, "Order item not found.")
            return redirect('shop:order_list')

        order_id = item.order.id
        success = order_service.delete_order_item(item_id)
        if success:
            messages.success(request, "Order item deleted.")
        else:
            messages.error(request, "Failed to delete order item.")
        return redirect('shop:order_item_list', order_id=order_id)
