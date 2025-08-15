from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseNotFound
from shop.services import shipment_service
from shop.models import Order

class ShipmentDetailView(View):
    def get(self, request, order_id):
        shipment = shipment_service.get_shipment_by_order(order_id)
        if shipment:
            return render(request, 'shop/shipment_detail.html', {'shipment': shipment})
        return HttpResponseNotFound("Shipment not found.")

class ShipmentCreateView(View):
    def get(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
            return render(request, 'shop/shipment_create.html', {'order': order})
        except Order.DoesNotExist:
            return HttpResponseNotFound("Order not found.")

    def post(self, request, order_id):
        address = request.POST.get('address')
        tracking_number = request.POST.get('tracking_number', '')
        carrier = request.POST.get('carrier', '')

        shipment = shipment_service.create_shipment(
            order_id=order_id,
            address=address,
            tracking_number=tracking_number,
            carrier=carrier
        )

        if shipment:
            messages.success(request, "Shipment created successfully.")
        else:
            messages.error(request, "Failed to create shipment.")
        return redirect('shop:shipment_detail', order_id=order_id)

class ShipmentUpdateTrackingView(View):
    def post(self, request, order_id):
        tracking_number = request.POST.get('tracking_number')
        carrier = request.POST.get('carrier')

        shipment = shipment_service.update_tracking(order_id, tracking_number, carrier)
        if shipment:
            messages.success(request, "Tracking updated.")
        else:
            messages.error(request, "Failed to update tracking.")
        return redirect('shop:shipment_detail', order_id=order_id)

class ShipmentMarkShippedView(View):
    def post(self, request, order_id):
        shipment = shipment_service.mark_as_shipped(order_id)
        if shipment:
            messages.success(request, "Shipment marked as shipped.")
        else:
            messages.error(request, "Failed to mark as shipped.")
        return redirect('shop:shipment_detail', order_id=order_id)

class ShipmentMarkDeliveredView(View):
    def post(self, request, order_id):
        shipment = shipment_service.mark_as_delivered(order_id)
        if shipment:
            messages.success(request, "Shipment marked as delivered.")
        else:
            messages.error(request, "Failed to mark as delivered.")
        return redirect('shop:shipment_detail', order_id=order_id)
