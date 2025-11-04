from functools import wraps
from user.utils.auth_status import get_user_login_status


# Decorator for checking logged user
def inject_login_status(view_func):
    @wraps(view_func)
    def wrapper(view_self, request, *args, **kwargs):
        is_logged_in, user_obj, user_role = get_user_login_status(request)

        # Attach to request object
        request.is_logged_in = is_logged_in
        request.active_user = user_obj
        request.user_role = user_role
        response = view_func(view_self, request, *args, **kwargs)

        # If template context exists, inject values
        if hasattr(response, "context_data"):
            response.context_data["is_logged_in"] = is_logged_in
            response.context_data["active_user"] = user_obj
            response.context_data["user_role"] = user_role

        return response

    return wrapper
