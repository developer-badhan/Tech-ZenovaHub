from django.shortcuts import redirect
from django.urls import reverse
from user.models.otp_model import EmailOTP as OTP


# Middleware to enforce OTP verification before accessing certain views
class OTPVerificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/admin/") or request.path.startswith("/static/"):
            return self.get_response(request)
        user_id = request.session.get("user_id")
        if user_id:
            try:
                otp_obj = OTP.objects.get(user_id=user_id)
                if not otp_obj.is_verified:
                    if not request.path.startswith(reverse("otp_verify")) and not request.path.startswith(reverse("otp_resend")):
                        return redirect("otp_verify")
            except OTP.DoesNotExist:
                print("OTP record does not exist for user.")
        return self.get_response(request)
