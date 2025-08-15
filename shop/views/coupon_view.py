from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from shop.services import coupon_service
from django.utils import timezone

class CouponApplyView(View):
    def post(self, request):
        code = request.POST.get('coupon_code', '').strip()
        coupon = coupon_service.get_active_coupon_by_code(code)

        if coupon:
            request.session['applied_coupon'] = coupon.code
            messages.success(request, f"Coupon '{coupon.code}' applied: {coupon.discount_percent}% off")
        else:
            request.session.pop('applied_coupon', None)
            messages.error(request, "Invalid or expired coupon code.")

        return redirect('shop:cart_detail')

class CouponRemoveView(View):
    def post(self, request):
        if request.session.get('applied_coupon'):
            del request.session['applied_coupon']
            messages.info(request, "Coupon removed.")
        else:
            messages.warning(request, "No coupon was applied.")
        return redirect('shop:cart_detail')

class CouponListView(View):
    def get(self, request):
        coupons = coupon_service.get_all_active_coupons()
        return render(request, 'shop/coupon_list.html', {'coupons': coupons})
