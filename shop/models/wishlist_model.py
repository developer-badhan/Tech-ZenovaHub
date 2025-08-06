from django.db import models
from django.conf import settings
from .product_model import Product

class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='wishlists')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='wishlisted_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_togrther = ('user','product')

    def __str__(self):
        return f"{self.user} wishlisted {self.product}"
    