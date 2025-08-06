from django.db import models

class Coupon(models.Model):
    code = models.CharField(max_length=20,unique=True)
    discount_percent = models.DecimalField(max_digits=5,decimal_places=2)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    def __str__(self):
        return f"{self.code} ({self.discount_percent}% off)"