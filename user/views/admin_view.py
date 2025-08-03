# user/views/admin_view.py
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from user.forms.admin_form import AdminSignupForm, AdminLoginForm
from user.services import admin_service

class AdminSignupView(View):
    def get(self, request):
        form = AdminSignupForm()
        return render(request, 'admin/signup.html', {'form': form})

    def post(self, request):
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            admin_service.create_admin(form.cleaned_data)
            messages.success(request, "Admin registered successfully.")
            return redirect('admin_login')
        return render(request, 'admin/signup.html', {'form': form})


class AdminLoginView(View):
    def get(self, request):
        form = AdminLoginForm()
        return render(request, 'admin/login.html', {'form': form})

    def post(self, request):
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            user = admin_service.authenticate_admin(
                form.cleaned_data['email'], form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('/admin/dashboard/')  # Placeholder
            messages.error(request, "Invalid credentials.")
        return render(request, 'admin/login.html', {'form': form})


# user/views/admin_view.py

from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from constants import Role

class AdminDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.role != Role.ADMIN:
            return redirect('admin_login')
        return render(request, 'admin/dashboard.html')


# user/views/admin_view.py (append)
from user.models import User

class AdminUserListView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.role != Role.ADMIN:
            return redirect('admin_login')
        users = User.objects.exclude(role=Role.ADMIN)  # Exclude self/admins
        return render(request, 'admin/user_list.html', {'users': users})
