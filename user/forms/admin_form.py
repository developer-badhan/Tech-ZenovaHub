from django import forms
from user.models import User
from constants import Gender

class AdminUserForm(forms.ModelForm):
    profile_photo = forms.ImageField(max_length=200, required=False)
    first_name = forms.CharField(max_length=50, required=True)
    middle_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=True)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    gender = forms.ChoiceField(choices=Gender.choices(), required=False)
    is_active = forms.BooleanField(required=False)
    is_staff = forms.BooleanField(required=False)
    is_superuser = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = [
            'profile_photo', 'first_name', 'middle_name', 'last_name',
            'dob', 'email', 'phone', 'gender', 'is_active', 
             'is_staff', 'is_superuser'
        ]

    def __init__(self, *args, **kwargs):
        super(AdminUserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter first name'})
        self.fields['middle_name'].widget.attrs.update({'placeholder': 'Enter middle name | Optional'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter last name'})
        self.fields['dob'].widget.attrs.update({'placeholder': 'Enter date of birth'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter email'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Enter phone number'})
        self.fields['gender'].widget.attrs.update({'placeholder': 'Select gender'})
        self.fields['is_active'].initial = True
        self.fields['is_staff'].initial = False
        self.fields['is_superuser'].initial = False
