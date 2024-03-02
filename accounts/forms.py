
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customuser
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from allauth.account.forms import LoginForm

from django.utils.translation import gettext_lazy as _



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Customuser
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Customuser
        fields = (
            'first_name',
            'last_name',
            "email",
            "username",
            'phone_number',
        )


class ChangeInfoForm(forms.Form):
    first_name=forms.CharField(help_text=_(' '))
    last_name=forms.CharField(help_text=_(''))
    username=forms.CharField(help_text=_(''))
    email=forms.EmailField(help_text=_(''))
    phone_number=PhoneNumberField(region="IR",help_text=_('phone number'))