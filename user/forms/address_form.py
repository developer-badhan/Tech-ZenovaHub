from django import forms
from user.models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'address_line1', 'address_line2',
            'city', 'state', 'postal_code',
            'country', 'is_default',
        ]

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields['address_line1'].widget.attrs.update({'placeholder': 'Primary address'})
        self.fields['address_line2'].widget.attrs.update({'placeholder': 'Secondary address (optional)'})
        self.fields['city'].widget.attrs.update({'placeholder': 'City'})
        self.fields['state'].widget.attrs.update({'placeholder': 'State / Region'})
        self.fields['postal_code'].widget.attrs.update({'placeholder': 'ZIP / Postal Code'})
        self.fields['country'].widget.attrs.update({'placeholder': 'Country'})
