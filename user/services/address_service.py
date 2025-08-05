from django.shortcuts import get_object_or_404
from user.models import Address

def create_address(user, data):
    if data.get('is_default'):
        Address.objects.filter(user=user, is_default=True).update(is_default=False)
    return Address.objects.create(user=user, **data)

def update_address(address, data):
    if data.get('is_default'):
        Address.objects.filter(user=address.user, is_default=True).exclude(id=address.id).update(is_default=False)
    for field, value in data.items():
        setattr(address, field, value)
    address.save()
    return address

def get_user_addresses(user):
    return Address.objects.filter(user=user)


def get_address_by_id(address_id):
    return get_object_or_404(Address, pk=address_id)
