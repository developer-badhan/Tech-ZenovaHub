from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from shop.services import coupon_service
from django.utils import timezone

# class CouponApplyView(View):
#     def post(self, request):
#         code = request.POST.get('coupon_code', '').strip()
#         coupon = coupon_service.get_active_coupon_by_code(code)

#         if coupon:
#             request.session['applied_coupon'] = coupon.code
#             messages.success(request, f"Coupon '{coupon.code}' applied: {coupon.discount_percent}% off")
#         else:
#             request.session.pop('applied_coupon', None)
#             messages.error(request, "Invalid or expired coupon code.")

#         return redirect('shop:cart_detail')

# class CouponRemoveView(View):
#     def post(self, request):
#         if request.session.get('applied_coupon'):
#             del request.session['applied_coupon']
#             messages.info(request, "Coupon removed.")
#         else:
#             messages.warning(request, "No coupon was applied.")
#         return redirect('shop:cart_detail')

# class CouponListView(View):
#     def get(self, request):
#         coupons = coupon_service.get_all_active_coupons()
#         return render(request, 'shop/coupon_list.html', {'coupons': coupons})


class CouponApplyView(View):
    def post(self, request):
        try:
            code = request.POST.get('coupon_code', '').strip()

            if not code:
                messages.error(request, "Please enter a coupon code.")
                return redirect('cart_detail')

            coupon = coupon_service.get_active_coupon_by_code(code)

            if coupon:
                request.session['applied_coupon'] = coupon.code
                messages.success(request, f"Coupon '{coupon.code}' applied: {coupon.discount_percent}% off")
            else:
                request.session.pop('applied_coupon', None)
                messages.error(request, "Invalid or expired coupon code.")

        except Exception as e:
            messages.error(request, "Something went wrong while applying the coupon.")
            print(f"[CouponApplyView] Error: {e}")

        return redirect('cart_detail')


class CouponRemoveView(View):
    def post(self, request):
        try:
            if 'applied_coupon' in request.session:
                del request.session['applied_coupon']
                messages.info(request, "Coupon removed.")
            else:
                messages.warning(request, "No coupon was applied.")
        except Exception as e:
            messages.error(request, "Something went wrong while removing the coupon.")
            print(f"[CouponRemoveView] Error: {e}")

        return redirect('cart_detail')


class CouponListView(View):
    def get(self, request):
        try:
            coupons = coupon_service.get_all_active_coupons()
            return render(request, 'coupon/coupon_list.html', {'coupons': coupons})
        except Exception as e:
            print(f"[CouponListView] Error: {e}")
            messages.error(request, "Unable to load coupons.")
            return render(request, 'coupon/coupon_list.html', {'coupons': []})

