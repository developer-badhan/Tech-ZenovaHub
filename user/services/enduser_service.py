# from django.shortcuts import get_object_or_404
# from user.models import User
# from constants import Role


# def is_user_created(request):
#     """
#     Returns True if a valid user exists in session and DB.
#     """
#     user_id = request.session.get('user_id')
#     if not user_id:
#         return False
#     return User.objects.filter(id=user_id).exists()


# def handle_user_creation(request, data):
#     user = User.objects.create(
#         first_name=data['first_name'],
#         middle_name=data.get('middle_name'),
#         last_name=data['last_name'],
#         dob=data['dob'],
#         email=data['email'],
#         phone=data.get('phone'),
#         gender=data.get('gender'),
#         profile_photo_url=data.get('profile_photo_url'),
#         role=Role.ENDUSER
#     )
#     set_user_session(request, user)
#     return user


# def handle_user_update(user, data):
#     user.first_name = data['first_name']
#     user.middle_name = data.get('middle_name')
#     user.last_name = data['last_name']
#     user.dob = data['dob']
#     user.phone = data.get('phone')
#     user.gender = data.get('gender')
#     user.profile_photo_url = data.get('profile_photo_url')
#     user.save()
#     return user


# def handle_user_deletion(request, user_id):
#     user = get_object_or_404(User, pk=user_id)
#     user.delete()
#     clear_user_session(request)


# def set_user_session(request, user):
#     request.session['user_id'] = user.id
#     request.session['user_created'] = True


# def clear_user_session(request):
#     request.session.pop('user_id', None)
#     request.session.pop('user_created', None)
#     request.session.modified = True


# def get_session_user_or_redirect(request):
#     user_id = request.session.get('user_id')
#     if not user_id:
#         return None
#     try:
#         return User.objects.get(pk=user_id)
#     except User.DoesNotExist:
#         clear_user_session(request)
#         return None


# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_id)
# def get_user_by_id(user_id):
#     return get_object_or_404(User, pk=user_





from django.shortcuts import get_object_or_404
from user.models import User
from constants import Role


def create_user(data):
    user = User.objects.create(
        first_name=data['first_name'],
        middle_name=data.get('middle_name'),
        last_name=data['last_name'],
        dob=data['dob'],
        email=data['email'],
        phone=data.get('phone'),
        gender=data.get('gender'),
        profile_photo=data.get('profile_photo'),
        role=Role.ENDUSER
    )
    return user


def update_user(user, data):
    user.first_name = data['first_name']
    user.middle_name = data.get('middle_name')
    user.last_name = data['last_name']
    user.dob = data['dob']
    user.phone = data.get('phone')
    user.gender = data.get('gender')
    user.profile_photo = data.get('profile_photo')
    user.save()
    return user


def delete_user(user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()


def get_user_by_id(user_id):
    return get_object_or_404(User, pk=user_id)

