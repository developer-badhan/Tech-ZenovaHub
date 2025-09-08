from django import forms


# Form for requesting an OTP
class OTPRequestForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email"
        })
    )

# Form for verifying the OTP
class OTPVerifyForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email"
        })
    )
    otp_code = forms.CharField(max_length=6,required=True,widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter 6-digit OTP"
        })
    )

# Form for resending the OTP
class OTPResendForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email"
        })
    )

