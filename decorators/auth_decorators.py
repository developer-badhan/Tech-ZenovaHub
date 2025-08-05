'''decorators/auth_decorators.py
This module contains decorators for authentication-related checks.
'''

from functools import wraps
from django.shortcuts import redirect
from django.urls import resolve
from constants.enums import Role

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


