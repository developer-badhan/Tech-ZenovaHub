from user.utils.auth_status import get_user_login_status

# Context Processor
def auth_context(request):
    is_logged_in, user_obj, user_role = get_user_login_status(request)
    return {
        "is_logged_in": is_logged_in,
        "active_user": user_obj,
        "user_role": user_role,
    }
