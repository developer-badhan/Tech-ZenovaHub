# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from django.contrib import messages
# from django.urls import reverse
# from django.contrib.auth import login
# from django.http import HttpResponseForbidden
# from user.models import User
# from user.forms import UserRegistrationForm, UserUpdateForm



# from django.shortcuts import redirect

# def home_view(request):
#     return render(request, 'home.html')

# def home_redirect(request):
#     return redirect('user_profile')


# # Helper: Only allow ENDUSERs to access these views
# def user_is_enduser(user):
#     from constants import Role
#     return user.is_authenticated and user.role == Role.ENDUSER

# class UserProfileView(View):
#     def get(self, request):
#         if not user_is_enduser(request.user):
#             return HttpResponseForbidden("Only ENDUSERs can access this page.")
#         return render(request, 'enduser/profile.html', {'user_obj': request.user})

# class UserProfileCreateView(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm()
#         return render(request, 'enduser/profile_creation.html', {'form': form})

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('user_profile')
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             from constants import Role
#             user.role = Role.ENDUSER  # Ensure only ENDUSER can register
#             user.save()
#             login(request, user)
#             messages.success(request, "Account created successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_creation.html', {'form': form})

# class UserProfileUpdateView(View):
#     def get(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(instance=request.user)
#         return render(request, 'enduser/profile_updation.html', {'form': form})

#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to edit this profile.")
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully.")
#             return redirect('user_profile')
#         return render(request, 'enduser/profile_updation.html', {'form': form})

# class UserProfileDeleteView(View):
#     def post(self, request, user_id):
#         if request.user.id != user_id or not user_is_enduser(request.user):
#             return HttpResponseForbidden("You are not authorized to delete this profile.")
#         request.user.delete()
#         messages.success(request, "Account deleted successfully.")
#         return redirect('user_profile_creation')