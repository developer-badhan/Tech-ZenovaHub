from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from user.forms.login_form import EndUserLoginForm
from user.forms import UserRegistrationForm, UserUpdateForm
from constants.enums import Role
from user.services import enduser_service,address_service
from decorators.auth_decorators import signin_required, customer_required, staff_required


# User Authentication Views

class EndUserLoginView(View):
    def get(self, request):
        try:
            if request.session.get('user_id'):
                return redirect('customer_dashboard')
            form = EndUserLoginForm()
            return render(request, 'login/login.html', {'form': form})
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('user_login')

    def post(self, request):
        try:
            form = EndUserLoginForm(request.POST)
            if form.is_valid():
                user = enduser_service.authenticate_user(
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                if user:
                    if user.role == Role.ADMIN:
                        messages.error(request, "Admins must use a separate login.")
                        return redirect('user_login')

                    request.session['user_id'] = user.id
                    request.session['user_role'] = user.role
                    request.session['is_authenticated'] = True

                    if user.role == Role.ENDUSER_CUSTOMER:
                        return redirect('customer_dashboard')
                    elif user.role == Role.ENDUSER_STAFF:
                        return redirect('staff_dashboard')
                else:
                    messages.error(request, "Invalid email or password.")
            return render(request, 'login/login.html', {'form': form})
        except Exception as e:
            messages.error(request, f"Login error: {str(e)}")
            return redirect('user_login')


class EndUserLogoutView(View):
    def get(self, request):
        try:
            request.session.flush()
            messages.success(request, "Signed out successfully.")
        except Exception as e:
            messages.error(request, f"Logout failed: {str(e)}")
        return redirect('user_login')



# User Dashboard Views

class CustomerDashboardView(View):
    @signin_required
    @customer_required
    def get(self, request):
        try:
            user_id = request.session.get('user_id')
            user = enduser_service.get_user_by_id(user_id)
            addresses = address_service.get_user_addresses(user)
            default_address = addresses.first() 

            return render(request, 'dashboard/customer_dashboard.html', {
                'default_address': default_address
            })
        except Exception as e:
            messages.error(request, f"Error loading dashboard: {str(e)}")
            return redirect('user_login')


class StaffDashboardView(View):
    @signin_required
    @staff_required
    def get(self, request):
        try:
            user_id = request.session.get('user_id')
            user = enduser_service.get_user_by_id(user_id)
            addresses = address_service.get_user_addresses(user)
            default_address = addresses.first() 
            return render(request, 'dashboard/staff_dashboard.html', {
                'default_address': default_address
            })
        except Exception as e:
            messages.error(request, f"Error loading dashboard: {str(e)}")
            return redirect('user_login')





# User Profile Management Views
class EndUserProfileCreateView(View):
    def get(self, request):
        try:
            if request.session.get('is_authenticated'):
                return redirect('customer_dashboard')
            form = UserRegistrationForm()
            return render(request, 'enduser/profile_creation.html', {'form': form})
        except Exception as e:
            messages.error(request, f"Error loading signup page: {str(e)}")
            return redirect('user_login')

    def post(self, request):
        try:
            if request.session.get('is_authenticated'):
                return redirect('customer_dashboard')

            form = UserRegistrationForm(request.POST, request.FILES)
            if form.is_valid():
                user = enduser_service.create_user(form.cleaned_data)
                request.session['user_id'] = user.id
                request.session['user_role'] = user.role
                request.session['is_authenticated'] = True
                return redirect('user_address_create', user_id=user.id)
            return render(request, 'enduser/profile_creation.html', {'form': form})
        except Exception as e:
            messages.error(request, f"Error during registration: {str(e)}")
            return redirect('user_login')


class EndUserProfileView(View):
    @signin_required
    def get(self, request, user_id):
        try:
            if request.session.get('user_id') != user_id:
                return redirect('user_login')
            user = enduser_service.get_user_by_id(user_id)
            address = address_service.get_user_addresses(user)
            context = {
                'user': user,
                'address': address
            }
            return render(request, 'enduser/profile.html', context)
        except Exception as e:
            messages.error(request, f"Failed to load profile: {str(e)}")
            return redirect('user_login')


class EndUserProfileUpdateView(View):
    @signin_required
    def get(self, request, user_id):
        try:
            if request.session.get('user_id') != user_id:
                return redirect('user_login')
            user = enduser_service.get_user_by_id(user_id)
            form = UserUpdateForm(instance=user)
            return render(request, 'enduser/profile_updation.html', {'form': form, 'user': user})
        except Exception as e:
            messages.error(request, f"Error loading update form: {str(e)}")
            return redirect('user_profile', user_id=user_id)

    @signin_required
    def post(self, request, user_id):
        try:
            if request.session.get('user_id') != user_id:
                return redirect('user_login')
            user = enduser_service.get_user_by_id(user_id)
            form = UserUpdateForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                enduser_service.update_user(user, form.cleaned_data)
                messages.success(request, "Profile updated successfully.")
                return redirect('user_profile', user_id=user.id)
            return render(request, 'enduser/profile_updation.html', {'form': form, 'user': user})
        except Exception as e:
            messages.error(request, f"Update failed: {str(e)}")
            return redirect('user_profile', user_id=user_id)


class EndUserDeleteView(View):
    @signin_required
    def get(self, request, user_id):
        try:
            if request.session.get('user_id') != user_id:
                return redirect('user_login')
            return render(request, 'enduser/confirm_delete.html', {'user_id': user_id})
        except Exception as e:
            messages.error(request, f"Error showing delete confirmation: {str(e)}")
            return redirect('user_profile', user_id=user_id)

    @signin_required
    def post(self, request, user_id):
        try:
            if request.session.get('user_id') != user_id:
                return redirect('user_login')
            enduser_service.delete_user(user_id)
            request.session.flush()
            messages.success(request, "Your account has been deleted.")
            return redirect('user_login')
        except Exception as e:
            messages.error(request, f"An error occurred while deleting the account: {str(e)}")
            return redirect('user_profile', user_id=user_id)





