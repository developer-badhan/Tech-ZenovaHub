from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User
from constants import Gender,Role

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    middle_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=True)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    gender = forms.ChoiceField(choices=Gender.choices(), required=False)

    class Meta:
        model = User
        fields = [
            'first_name', 'middle_name', 'last_name',
            'dob', 'email', 'phone', 'gender', 
        ]


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True)
    middle_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=True)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    phone = forms.CharField(max_length=15, required=False)
    gender = forms.ChoiceField(choices=Gender.choices(), required=False)
    fcm_token = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = User
        fields = [
            'first_name', 'middle_name', 'last_name',
            'dob', 'phone', 'gender', 'fcm_token'
        ]
