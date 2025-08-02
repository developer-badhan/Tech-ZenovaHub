# from django.shortcuts import render, redirect
# from django.views import View
# from django.contrib import messages
# from user.forms import UserRegistrationForm, UserUpdateForm
# from user.services import enduser_service


# class UserProfileCreateView(View):
#     def get(self, request):
#         if enduser_service.is_user_created(request):
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if enduser_service.is_user_created(request):
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = enduser_service.handle_user_creation(request, form.cleaned_data)
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})


# class UserProfileView(View):
#     def get(self, request):
#         user = enduser_service.get_session_user_or_redirect(request)
#         if not user:
#             return redirect('user_profile_creation')
#         return render(request, 'enduser/profile.html', {'user': user})


# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         user = enduser_service.get_user_by_id(user_id)
#         form = UserUpdateForm(instance=user)
#         return render(request, 'enduser/profile_updation.html', {'form': form, 'user': user})

#     def post(self, request, user_id):
#         user = enduser_service.get_user_by_id(user_id)
#         form = UserUpdateForm(request.POST, instance=user)
#         if form.is_valid():
#             enduser_service.handle_user_update(user, form.cleaned_data)
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form, 'user': user})


# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         enduser_service.handle_user_deletion(request, user_id)
#         messages.success(request, "Profile deleted successfully.")
#         return redirect('user_profile_creation')



from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from user.forms import UserRegistrationForm, UserUpdateForm
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
