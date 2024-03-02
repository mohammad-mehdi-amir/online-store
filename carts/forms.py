from django import forms
from products.models import Property
class AddToCartForm(forms.Form):
    QUANTITY_CHOICES=[(i,str(i)) for i in range(1,6)]
    color=forms.CharField(required=False)
    size=forms.CharField(required=False)
    quantity=forms.TypedChoiceField(choices=QUANTITY_CHOICES,coerce=int)
    inplace=forms.CharField(required=False,widget=forms.HiddenInput)