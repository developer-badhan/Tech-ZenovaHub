from django.db import models
from django.utils import timezone
from datetime import timedelta
from user.models import User

class EmailOTP(models.Model):
    user = models.OneToOneField(User,related_name='otps', on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=10)

    def __str__(self):
        return f"OTP for {self.user.email} - Verified: {self.is_verified}"
