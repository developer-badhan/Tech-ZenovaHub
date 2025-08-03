from django.urls import path
from . import views

urlpatterns = [

    # Admin routes
    path('signup/', views.AdminSignupView.as_view(), name='admin_signup'),
    path('login/', views.AdminLoginView.as_view(), name='admin_login'),
    path('dashboard/', views.AdminDashboardView.as_view(), name='admin_dashboard'),
    path('users/', views.AdminUserListView.as_view(), name='admin_user_list'),



    # Enduser routes
    path('login/', views.EndUserLoginView.as_view(), name='user_login'),
    path('user/<int:user_id>/', views.UserProfileView.as_view(), name='user_profile'),
    path('user/create/', views.UserProfileCreateView.as_view(), name='user_profile_creation'),
    path('user/update/<int:user_id>/', views.UserProfileUpdateView.as_view(), name='user_profile_update'),
    path('user/delete/<int:user_id>/', views.UserProfileDeleteView.as_view(), name='user_profile_delete'),

    # Enduser Dashboard routes
    path('customer/dashboard/', views.CustomerDashboardView.as_view(), name='customer_dashboard'),
    path('staff/dashboard/', views.StaffDashboardView.as_view(), name='staff_dashboard'),

    # Address routes
    path('user/<int:user_id>/addresses/', views.AddressListView.as_view(), name='user_address_list'),
    path('user/<int:user_id>/addresses/create/', views.AddressCreateView.as_view(), name='user_address_create'),



]

