from django import forms
from .models import order


class AddOrderForm(forms.ModelForm):
    class Meta:
        model = order
        fields = ('first_name','last_name','province','city','address','postal_code','order_note','total_price')
