from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseNotFound
from django.views import View
from shop.models import Coupon
from shop.services import coupon_service
from decorators import login_admin_required,customer_required

class CouponListView(View):
    def get(self, request):
        coupons = coupon_service.get_all_coupons()
        return render(request, 'coupon/coupon_list.html', {'coupons': coupons})

class CouponCreateView(View):
    @login_admin_required
    def get(self, request):
        return render(request, 'coupon/coupon_create.html')

    @login_admin_required
    def post(self, request):
        code = request.POST.get('code')
        discount_percent = request.POST.get('discount_percent')
        valid_from = request.POST.get('valid_from')
        valid_to = request.POST.get('valid_to')
        usage_limit = request.POST.get('usage_limit')

        try:
            coupon = coupon_service.create_coupon(code, discount_percent, valid_from, valid_to, usage_limit)
            messages.success(request, "Coupon created successfully.")
            return redirect('coupon_list')
        except Exception as e:
            messages.error(request, f"Failed to create coupon: {e}")
            return render(request, 'coupon/coupon_create.html')

class CouponUpdateView(View):
    @login_admin_required
    def get(self, request, coupon_id):
        try:
            coupon = Coupon.objects.get(id=coupon_id)
            return render(request, 'coupon/coupon_update.html', {'coupon': coupon})
        except Coupon.DoesNotExist:
            return HttpResponseNotFound("Coupon not found.")

    @login_admin_required
    def post(self, request, coupon_id):
        code = request.POST.get('code')
        discount_percent = request.POST.get('discount_percent')
        valid_from = request.POST.get('valid_from')
        valid_to = request.POST.get('valid_to')
        usage_limit = request.POST.get('usage_limit')

        try:
            coupon = coupon_service.update_coupon(coupon_id, code, discount_percent, valid_from, valid_to, usage_limit)
            messages.success(request, "Coupon updated successfully.")
            return redirect('coupon_list')
        except Exception as e:
            messages.error(request, f"Failed to update coupon: {e}")
            return redirect('coupon_update', coupon_id=coupon_id)

class CouponDeleteView(View):
    @login_admin_required
    def post(self, request, coupon_id):
        try:
            coupon_service.delete_coupon(coupon_id)
            messages.success(request, "Coupon deleted successfully.")
        except Exception as e:
            messages.error(request, f"Failed to delete coupon: {e}")
        return redirect('coupon_list')

class CouponApplyView(View):
    @customer_required
    def post(self, request):
        coupon_code = request.POST.get('coupon_code')
        try:
            discount = coupon_service.apply_coupon(request.user, coupon_code)
            messages.success(request, f"Coupon applied! You saved {discount}% off.")
            return redirect('order_create')  # Assuming you're on the order creation page
        except Exception as e:
            messages.error(request, f"Failed to apply coupon: {e}")
            return redirect('order_create')
