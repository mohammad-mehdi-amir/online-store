
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
    first_name=forms.CharField(help_text=_(''))
    last_name=forms.CharField(help_text=_(''))
    username=forms.CharField(help_text=_(''))
    email=forms.EmailField(help_text=_(''))
    phone_number=PhoneNumberField(region="IR",help_text=_('phone number'))
    
    
    
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    phone_number=PhoneNumberField(region="IR",help_text=_('phone number'))
    def save(self, request):
        try:
            user= super(CustomSignupForm,self).save(request)
            print('pass1')
            user.phone_number = self.cleaned_data['phone_number']
            print('pass2')
            user.save()
            print('pass3')
            return user
        except Exception as e:
            print(self.cleaned_data['phone_number'],'>-----------')
            print(e,'<--------')
    