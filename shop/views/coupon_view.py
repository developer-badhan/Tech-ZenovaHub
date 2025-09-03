from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseNotFound
from django.views import View
from constants.enums import Role
from shop.models import Coupon
from shop.services import coupon_service
from user.services import enduser_service
from decorators import login_admin_required,customer_required,login_admin_required_with_user,inject_authenticated_user
from django.contrib.auth import get_user_model



# Coupon list view
class CouponListView(View):
    def get(self, request):
        coupons = coupon_service.get_all_coupons()
        customers = enduser_service.get_all_customers()
        return render(request, 'coupon/coupon_list.html', {
            'coupons': coupons,
            'customers': customers
        })


# Coupon creation view
class CouponCreateView(View):
    @login_admin_required_with_user
    def get(self, request):
        return render(request, 'coupon/coupon_create.html')

    @login_admin_required_with_user
    def post(self, request):
        code = request.POST.get('code')
        discount_percent = request.POST.get('discount_percent')
        valid_from = request.POST.get('valid_from')
        valid_to = request.POST.get('valid_to')
        usage_limit = request.POST.get('usage_limit')
        try:
            coupon_service.create_coupon(
                code, discount_percent, valid_from, valid_to, usage_limit, created_by=request.user
            )
            messages.success(request, "Coupon created successfully.")
            return redirect('coupon_list')
        except Exception as e:
            messages.error(request, f"Failed to create coupon: {e}")
            return render(request, 'coupon/coupon_create.html')


# Coupon update view
class CouponUpdateView(View):
    @login_admin_required_with_user
    def get(self, request, coupon_id):
        try:
            coupon = Coupon.objects.get(id=coupon_id)
            return render(request, 'coupon/coupon_update.html', {'coupon': coupon})
        except Coupon.DoesNotExist:
            return HttpResponseNotFound("Coupon not found.")

    @login_admin_required_with_user
    def post(self, request, coupon_id):
        code = request.POST.get('code')
        discount_percent = request.POST.get('discount_percent')
        valid_from = request.POST.get('valid_from')
        valid_to = request.POST.get('valid_to')
        usage_limit = request.POST.get('usage_limit')
        try:
            coupon_service.update_coupon(coupon_id, code, discount_percent, valid_from, valid_to, usage_limit)
            messages.success(request, "Coupon updated successfully.")
            return redirect('coupon_list')
        except Exception as e:
            messages.error(request, f"Failed to update coupon: {e}")
            return redirect('coupon_update', coupon_id=coupon_id)


# Coupon deletion view
class CouponDeleteView(View):
    @login_admin_required
    def post(self, request, coupon_id):
        try:
            coupon_service.delete_coupon(coupon_id)
            messages.success(request, "Coupon deleted successfully.")
        except Exception as e:
            messages.error(request, f"Failed to delete coupon: {e}")
        return redirect('coupon_list')


# Coupon application view
class CouponApplyView(View):
    @customer_required
    def post(self, request):
        coupon_code = request.POST.get('coupon_code')
        try:
            discount = coupon_service.apply_coupon(request.user, coupon_code)
            messages.success(request, f"Coupon applied! You saved {discount}% off.")
            return redirect('order_create')  
        except Exception as e:
            messages.error(request, f"Failed to apply coupon: {e}")
            return redirect('order_create')


# Assign coupon to user view
class AssignCouponToUserView(View):
    @login_admin_required_with_user
    def post(self, request, coupon_id):
        user_id = request.POST.get('user_id')
        try:
            coupon = Coupon.objects.get(id=coupon_id)
            User = get_user_model()
            user = User.objects.get(id=user_id)
            if user.role != Role.ENDUSER_CUSTOMER:
                messages.error(request, "Only customers can be assigned coupons.")
                return redirect('coupon_list')
            coupon.used_by.add(user)
            coupon.save()
            messages.success(request, f"Coupon assigned to {user.email}.")
        except Exception as e:
            messages.error(request, f"Error assigning coupon: {e}")
        return redirect('coupon_list')


# Customer coupon list view
class CustomerCouponListView(View):
    @inject_authenticated_user
    @customer_required
    def get(self, request):
        user = request.user
        coupons = coupon_service.get_coupons_assigned_to_user(user)
        return render(request, 'coupon/customer_coupon_list.html', {'coupons': coupons})

