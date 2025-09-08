# import random
# from hashlib import md5
# from django.utils import timezone
# from django.core.mail import send_mail
# from django.conf import settings
# from user.models.otp_model import EmailOTP
# from user.models import User

# def _hash_otp(otp_code):
#     return md5(otp_code.encode()).hexdigest()[:6]

# def generate_otp(user):
#     raw_otp = str(random.randint(100000, 999999))
#     hashed_otp = _hash_otp(raw_otp)

#     otp_obj, _ = EmailOTP.objects.update_or_create(
#         user=user,
#         defaults={
#             "code": hashed_otp,
#             "created_at": timezone.now(),
#             "is_verified": False
#         }
#     )

#     subject = "Your Tech-ZenovaHub OTP Code"
#     message = f"""
#     Hi {user.first_name},

#     Your OTP code is: {raw_otp}
#     (Valid for 10 minutes)

#     If you didn’t request this, please ignore.

#     – Tech-ZenovaHub Team
#     """
#     send_mail(
#         subject=subject.strip(),
#         message=message.strip(),
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         recipient_list=[user.email],
#         fail_silently=False
#     )

#     return otp_obj

# from django.core.mail import send_mail
# from django.conf import settings

# def verify_otp(user, entered_code):
#     try:
#         otp_obj = EmailOTP.objects.get(user=user)
#     except EmailOTP.DoesNotExist:
#         return False, "No OTP found. Please request a new one."

#     if otp_obj.is_verified:
#         return False, "OTP already verified."

#     if otp_obj.is_expired():
#         return False, "OTP expired. Please request a new one."

#     hashed_code = _hash_otp(entered_code)
#     if otp_obj.code != hashed_code:
#         return False, "Invalid OTP. Please try again."

#     # ✅ Mark OTP as verified
#     otp_obj.is_verified = True
#     otp_obj.save()

#     # ✅ Send Welcome Email
#     subject = "Welcome to Tech-ZenovaHub 🎉"
#     message = f"""
#     Hi {user.first_name},

#     🎉 Welcome to Tech-ZenovaHub!

#     Your account has been successfully verified with OTP.
#     You can now log in and explore our platform.

#     Thanks for joining us!
#     – Tech-ZenovaHub Team
#     """
#     send_mail(
#         subject=subject.strip(),
#         message=message.strip(),
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         recipient_list=[user.email],
#         fail_silently=False,
#     )

#     return True, "OTP verified successfully. Welcome email sent!"


# def resend_otp(email):
#     try:
#         user = User.objects.get(email=email)
#         return generate_otp(user)
#     except User.DoesNotExist:
#         return None
















import random
from hashlib import md5
from django.utils import timezone
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from user.models.otp_model import EmailOTP
from user.models import User


def _hash_otp(otp_code):
    return md5(otp_code.encode()).hexdigest()[:6]


def generate_otp(user):
    raw_otp = str(random.randint(100000, 999999))
    hashed_otp = _hash_otp(raw_otp)

    otp_obj, _ = EmailOTP.objects.update_or_create(
        user=user,
        defaults={
            "code": hashed_otp,
            "created_at": timezone.now(),
            "is_verified": False
        }
    )

    subject = "Your Tech-ZenovaHub OTP Code"
    message = f"""
    Hi {user.first_name},

    Your OTP code is: {raw_otp}
    (Valid for 10 minutes)

    If you didn’t request this, please ignore.

    – Tech-ZenovaHub Team
    """

    send_mail(
        subject=subject.strip(),
        message=message.strip(),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False
    )

    return otp_obj


def verify_otp(user, entered_code):
    try:
        otp_obj = EmailOTP.objects.get(user=user)
    except EmailOTP.DoesNotExist:
        return False, "No OTP found. Please request a new one."

    if otp_obj.is_verified:
        return False, "OTP already verified."

    if otp_obj.is_expired():
        return False, "OTP expired. Please request a new one."

    hashed_code = _hash_otp(entered_code)
    if otp_obj.code != hashed_code:
        return False, "Invalid OTP. Please try again."

    # ✅ Mark OTP as verified
    otp_obj.is_verified = True
    otp_obj.save()

    # ✅ Send Welcome Email (HTML template)
    subject = "🎉 Welcome to Tech-ZenovaHub"
    html_content = render_to_string("email/welcome_email.html", {"user": user})
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject=subject.strip(),
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email],
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

    return True, "OTP verified successfully. Welcome email sent!"


def resend_otp(email):
    try:
        user = User.objects.get(email=email)
        return generate_otp(user)
    except User.DoesNotExist:
        return None
