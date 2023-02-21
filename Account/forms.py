from django import forms
from .models import User

class FormRegistration(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User already exist")
        return email
        
    def clean(self):
        
        password = self.cleaned_data['password']
        if len(password) < 4:
            raise forms.ValidationError("Password length should be greater than 3")
        conform_password = self.cleaned_data['confirm_password']

        if password != conform_password:
            raise forms.ValidationError('Confirm password does not match')

class FormLogIn(forms.Form):
    email = forms.EmailField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput)


    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("User not authorize")
        return email
    

