from django.urls import path
from . import views

urlpatterns = [

    # ────── Auth Routes ──────
    path('signin/', views.EndUserLoginView.as_view(), name='user_login'),
    path('signout/', views.EndUserLogoutView.as_view(), name='user_logout'),

    # ────── Signup Routes ──────
    path('signup/', views.UserProfileCreateView.as_view(), name='user_profile_creation'),

    # ────── Dashboard Routes ──────
    path('customer/dashboard/', views.CustomerDashboardView.as_view(), name='customer_dashboard'),
    path('staff/dashboard/', views.StaffDashboardView.as_view(), name='staff_dashboard'),

    # ────── Enduser Profile Routes ──────
    path('user/<int:user_id>/profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('user/update/<int:user_id>/', views.UserProfileUpdateView.as_view(), name='user_profile_update'),
    path('user/delete/<int:user_id>/', views.UserDeleteView.as_view(), name='user_delete'),


    # ────── Address Routes ──────
    path('user/<int:user_id>/addresses/', views.AddressListView.as_view(), name='user_address_list'),
    path('user/<int:user_id>/addresses/create/', views.AddressCreateView.as_view(), name='user_address_create'),
    path('user/<int:user_id>/addresses/update/<int:address_id>/', views.AddressUpdateView.as_view(), name='user_address_update'),

]
