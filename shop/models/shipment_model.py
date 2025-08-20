from django.db import models
from .order_model import Order

class Shipment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='shipment')
    address = models.TextField()
    shipped_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    tracking_number = models.CharField(max_length=100, blank=True, null=True)
    carrier = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50, default='processing')

    def __str__(self):
        return f"Shipment for Order #{self.order.id} via {self.carrier} (Tracking: {self.tracking_number})"