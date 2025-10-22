import re
from datetime import datetime
from django.utils import timezone
from shop.models import Coupon


def _normalize_date_str(s: str) -> str:
    """
    Normalize common user inputs:
    - Trim, collapse multiple spaces
    - Uppercase AM/PM
    - Ensure there is a space before AM/PM if the user typed '5:00PM' or '5PM'
    - Remove stray periods (e.g. 'a.m.' -> 'AM')
    """
    if s is None:
        raise ValueError("Date string is required.")
    s = s.strip()
    # collapse multiple spaces
    s = re.sub(r'\s+', ' ', s)
    # remove dots in am/pm (a.m. -> am)
    s = re.sub(r'\bA\.?M\.?\b', 'AM', s, flags=re.IGNORECASE)
    s = re.sub(r'\bP\.?M\.?\b', 'PM', s, flags=re.IGNORECASE)
    s = s.upper()
    # ensure space before AM/PM if missing, e.g. '5:00PM' -> '5:00 PM'
    s = re.sub(r'(?<!\s)(AM|PM)\b', r' \1', s)
    return s


def parse_datetime_with_fallback(date_str):
    """
    Try multiple formats for flexibility:
      - '2025-10-22 14:30'         (24-hour)
      - '2025-10-22 02:30 PM'      (12-hour with space)
      - '2025-10-22 02:30PM'       (12-hour without space)
      - '2025-10-22 2 PM'          (12-hour without minutes)
      - '2025-10-22 02:30:15 PM'   (with seconds)
    Raises ValueError if none match.
    Returns timezone-aware datetime.
    """
    s = _normalize_date_str(date_str)

    # candidate formats (ordered: most common -> fallback)
    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d %I:%M:%S %p",
        "%Y-%m-%d %I:%M %p",
        "%Y-%m-%d %I%p",
        "%Y-%m-%d %I %p",
    ]

    last_err = None
    for fmt in formats:
        try:
            dt = datetime.strptime(s, fmt)
            # make timezone-aware using Django utilities
            return timezone.make_aware(dt)
        except ValueError as e:
            last_err = e
            continue

    # none matched
    raise ValueError(
        "Invalid date/time format. Accepted examples: "
        "'YYYY-MM-DD HH:MM' (24-hour) or 'YYYY-MM-DD h:MM AM/PM' (12-hour)."
    )


# Get all coupons
def get_all_coupons():
    return Coupon.objects.all()


# Create coupon
def create_coupon(code, discount_percent, valid_from, valid_to, usage_limit, created_by):
    # Basic validation: ensure fields are present
    if not code:
        raise ValueError("Coupon code is required.")
    if discount_percent is None or discount_percent == '':
        raise ValueError("Discount percent is required.")
    if not valid_from:
        raise ValueError("Valid from datetime is required.")
    if not valid_to:
        raise ValueError("Valid to datetime is required.")

    valid_from_dt = parse_datetime_with_fallback(valid_from)
    valid_to_dt = parse_datetime_with_fallback(valid_to)
    discount_percent = float(discount_percent)

    if Coupon.objects.filter(code=code).exists():
        raise ValueError("Coupon code already exists.")

    coupon = Coupon.objects.create(
        code=code,
        discount_percent=discount_percent,
        valid_from=valid_from_dt,
        valid_to=valid_to_dt,
        usage_limit=usage_limit,
        created_by=created_by
    )
    return coupon


# Update coupon
def update_coupon(coupon_id, code, discount_percent, valid_from, valid_to, usage_limit):
    try:
        coupon = Coupon.objects.get(id=coupon_id)
    except Coupon.DoesNotExist:
        raise ValueError("Coupon not found.")

    if not code:
        raise ValueError("Coupon code is required.")
    if discount_percent is None or discount_percent == '':
        raise ValueError("Discount percent is required.")
    if not valid_from:
        raise ValueError("Valid from datetime is required.")
    if not valid_to:
        raise ValueError("Valid to datetime is required.")

    coupon.code = code
    coupon.discount_percent = float(discount_percent)
    coupon.valid_from = parse_datetime_with_fallback(valid_from)
    coupon.valid_to = parse_datetime_with_fallback(valid_to)
    coupon.usage_limit = usage_limit
    coupon.save()
    return coupon


# Delete coupon
def delete_coupon(coupon_id):
    try:
        coupon = Coupon.objects.get(id=coupon_id)
        coupon.delete()
    except Coupon.DoesNotExist:
        raise ValueError("Coupon not found.")


# Apply a coupon to a user's order
def apply_coupon(user, coupon_code):
    try:
        coupon = Coupon.objects.get(code=coupon_code, active=True)
    except Coupon.DoesNotExist:
        raise ValueError("Invalid coupon code.")
    now = timezone.now()
    if not (coupon.valid_from <= now <= coupon.valid_to):
        raise ValueError("Coupon is not valid.")
    if coupon.used_count >= coupon.usage_limit:
        raise ValueError("Coupon usage limit reached.")
    if user in coupon.used_by.all():
        raise ValueError("You have already used this coupon.")
    coupon.used_count += 1
    coupon.used_by.add(user)
    coupon.save()
    return coupon.discount_percent


# Get all coupons assigned to a user
def get_coupons_assigned_to_user(user):
    return Coupon.objects.filter(used_by=user)
