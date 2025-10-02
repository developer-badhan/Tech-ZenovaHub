from django import forms
from user.models import User


# Admin form for adding users
class AdminUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(required=True)
    is_active = forms.BooleanField(required=False)


    class Meta:
        model = User
        fields = [
            'first_name', 'last_name',
            'dob', 'email', 'is_active'
        ]

    def __init__(self, *args, **kwargs):
        super(AdminUserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter first name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter last name'})
        self.fields['dob'].widget.attrs.update({'placeholder': 'Enter date of birth'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter email'})
        self.fields['is_active'].initial = True


# Admin form for updating users
class AdminUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'dob', 'email', 'is_active']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(AdminUserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter first name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter last name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter email'})
