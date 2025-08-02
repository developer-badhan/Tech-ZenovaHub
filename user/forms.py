from django import forms
from user.models import User
from constants import Gender

class UserRegistrationForm(forms.ModelForm):
    profile_photo = forms.URLField(max_length=200,required=False)
    first_name = forms.CharField(max_length=50,required=True)
    middle_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=True)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    gender = forms.ChoiceField(choices=Gender.choices(), required=False)

    class Meta:
        model = User
        fields = [
              'profile_photo', 'first_name', 'middle_name', 'last_name',
            'dob', 'email', 'phone', 'gender',
        ]


class UserUpdateForm(forms.ModelForm):
    profile_photo = forms.URLField(max_length=200,required=False)
    first_name = forms.CharField(max_length=50, required=True)
    middle_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=True)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    phone = forms.CharField(max_length=15, required=False)
    gender = forms.ChoiceField(choices=Gender.choices(), required=False)

    class Meta:
        model = User
        fields = [
            'profile_photo','first_name', 'middle_name', 'last_name',
            'dob', 'phone', 'gender', 
        ]

