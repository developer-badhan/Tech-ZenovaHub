# This file contains decorators for authentication and authorization checks.

from functools import wraps
from django.shortcuts import redirect
from constants.enums import Role

def signin_required(view_func):
    @wraps(view_func)
    def wrapper(view_self, request, *args, **kwargs):
        if not hasattr(request, 'session') or not request.session.get('is_authenticated'):
            return redirect('user_login')
        return view_func(view_self, request, *args, **kwargs)
    return wrapper

def customer_required(view_func):
    @wraps(view_func)
    def wrapper(view_self, request, *args, **kwargs):
        if not request.session.get('is_authenticated') or request.session.get('user_role') != Role.ENDUSER_CUSTOMER:
            return redirect('user_login')
        return view_func(view_self, request, *args, **kwargs)
    return wrapper

def staff_required(view_func):
    @wraps(view_func)
    def wrapper(view_self, request, *args, **kwargs):
        if not request.session.get('is_authenticated') or request.session.get('user_role') != Role.ENDUSER_STAFF:
            return redirect('user_login')
        return view_func(view_self, request, *args, **kwargs)
    return wrapper



