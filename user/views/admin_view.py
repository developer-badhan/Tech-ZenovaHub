from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from urllib.parse import urlencode
from user.forms import AdminUserForm
from user.services import create_admin, authenticate_admin
from constants import Role


class AdminUserSignupView(View):
    def get(self, request):
        form = AdminUserForm()
        return render(request, "admin/admin_signup.html", {"form": form})

    def post(self, request):
        form = AdminUserForm(request.POST, request.FILES)
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return render(request, "admin/admin_signup.html", {
                "form": form,
                "toast_status": "error",
                "toast_message": "Passwords do not match."
            })

        if form.is_valid():
            data = form.cleaned_data
            data["password"] = password
            create_admin(data)
            query = urlencode({"status": "success", "message": "Admin account created successfully. Please log in."})
            return redirect("admin_login")
        else:
            return render(request, "admin/admin_signup.html", {
                "form": form,
                "toast_status": "error",
                "toast_message": "Please correct the errors below."
            })


class AdminUserLoginView(View):
    def get(self, request):
        return render(request, "admin/admin_login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate_admin(email, password)

        if user:
            login(request, user)
            query = urlencode({"status": "success", "message": f"Welcome {user.first_name}!"})
            return redirect("admin_dashboard")
        else:
            return render(request, "admin/admin_login.html", {
                "toast_status": "error",
                "toast_message": "Invalid email or password."
            })


class AdminUserLogoutView(View):
    def get(self, request):
        logout(request)
        query = urlencode({"status": "success", "message": "You have been logged out."})
        return redirect("admin_login")


@method_decorator(login_required(login_url="admin_login"), name="dispatch")
class AdminDashboardView(View):
    def get(self, request):
        if request.user.role != Role.ADMIN:
            return redirect("admin_signup")
        return render(request, "admin/admin_dashboard.html")






# user/views.py

from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from user.forms import AdminUserUpdateForm
from user.services import update_admin, delete_admin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from constants import Role
from user.models import User


@method_decorator(login_required(login_url='admin_login'), name='dispatch')
class AdminUserUpdateView(View):
    def get(self, request, pk):
        if request.user.role != Role.ADMIN or request.user.pk != pk:
            return redirect('admin_dashboard')

        admin_user = get_object_or_404(User, pk=pk)
        form = AdminUserUpdateForm(instance=admin_user)
        return render(request, "admin/admin_update.html", {"form": form, "admin_user": admin_user})

    def post(self, request, pk):
        if request.user.role != Role.ADMIN or request.user.pk != pk:
            return redirect('admin_dashboard')

        admin_user = get_object_or_404(User, pk=pk)
        form = AdminUserUpdateForm(request.POST, request.FILES, instance=admin_user)

        if form.is_valid():
            update_admin(pk, form.cleaned_data)
            messages.success(request, "Profile updated successfully.")
            return redirect(reverse("admin_dashboard"))
        else:
            return render(request, "admin/admin_update.html", {
                "form": form,
                "admin_user": admin_user,
                "toast_status": "error",
                "toast_message": "Please correct the errors below."
            })


   

@method_decorator(login_required(login_url='admin_login'), name='dispatch')
class AdminUserDeleteView(View):
    def get(self, request, pk):
        if request.user.role != Role.ADMIN or request.user.pk != pk:
            return redirect('admin_dashboard')
        return render(request, "admin/admin_delete.html", {"admin_user": request.user})

    def post(self, request, pk):
        if request.user.role != Role.ADMIN or request.user.pk != pk:
            return redirect('admin_dashboard')

        delete_admin(pk)
        logout(request)
        return redirect("admin_signup")
