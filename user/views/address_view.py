from django.views import View
from django.shortcuts import render, redirect
from decorators.auth_decorators import signin_required
from user.forms import AddressForm
from user.services import enduser_service, address_service
from constants import Role
from user.models import Address


# ────── CREATE ADDRESS ──────

class AddressCreateView(View):
    @signin_required
    def get(self, request, user_id):
        if request.session.get('user_id') != user_id:
            return redirect('user_login')

        user = enduser_service.get_user_by_id(user_id)
        form = AddressForm()
        return render(request, 'address/address_form.html', {'form': form, 'user': user})

    @signin_required
    def post(self, request, user_id):
        if request.session.get('user_id') != user_id:
            return redirect('user_login')

        user = enduser_service.get_user_by_id(user_id)
        form = AddressForm(request.POST)
        if form.is_valid():
            address_service.create_address(user, form.cleaned_data)
            role = request.session.get('user_role')
            if role == Role.ENDUSER_CUSTOMER:
                return redirect('customer_dashboard')
            elif role == Role.ENDUSER_STAFF:
                return redirect('staff_dashboard')

        return render(request, 'address/address_form.html', {'form': form, 'user': user})


# ────── LIST USER ADDRESSES ──────

class AddressListView(View):
    @signin_required
    def get(self, request, user_id):
        if request.session.get('user_id') != user_id:
            return redirect('user_login')

        user = enduser_service.get_user_by_id(user_id)
        addresses = address_service.get_user_addresses(user)
        return render(request, 'address/address_list.html', {'addresses': addresses})


# ────── UPDATE ADDRESS ──────

class AddressUpdateView(View):
    @signin_required
    def get(self, request, user_id, address_id):
        if request.session.get('user_id') != user_id:
            return redirect('user_login')

        address = address_service.get_address_by_id(address_id)
        if address.user.id != user_id:
            return redirect('user_login')

        form = AddressForm(instance=address)
        return render(request, 'address/address_update.html', {'form': form, 'address': address})

@signin_required
def post(self, request, user_id, address_id):
    if request.session.get('user_id') != user_id:
        return redirect('user_login')

    address = address_service.get_address_by_id(address_id)
    if address.user.id != user_id:
        return redirect('user_login')

    form = AddressForm(request.POST, instance=address)
    if form.is_valid():
        address_service.update_address(address, form.cleaned_data)

        role = request.session.get('user_role')
        if role == Role.ENDUSER_CUSTOMER:
            return redirect('customer_dashboard')
        elif role == Role.ENDUSER_STAFF:
            return redirect('staff_dashboard')

    return render(request, 'address/address_update.html', {'form': form, 'address': address})

    



