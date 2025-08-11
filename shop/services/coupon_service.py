from shop.models import Coupon
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

def get_active_coupon_by_code(code):
    try:
        coupon = Coupon.objects.get(code__iexact=code.strip(), active=True)
        now = timezone.now()

        if coupon.valid_from <= now <= coupon.valid_to:
            return coupon
        else:
            print(f"Coupon '{code}' is expired or not yet active.")
            return None
    except ObjectDoesNotExist:
        print(f"Coupon code '{code}' does not exist.")
        return None
    except Exception as e:
        print(f"Error fetching coupon '{code}': {e}")
        return None

def get_all_active_coupons():
    try:
        now = timezone.now()
        return Coupon.objects.filter(active=True, valid_from__lte=now, valid_to__gte=now).order_by('-created_at')
    except Exception as e:
        print(f"Error fetching active coupons: {e}")
        return []

def create_coupon(code, discount_percent, valid_from, valid_to, active=True):
    try:
        coupon = Coupon.objects.create(
            code=code.strip(),
            discount_percent=discount_percent,
            valid_from=valid_from,
            valid_to=valid_to,
            active=active
        )
        return coupon
    except Exception as e:
        print(f"Error creating coupon: {e}")
        return None

def deactivate_coupon(code):
    try:
        coupon = Coupon.objects.get(code__iexact=code.strip())
        coupon.active = False
        coupon.save()
        return True
    except ObjectDoesNotExist:
        print(f"Coupon '{code}' not found.")
        return False
    except Exception as e:
        print(f"Error deactivating coupon '{code}': {e}")
        return False