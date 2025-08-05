from django import forms
from user.models import User
from constants import Gender,Role


class UserRegistrationForm(forms.ModelForm):
    profile_photo = forms.ImageField(max_length=200, required=False)
    first_name = forms.CharField(max_length=50, required=True)
    middle_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=True)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    gender = forms.ChoiceField(choices=Gender.choices(), required=False)
    role = forms.ChoiceField(choices=[
        (Role.ENDUSER_CUSTOMER, "Customer"),
        (Role.ENDUSER_STAFF, "Delivery Staff")
    ], required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
        required=True,
        label='Password'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
        required=True,
        label='Confirm Password'
    )

    class Meta:
        model = User
        fields = [
            'profile_photo', 'first_name', 'middle_name', 'last_name',
            'dob', 'email', 'phone', 'gender', 'role',
            'password', 'confirm_password'
        ]

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter the first name'})
        self.fields['middle_name'].widget.attrs.update({'placeholder': 'Enter the middle name | Optional'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter the last name'})
        self.fields['dob'].widget.attrs.update({'placeholder': 'Enter the date of birth'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter the email'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Enter the phone number'})

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data



class UserUpdateForm(forms.ModelForm):
    profile_photo = forms.ImageField(max_length=200,required=False)
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

    def __init__(self,*args, **kwargs):
        super(UserUpdateForm,self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder':'Enter the first name'})
        self.fields['middle_name'].widget.attrs.update({'placeholder':'Enter the middel name | Optional'})
        self.fields['last_name'].widget.attrs.update({'placeholder':'Enter the last name'})
        self.fields['dob'].widget.attrs.update({'placeholder':'Enter the date of birth'})
        self.fields['phone'].widget.attrs.update({'placeholder':'Enter the phone number'})
