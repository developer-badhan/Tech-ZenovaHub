from django.core.mail import send_mail
from django.conf import settings

def send_welcome_email(user):
    subject = "Welcome to Tech-ZenovaHub 🎉"

    if user.role == 1:  # Customer
        message = f"""
Hello {user.first_name},

Welcome to Tech-ZenovaHub! 🚀  
Your customer account has been successfully created.

You can now start exploring products, managing your cart, and placing orders.

Thanks for joining us!  
— Tech-ZenovaHub Team
"""
    elif user.role == 2:  # Staff
        message = f"""
Hello {user.first_name},

Welcome aboard as our Delivery Staff at Tech-ZenovaHub! 🚚  
You can now manage deliveries, update statuses, and view assigned tasks.

We’re excited to have you with us.  
— Tech-ZenovaHub Team
"""
    elif user.role == 3:  # Admin
        message = f"""
Hello {user.first_name},

Your Admin account has been created on Tech-ZenovaHub ⚡  
You now have access to manage users, products, and orders.

Thank you for helping us grow!  
— Tech-ZenovaHub Team
"""
    else:
        message = f"""
Hello {user.first_name},

Welcome to Tech-ZenovaHub! 🚀  

We’re excited to have you onboard.  
— Tech-ZenovaHub Team
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
