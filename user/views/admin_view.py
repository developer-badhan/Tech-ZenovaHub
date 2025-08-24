# from django.views import View
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, logout
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
# from urllib.parse import urlencode
# from user.forms import AdminUserForm
# from user.services import create_admin, authenticate_admin
# from constants import Role


# class AdminUserSignupView(View):
#     def get(self, request):
#         form = AdminUserForm()
#         return render(request, "admin/admin_signup.html", {"form": form})

#     def post(self, request):
#         form = AdminUserForm(request.POST, request.FILES)
#         password = request.POST.get("password")
#         confirm_password = request.POST.get("confirm_password")

#         if password != confirm_password:
#             return render(request, "admin/admin_signup.html", {
#                 "form": form,
#                 "toast_status": "error",
#                 "toast_message": "Passwords do not match."
#             })

#         if form.is_valid():
#             data = form.cleaned_data
#             data["password"] = password
#             create_admin(data)
#             query = urlencode({"status": "success", "message": "Admin account created successfully. Please log in."})
#             return redirect("admin_login")
#         else:
#             return render(request, "admin/admin_signup.html", {
#                 "form": form,
#                 "toast_status": "error",
#                 "toast_message": "Please correct the errors below."
#             })


# class AdminUserLoginView(View):
#     def get(self, request):
#         return render(request, "admin/admin_login.html")

#     def post(self, request):
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         user = authenticate_admin(email, password)

#         if user:
#             login(request, user)
#             query = urlencode({"status": "success", "message": f"Welcome {user.first_name}!"})
#             return redirect("admin_dashboard")
#         else:
#             return render(request, "admin/admin_login.html", {
#                 "toast_status": "error",
#                 "toast_message": "Invalid email or password."
#             })


# class AdminUserLogoutView(View):
#     def get(self, request):
#         logout(request)
#         query = urlencode({"status": "success", "message": "You have been logged out."})
#         return redirect("admin_login")


# @method_decorator(login_required(login_url="admin_login"), name="dispatch")
# class AdminDashboardView(View):
#     def get(self, request):
#         if request.user.role != Role.ADMIN:
#             return redirect("admin_signup")
#         return render(request, "admin/admin_dashboard.html")






# # user/views.py

# from django.views import View
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from django.urls import reverse
# from user.forms import AdminUserUpdateForm
# from user.services import update_admin, delete_admin
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
# from constants import Role
# from user.models import User


# # @method_decorator(login_required(login_url='admin_login'), name='dispatch')
# class AdminUserUpdateView(View):
#     def get(self, request, pk):
#         if request.user.role != Role.ADMIN or request.user.pk != pk:
#             return redirect('admin_dashboard')

#         admin_user = get_object_or_404(User, pk=pk)
#         form = AdminUserUpdateForm(instance=admin_user)
#         return render(request, "admin/admin_update.html", {"form": form, "admin_user": admin_user})

#     def post(self, request, pk):
#         if request.user.role != Role.ADMIN or request.user.pk != pk:
#             return redirect('admin_dashboard')

#         admin_user = get_object_or_404(User, pk=pk)
#         form = AdminUserUpdateForm(request.POST, request.FILES, instance=admin_user)

#         if form.is_valid():
#             update_admin(pk, form.cleaned_data)
#             messages.success(request, "Profile updated successfully.")
#             return redirect(reverse("admin_dashboard"))
#         else:
#             return render(request, "admin/admin_update.html", {
#                 "form": form,
#                 "admin_user": admin_user,
#                 "toast_status": "error",
#                 "toast_message": "Please correct the errors below."
#             })


   

# # @method_decorator(login_required(login_url='admin_login'), name='dispatch')
# class AdminUserDeleteView(View):
#     def get(self, request, pk):
#         if request.user.role != Role.ADMIN or request.user.pk != pk:
#             return redirect('admin_dashboard')
#         return render(request, "admin/admin_delete.html", {"admin_user": request.user})

#     def post(self, request, pk):
#         if request.user.role != Role.ADMIN or request.user.pk != pk:
#             return redirect('admin_dashboard')

#         delete_admin(pk)
#         logout(request)
#         return redirect("admin_signup")




from django.views import View
from django.shortcuts import render, redirect
from user.forms.admin_form import AdminUserForm
from user.forms import AdminUserUpdateForm
from user.services import admin_service
from decorators.auth_decorators import login_admin_required
from user.models import User


# ────────────── Admin Signup ──────────────
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
            return redirect("admin_login")
        return render(request, "admin/admin_signup.html", {"form": form})


# ────────────── Admin Login ──────────────
class AdminUserLoginView(View):
    def get(self, request):
        return render(request, "admin/admin_login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user, error = admin_service.authenticate_admin(email, password, request)
        if error:
            return render(request, "admin/admin_login.html", {"error": error})
        return redirect("admin_dashboard")


# ────────────── Admin Logout ──────────────
class AdminUserLogoutView(View):
    @login_admin_required
    def get(self, request):
        _, error = admin_service.logout_admin(request)
        if error:
            return render(request, "admin/admin_dashboard.html", {"error": error})
        return redirect("admin_login")


# ────────────── Admin Update ──────────────
class AdminUserUpdateView(View):
    @login_admin_required
    def get(self, request, pk):
        admin = User.objects.get(pk=pk, role=3)  # role=3 → ADMIN
        form = AdminUserUpdateForm(instance=admin)
        return render(request, "admin/admin_update.html", {"form": form, "admin": admin})

    @login_admin_required
    def post(self, request, pk):
        admin = User.objects.get(pk=pk, role=3)
        form = AdminUserUpdateForm(request.POST, instance=admin)
        if form.is_valid():
            updated_admin, error = admin_service.update_admin(pk, form.cleaned_data)
            if error:
                return render(request, "admin/admin_update.html", {"form": form, "error": error})
            return redirect("admin_dashboard")
        return render(request, "admin/admin_update.html", {"form": form})


# ────────────── Admin Delete ──────────────
from django.views import View
from django.shortcuts import render, redirect
from decorators.auth_decorators import login_admin_required
from user.services import admin_service


class AdminUserDeleteView(View):
    @login_admin_required
    def get(self, request, pk):
        return render(request, "admin/admin_delete.html", {"admin_id": pk})

    @login_admin_required
    def post(self, request, pk):
        success, error = admin_service.delete_admin(pk)

        if error:
            return render(request, "admin/admin_delete.html", {"error": error, "admin_id": pk})

        # If current logged-in admin deleted their own account → log them out & redirect to login
        if str(request.session.get("user_id")) == str(pk):
            request.session.flush()  # clear session
            return redirect("admin_login")

        # Otherwise, redirect to dashboard (in case one admin deletes another admin)
        return redirect("admin_dashboard")


# ────────────── Admin Dashboard ──────────────
from django.views import View
from django.shortcuts import render
from decorators.auth_decorators import login_admin_required
from user.services import admin_service




class AdminDashboardView(View):
    @login_admin_required
    def get(self, request):
        data, error = admin_service.get_dashboard_data()
        if error:
            return render(request, "admin/admin_dashboard.html", {"error": error})
        return render(request, "admin/admin_dashboard.html", {
            "admin": request.user,
            "stats": data,
        })



# @method_decorator(login_admin_required(login_url="admin_login"), name="dispatch")
# class AdminDashboardView(View):
#     def get(self, request):
#         if request.user.role != Role.ADMIN:
#             return redirect("admin_signup")
#         return render(request, "admin/admin_dashboard.html")

