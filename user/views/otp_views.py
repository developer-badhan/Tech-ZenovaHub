from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from user.models import User
from user.forms import otp_forms
from user.services import otp_service
from user.serializers import otp_serializers


class OTPRequestView(View):
    """
    Handles OTP request via email.
    """

    def get(self, request):
        form = otp_forms.OTPRequestForm()
        return render(request, "otp/otp_request.html", {"form": form})

    def post(self, request):
        form = otp_forms.OTPRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            try:
                user = User.objects.get(email=email)
                otp_obj = otp_service.generate_otp(user)

                serializer = otp_serializers.OTPSerializer(otp_obj)
                messages.success(request, "OTP sent to your email.")
                return JsonResponse({"status": "success", "data": serializer.data})

            except User.DoesNotExist:
                form.add_error("email", "User not found.")

        return render(request, "otp/otp_request.html", {"form": form})


class OTPVerifyView(View):
    """
    Handles OTP verification.
    """

    def get(self, request):
        form = otp_forms.OTPVerifyForm()
        return render(request, "otp/otp_verify.html", {"form": form})

    def post(self, request):
        form = otp_forms.OTPVerifyForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            code = form.cleaned_data["otp_code"]

            try:
                user = User.objects.get(email=email)
                success, message = otp_service.verify_otp(user, code)

                if success:
                    messages.success(request, message)
                    return JsonResponse({"status": "success", "message": message})
                else:
                    form.add_error("otp_code", message)

            except User.DoesNotExist:
                form.add_error("email", "User not found.")

        return render(request, "otp/otp_verify.html", {"form": form})


class OTPResendView(View):
    """
    Handles resending OTP.
    """

    def get(self, request):
        form = otp_forms.OTPResendForm()
        return render(request, "otp/otp_resend.html", {"form": form})

    def post(self, request):
        form = otp_forms.OTPResendForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            try:
                user = User.objects.get(email=email)
                otp_obj = otp_service.resend_otp(email)

                if otp_obj:
                    serializer = otp_serializers.OTPSerializer(otp_obj)
                    messages.success(request, "OTP resent successfully.")
                    return JsonResponse({"status": "success", "data": serializer.data})
                else:
                    form.add_error("email", "Failed to resend OTP.")

            except User.DoesNotExist:
                form.add_error("email", "User not found.")

        return render(request, "otp/otp_resend.html", {"form": form})
