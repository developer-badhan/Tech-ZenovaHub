from datetime import datetime
from django.utils import timezone
from shop.models import Coupon
from user import models

def get_all_coupons():
    return Coupon.objects.all()

def create_coupon(code, discount_percent, valid_from, valid_to, usage_limit, created_by):
    valid_from = timezone.make_aware(datetime.strptime(valid_from, "%Y-%m-%d %H:%M"))
    valid_to = timezone.make_aware(datetime.strptime(valid_to, "%Y-%m-%d %H:%M"))
    discount_percent = float(discount_percent)

    if Coupon.objects.filter(code=code).exists():
        raise ValueError("Coupon code already exists.")

    coupon = Coupon.objects.create(
        code=code,
        discount_percent=discount_percent,
        valid_from=valid_from,
        valid_to=valid_to,
        usage_limit=usage_limit,
        created_by=created_by
    )
    return coupon


def update_coupon(coupon_id, code, discount_percent, valid_from, valid_to, usage_limit):
    try:
        coupon = Coupon.objects.get(id=coupon_id)
        coupon.code = code
        coupon.discount_percent = float(discount_percent)
        coupon.valid_from = timezone.make_aware(datetime.strptime(valid_from, "%Y-%m-%d %H:%M"))
        coupon.valid_to = timezone.make_aware(datetime.strptime(valid_to, "%Y-%m-%d %H:%M"))
        coupon.usage_limit = usage_limit
        coupon.save()
        return coupon
    except Coupon.DoesNotExist:
        raise ValueError("Coupon not found.")



def delete_coupon(coupon_id):
    try:
        coupon = Coupon.objects.get(id=coupon_id)
        coupon.delete()
    except Coupon.DoesNotExist:
        raise ValueError("Coupon not found.")


def apply_coupon(user, coupon_code):
    try:
        coupon = Coupon.objects.get(code=coupon_code, active=True)
        now = timezone.now()
        if coupon.valid_from <= now <= coupon.valid_to:
            if coupon.used_count < coupon.usage_limit:
                if user in coupon.used_by.all():
                    raise ValueError("You have already used this coupon.")
                coupon.used_count += 1
                coupon.used_by.add(user)
                coupon.save()
                return coupon.discount_percent
            else:
                raise ValueError("Coupon usage limit reached.")
        else:
            raise ValueError("Coupon is not valid.")
    except Coupon.DoesNotExist:
        raise ValueError("Invalid coupon code.")



def get_coupons_assigned_to_user(user):
    return Coupon.objects.filter(used_by=user)
