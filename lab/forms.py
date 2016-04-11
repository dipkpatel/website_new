# Import Django's form module.
from django import forms


class RegistrationForm(forms.Form):
    """
    A class to represent our registration form, using Django's forms module.

    If we define our "form" nicely here, Django can generate our <input> tags
    automatically in the template, and validate the user's input.
    """
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    
    email = forms.EmailField() 
    password = forms.CharField(widget=forms.PasswordInput(), max_length=64)


class AuthenticationForm(forms.Form):
    """
    A class to represent our sign-in form.

    Works similarly to the registration form.
    """
    email = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=64)
