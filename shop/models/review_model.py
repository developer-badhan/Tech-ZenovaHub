from django.db import models
from django.conf import settings
from .product_model import Product

class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)] 

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  

    def __str__(self):
        return f"{self.rating}★ by {self.user} for {self.product}"
    

