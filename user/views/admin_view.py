from django.views import View
from django.shortcuts import render, redirect
from user.forms.admin_form import AdminUserForm
from user.forms import AdminUserUpdateForm
from user.services import admin_service
from decorators.auth_decorators import login_admin_required
from user.models import User


# Admin Registration
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


# Admin Login
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


# Admin Logout
class AdminUserLogoutView(View):
    @login_admin_required
    def get(self, request):
        _, error = admin_service.logout_admin(request)
        if error:
            return render(request, "admin/admin_dashboard.html", {"error": error})
        return redirect("admin_login")


# Admin Update 
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
                return render(request, "admin/admin_update.html", {"form": form, "error": error})
            return redirect("admin_dashboard")
        return render(request, "admin/admin_update.html", {"form": form})


# Admin Delete
class AdminUserDeleteView(View):
    @login_admin_required
    def get(self, request, pk):
        return render(request, "admin/admin_delete.html", {"admin_id": pk})

    @login_admin_required
    def post(self, request, pk):
        success, error = admin_service.delete_admin(pk)
        if error:
            return render(request, "admin/admin_delete.html", {"error": error, "admin_id": pk})
        if str(request.session.get("user_id")) == str(pk):
            request.session.flush()  
            return redirect("admin_login")
        return redirect("admin_dashboard")


# Admin Dashboard 
class AdminDashboardView(View):
    @login_admin_required
    def get(self, request):
        data, error = admin_service.get_dashboard_data(request)
        if error:
            return render(request, "admin/admin_dashboard.html", {"error": error})    
        return render(request, "admin/admin_dashboard.html", {
            "admin_user": data["admin"],
            "stats": data,
        })
