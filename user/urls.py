from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:user_id>/', views.UserProfileView.as_view(), name='user_profile'),
    path('user/create/', views.UserProfileCreateView.as_view(), name='user_profile_creation'),
    path('user/update/<int:user_id>/', views.UserProfileUpdateView.as_view(), name='user_profile_update'),
    path('user/delete/<int:user_id>/', views.UserProfileDeleteView.as_view(), name='user_profile_delete'),
]

