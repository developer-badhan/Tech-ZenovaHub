from django.urls import path
from . import views

# user app URL configuration

urlpatterns = [

    # Admin User Routes
    path('admin/signin/',views.AdminUserLoginView.as_view(),name='admin_login'),
    path('admin/signup/',views.AdminUserSignupView.as_view(),name='admin_signup'),
    path('admin/signout/',views.AdminUserLogoutView.as_view(),name='admin_logout'),
    path('admin/update/<int:pk>/', views.AdminUserUpdateView.as_view(), name='admin_update'),
    path('admin/delete/<int:pk>/', views.AdminUserDeleteView.as_view(), name='admin_delete'),
    path('admin/dashboard/', views.AdminDashboardView.as_view(), name='admin_dashboard'),

    # User Authentication Routes
    path('signin/', views.EndUserLoginView.as_view(), name='user_login'),
    path('signout/', views.EndUserLogoutView.as_view(), name='user_logout'),

    # User Registration Routes
    path('signup/', views.EndUserProfileCreateView.as_view(), name='user_profile_creation'),

    # User Dashboard Routes
    path('customer/dashboard/', views.CustomerDashboardView.as_view(), name='customer_dashboard'),
    path('staff/dashboard/', views.StaffDashboardView.as_view(), name='staff_dashboard'),

    # Enduser Profile Routes
    path('user/<int:user_id>/profile/', views.EndUserProfileView.as_view(), name='user_profile'),
    path('user/update/<int:user_id>/', views.EndUserProfileUpdateView.as_view(), name='user_profile_update'),
    path('user/delete/<int:user_id>/', views.EndUserDeleteView.as_view(), name='user_delete'),

    # User Address Routes
    path('user/<int:user_id>/addresses/create/', views.AddressCreateView.as_view(), name='user_address_create'),
    path('user/<int:user_id>/addresses/update/<int:address_id>/', views.AddressUpdateView.as_view(), name='user_address_update'),

] 







