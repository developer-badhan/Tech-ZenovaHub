from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from constants.enums import Role
from user.forms import UserRegistrationForm,UserUpdateForm
from user.services import enduser_service


class UserProfileCreateView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'enduser/profile_creation.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = enduser_service.create_user(form.cleaned_data)
            return redirect('user_profile', user_id=user.id)
        return render(request, 'enduser/profile_creation.html', {'form': form})


class UserProfileView(View):
    def get(self, request, user_id):
        user = enduser_service.get_user_by_id(user_id)
        return render(request, 'enduser/profile.html', {'user': user})


class UserProfileUpdateView(View):
    def get(self, request, user_id):
        user = enduser_service.get_user_by_id(user_id)
        form = UserUpdateForm(instance=user)
        return render(request, 'enduser/profile_updation.html', {'form': form, 'user': user})

    def post(self, request, user_id):
        user = enduser_service.get_user_by_id(user_id)
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            enduser_service.update_user(user, form.cleaned_data)
            messages.success(request, "Profile updated successfully.")
            return redirect('user_profile', user_id=user.id)
        return render(request, 'enduser/profile_updation.html', {'form': form, 'user': user})


class UserProfileDeleteView(View):
    def post(self, request, user_id):
        enduser_service.delete_user(user_id)
        messages.success(request, "Profile deleted successfully.")
        return redirect('user_profile_creation')


# user/views/enduser_view.py (append at bottom)
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from user.forms.login_form import EndUserLoginForm
from django.utils.decorators import method_decorator

class EndUserLoginView(View):
    def get(self, request):
        form = EndUserLoginForm()
        return render(request, 'enduser/login.html', {'form': form})

    def post(self, request):
        form = EndUserLoginForm(request.POST)
        if form.is_valid():
            user = enduser_service.authenticate_user(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                if user.role == Role.ADMIN:
                    messages.error(request, "Admins must use a separate login.")
                    return redirect('user_login')

                login(request, user)
                if user.role == Role.ENDUSER_CUSTOMER:
                    return redirect('customer_dashboard')
                elif user.role == Role.ENDUSER_STAFF:
                    return redirect('staff_dashboard')
            else:
                messages.error(request, "Invalid credentials.")
        return render(request, 'enduser/login.html', {'form': form})



# user/views/enduser_view.py

from django.contrib.auth.mixins import LoginRequiredMixin
from constants import Role

class CustomerDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.role != Role.ENDUSER_CUSTOMER:
            return redirect('user_login')
        return render(request, 'enduser/customer_dashboard.html')


class StaffDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.role != Role.ENDUSER_STAFF:
            return redirect('user_login')
        return render(request, 'enduser/staff_dashboard.html')
