from user.models import User


# Retrieve user role from session or database
def get_user_role(request):
    try:
        if "user_role" in request.session:
            role = request.session.get("user_role")
            if role is not None:
                return int(role)
        user_id = request.session.get("user_id")
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                request.session["user_role"] = user.role  # cache
                return user.role
            except User.DoesNotExist:
                return None
    except Exception as e:
        print(f"Error retrieving user role: {e}")
        return None
    return None
