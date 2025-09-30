from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from user.forms.admin_form import AdminUserForm
from user.forms import AdminUserUpdateForm
from user.services import admin_service
from decorators.auth_decorators import login_admin_required
from user.models import User



# Admin User Views 
class AdminUserSignupView(View):
    def get(self, request):
        form = AdminUserForm()
        return render(request, "admin/admin_signup.html", {"form": form})

    def post(self, request):
        form = AdminUserForm(request.POST)
        if form.is_valid():
            admin, error = admin_service.create_admin(
                {**form.cleaned_data, "password": request.POST.get("password")}
            )
            if error:
                return render(request, "admin/admin_signup.html", {"form": form, "error": error})
            request.session["user_id"] = admin.id
            request.session["user_role"] = admin.role
            messages.success(request, "Account created. Please request OTP to activate your account.")
            return redirect("otp_request")
        return render(request, "admin/admin_signup.html", {"form": form})


# Admin User Login View
class AdminUserLoginView(View):
    def get(self, request):
        return render(request, "admin/admin_login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user, error = admin_service.authenticate_admin(email, password, request)
        if error:
            messages.error(request, error)
            return render(request, "admin/admin_login.html")
        if not hasattr(user, "otps") or not user.otps.is_verified:
            messages.warning(request, "Your email is not verified. Please verify via OTP.")
            return redirect("otp_request")
        messages.success(request, f"Welcome {user.first_name}! You are logged in as Admin.")
        return redirect("admin_dashboard")


# Admin User Logout View
class AdminUserLogoutView(View):
    @login_admin_required
    def get(self, request):
        _, error = admin_service.logout_admin(request)
        if error:
            messages.error(request, error)
            return redirect("admin_dashboard")
        messages.success(request, "You have been logged out successfully.")
        return redirect("admin_login")


# Admin User Update and Delete Views
class AdminUserUpdateView(View):
    @login_admin_required
    def get(self, request, pk):
        admin = User.objects.get(pk=pk, role=3)
        form = AdminUserUpdateForm(instance=admin)
        return render(request, "admin/admin_update.html", {"form": form, "admin": admin})

    @login_admin_required
    def post(self, request, pk):
        admin = User.objects.get(pk=pk, role=3)
        form = AdminUserUpdateForm(request.POST, instance=admin)
        if form.is_valid():
            updated_admin, error = admin_service.update_admin(pk, form.cleaned_data)
            if error:
                messages.error(request, error)
                return render(request, "admin/admin_update.html", {"form": form})
            messages.success(request, "Admin updated successfully.")
            return redirect("admin_dashboard")
        return render(request, "admin/admin_update.html", {"form": form})


# Admin User Delete View
class AdminUserDeleteView(View):
    @login_admin_required
    def get(self, request, pk):
        return render(request, "admin/admin_delete.html", {"admin_id": pk})

    @login_admin_required
    def post(self, request, pk):
        success, error = admin_service.delete_admin(pk)
        if error:
            messages.error(request, error)
            return redirect("admin_dashboard")
        if str(request.session.get("user_id")) == str(pk):
            request.session.flush()
            messages.success(request, "Your account has been deleted.")
            return redirect("admin_login")
        return redirect("admin_dashboard")


# Admin Dashboard View
class AdminDashboardView(View):
    @login_admin_required
    def get(self, request):
        data, error = admin_service.get_dashboard_data(request)
        if error:
            messages.error(request, error)
            return render(request, "admin/admin_dashboard.html")
        return render(request, "admin/admin_dashboard.html", {
            "admin_user": data["admin"],
            "stats": data,
        })






