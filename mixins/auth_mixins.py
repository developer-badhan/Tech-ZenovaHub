# mixins/auth_mixins.py
from django.shortcuts import redirect
from django.contrib import messages
from constants import Role

def _is_customer(user) -> bool:
    # robust: handles AnonymousUser, IntEnum/int mismatch
    return getattr(user, "is_authenticated", False) and int(getattr(user, "role", 0)) == int(Role.ENDUSER_CUSTOMER)

class CustomerRequiredMixin:
    """
    Gate for class-based views: only authenticated customers pass.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Please sign in to use your wishlist.")
            return redirect("user_login")

        if not _is_customer(request.user):
            messages.error(request, "Only customers can access the wishlist.")
            return redirect("user_login")

        return super().dispatch(request, *args, **kwargs)

