from functools import wraps
from django.shortcuts import redirect
from django.urls import resolve
from constants.enums import Role


# Sign-in required decorator
def signin_required(view_func):
    @wraps(view_func)
    def wrapper(view_self, request, *args, **kwargs):
        if not hasattr(request, 'session') or not request.session.get('is_authenticated'):
            current_view_name = resolve(request.path_info).url_name
            if current_view_name != 'user_login':
                return redirect('user_login')
        return view_func(view_self, request, *args, **kwargs)
    return wrapper


# Customer role required decorator
def customer_required(view_func):
    @wraps(view_func)
    def wrapper(view_self, request, *args, **kwargs):
        if not request.session.get('is_authenticated') or request.session.get('user_role') != Role.ENDUSER_CUSTOMER:
            current_view_name = resolve(request.path_info).url_name
            if current_view_name != 'user_login':
                return redirect('user_login')
        return view_func(view_self, request, *args, **kwargs)
    return wrapper

# Staff role required decorator
def staff_required(view_func):
    @wraps(view_func)
    def wrapper(view_self, request, *args, **kwargs):
        if not request.session.get('is_authenticated') or request.session.get('user_role') != Role.ENDUSER_STAFF:
            current_view_name = resolve(request.path_info).url_name
            if current_view_name != 'user_login':
                return redirect('user_login')
        return view_func(view_self, request, *args, **kwargs)
    return wrapper


# Login required decorator
def login_admin_required(view_func):
    @wraps(view_func)
    def wrapper(view_self, request, *args, **kwargs):
        if not request.session.get('is_authenticated'):
            return redirect('admin_login')
        user_role = request.session.get('user_role')
        if user_role != Role.ADMIN:
            return redirect('user_login')
        return view_func(view_self, request, *args, **kwargs)
    return wrapper

