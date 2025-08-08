from django.contrib.auth.models import AbstractUser
from django.db import models
from constants import Gender, Role

class User(AbstractUser):
    username = models.CharField(max_length=128, blank=True, null=True)  
    password = models.CharField(max_length=128)  
    first_name = models.CharField(max_length=50, blank=False, null=False)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    dob = models.DateField(blank=False, null=False)
    email = models.EmailField(null=False, unique=True, blank=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    gender = models.IntegerField(choices=Gender.choices(), blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_pictures/', max_length=200, null=True, blank=True)
    role = models.IntegerField(choices=Role.choices(), blank=False, null=False, db_default=Role.ENDUSER_CUSTOMER)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(db_default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    fcm_token = models.CharField(max_length=512, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        db_table = 'users'

    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}"
        return f"ID: {self.id}, Name: {full_name}, Created at: {self.created_at}, Active: {self.is_active}"

