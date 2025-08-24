from functools import wraps
from django.shortcuts import redirect
from django.urls import resolve
from constants.enums import Role

# This module contains decorators for authentication-related checks.

def signin_required(view_func):
    @wraps(view_func)
    def wrapper(view_self, request, *args, **kwargs):
        if not hasattr(request, 'session') or not request.session.get('is_authenticated'):
            current_view_name = resolve(request.path_info).url_name
            if current_view_name != 'user_login':
                return redirect('user_login')
        return view_func(view_self, request, *args, **kwargs)
    return wrapper


def customer_required(view_func):
    @wraps(view_func)
    def wrapper(view_self, request, *args, **kwargs):
        if not request.session.get('is_authenticated') or request.session.get('user_role') != Role.ENDUSER_CUSTOMER:
            current_view_name = resolve(request.path_info).url_name
            if current_view_name != 'user_login':
                return redirect('user_login')
        return view_func(view_self, request, *args, **kwargs)
    return wrapper

def staff_required(view_func):
    @wraps(view_func)
    def wrapper(view_self, request, *args, **kwargs):
        if not request.session.get('is_authenticated') or request.session.get('user_role') != Role.ENDUSER_STAFF:
            current_view_name = resolve(request.path_info).url_name
            if current_view_name != 'user_login':
                return redirect('user_login')
        return view_func(view_self, request, *args, **kwargs)
    return wrapper

# def admin_required(view_func):
#     @wraps(view_func)
#     def wrapper(view_self, request, *args, **kwargs):
#         if not request.session.get('is_authenticated') or request.session.get('user_role') != Role.ADMIN:
#             current_view_name = resolve(request.path_info).url_name
#             if current_view_name != 'user_login':
#                 return redirect('user_login')
#         return view_func(view_self, request, *args, **kwargs)
#     return wrapper


'''
def login_admin_required(view_func):
    @wraps(view_func)
    def wrapper(view_self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role != Role.ADMIN:
            current_view_name = resolve(request.path_info).url_name
            if current_view_name != 'admin_login':
                return redirect('admin_login')
        return view_func(view_self, request, *args, **kwargs)
    return wrapper

'''


# ────────────── NEW: Admin Required Decorator ──────────────
def login_admin_required(view_func):
    """
    Restricts access to only Admin users.
    Redirects EndUser/Staff to their login page,
    Redirects unauthenticated users to admin login.
    """
    @wraps(view_func)
    def wrapper(view_self, request, *args, **kwargs):
        if not request.session.get('is_authenticated'):
            return redirect('admin_login')

        user_role = request.session.get('user_role')
        if user_role != Role.ADMIN:
            # If staff or customer tries to access admin route, send them to user login
            return redirect('user_login')

        return view_func(view_self, request, *args, **kwargs)
    return wrapper