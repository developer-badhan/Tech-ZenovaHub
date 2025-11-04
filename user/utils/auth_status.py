from django.contrib.auth import get_user_model
from user.utils.session_utils import get_user_role


# User Login Status
def get_user_login_status(request):
    User = get_user_model()
    user_obj = None
    user_role = None
    is_logged_in = False

    try:
        user = getattr(request, "user", None)
        if user and getattr(user, "is_authenticated", False):
            is_logged_in = True
            user_obj = user
            user_role = getattr(user, "role", None)
            return is_logged_in, user_obj, user_role
        user_id = request.session.get("user_id")
        if user_id:
            try:
                user_obj = User.objects.get(id=user_id)
                is_logged_in = True
                user_role = get_user_role(request)
            except User.DoesNotExist:
                user_obj = None
                is_logged_in = False
                user_role = None

    except Exception as e:
        print(f"[AuthStatus] Error checking login status: {e}")
    return is_logged_in, user_obj, user_role
