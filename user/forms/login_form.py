from django import forms


# Form for end-user login
class EndUserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(EndUserLoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter the email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter the password'})
