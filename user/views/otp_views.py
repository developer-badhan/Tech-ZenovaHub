from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from user.models import User
from user.forms import otp_forms
from user.services import otp_service
from constants.enums import Role
from user.serializers import otp_serializers
from user.utils import get_user_role



# View to handle OTP requests
class OTPRequestView(View):
    def get_template(self, request):
        role = get_user_role(request)
        print(f"User role in session: {role}")
        if role == Role.ADMIN:
            return "admin/otp/otp_request.html"
        elif role in [Role.ENDUSER_CUSTOMER, Role.ENDUSER_STAFF]:
            return "otp/otp_request.html"
        else:
            return "otp/otp_request.html"

    def get(self, request):
        form = otp_forms.OTPRequestForm()
        return render(request, self.get_template(request), {"form": form})

    def post(self, request):
        form = otp_forms.OTPRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            try:
                user = User.objects.get(email=email)
                otp_obj = otp_service.generate_otp(user)
                serializer = otp_serializers.OTPSerializer(otp_obj)
                print(f"The OTP is: {serializer.data}")
                messages.success(request, "OTP sent to your email. Please verify to continue.")
                return redirect("otp_verify")
            except User.DoesNotExist:
                form.add_error("email", "User not found.")
        return render(request, self.get_template(request), {"form": form})


# View to handle OTP verification
class OTPVerifyView(View):
    def get_template(self, request):
        role = get_user_role(request)
        print(f"User role in session: {role}")
        if role == Role.ADMIN:
            return "admin/otp/otp_verify.html"
        elif role in [Role.ENDUSER_CUSTOMER, Role.ENDUSER_STAFF]:
            return "otp/otp_verify.html"
        else:
            return "otp/otp_verify.html"
        
    def get(self, request):
        form = otp_forms.OTPVerifyForm()
        return render(request, self.get_template(request), {"form": form})

    def post(self, request):
        form = otp_forms.OTPVerifyForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            code = form.cleaned_data["otp_code"]
            try:
                user = User.objects.get(email=email)
                success, message = otp_service.verify_otp(user, code)
                if success:
                    user.otps.is_verified = True
                    user.otps.save()
                    if user.role == Role.ADMIN:
                        messages.success(request, "OTP verified! Please log in as Admin.")
                        return redirect("admin_login")
                    else:
                        messages.success(request, "OTP verified! Please log in.")
                        return redirect("user_login")
                else:
                    form.add_error("otp_code", message)
            except User.DoesNotExist:
                form.add_error("email", "User not found.")
        return render(request, self.get_template(request), {"form": form})


# View to handle OTP resend requests
class OTPResendView(View):
    def get_template(self, request):
        role = get_user_role(request)
        print(f"User role in session: {role}")
        if role == Role.ADMIN:
            return "admin/otp/otp_resend.html"
        elif role in [Role.ENDUSER_CUSTOMER, Role.ENDUSER_STAFF]:
            return "otp/otp_resend.html"
        else:
            return "otp/otp_resend.html"
        
    def get(self, request):
        form = otp_forms.OTPResendForm()
        return render(request, self.get_template(request), {"form": form})

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
                    print(f"The OTP is: {serializer.data}")
                    messages.success(request, "OTP resent successfully. Please check your email.")
                    return redirect("otp_verify")
                else:
                    form.add_error("email", "Failed to resend OTP.")
            except User.DoesNotExist:
                form.add_error("email", "User not found.")
        return render(request, self.get_template(request), {"form": form})

