from ast import mod
from os import name
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from jalali_date.fields import JalaliDateTimeField
from products.models import Property,Product
from solo.models import SingletonModel
from django.shortcuts import redirect, render
class Shiping_price(SingletonModel):
    shiping_price=models.PositiveIntegerField( default=45000)
    def __str__(self):
        return str(self.shiping_price)
    class Meta:
        verbose_name = "تغییر هزینه پست و بسته بندی"





class Province(models.Model):
    name=models.CharField(max_length=70)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural ='استان ها'

# class Address(models.Model):
#     customer=models.Forginkey(Customer,on_delete=models.CASECADE,related_name='address')
#     province=models.OneToOneField(Province,on_delete=models.CASCADE)
#     city=models.CharField(max_length=50)
#     address=models.CharField(max_length=200)
#     postal_code=models.CharField(max_length=10)
    
    
    
    
class order(models.Model):


    ORDER_OPTIONS = [
    ('در انتظار تایید', 'در انتظار تایید'),
    ( 'در حال آماده سازی', 'در حال آماده سازی'),
    ( 'ارسال شده', 'ارسال شده')
]

    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='orders',null=True,verbose_name=_('customer :'))
    phone_number=PhoneNumberField(verbose_name=_('phone number :'))
    first_name=models.CharField(max_length=30,verbose_name=_('First Name :'))
    last_name=models.CharField(max_length=30,verbose_name=_('Last Name :'))
    
    
    
    province=models.ForeignKey(Province,on_delete=models.CASCADE,null=True,related_name='orders',verbose_name=_('province :'))
    city=models.CharField(max_length=50,verbose_name=_('city :'))
    address=models.CharField(max_length=150,verbose_name=_('address :'))
    postal_code=models.CharField(max_length=10,verbose_name=_('postal code :'),null=True,blank=True)
    
    
    datetime_order=models.DateTimeField(auto_now_add=True)
    datetime_order_modified=models.DateTimeField(auto_now=True)
    
    
    # is_payed=models.BooleanField(default=False)
    peyment_status=models.BooleanField(default=False,verbose_name=_('peyment_status :'))
    order_status =models.CharField(max_length=50,choices=ORDER_OPTIONS,null=True,default='در انتظار تایید',verbose_name=_('order_status :'))
    
    order_note=models.TextField(blank=True,verbose_name=_('Do You Have Any Note For This Order?'))
    
    
    total_price=models.PositiveIntegerField(null=True,blank=True,verbose_name=_('total order price:'))

    zarinpal_authority = models.CharField(max_length=225,blank=True,verbose_name=_(' zarinpal authority code:'))
    class NotEnoughException(Exception):
        def __init__(self, number):
            self.number = number

    
    
    
    
    def __str__(self):
        return f'{self.id} {self.first_name} {self.last_name}'
    class Meta:
        verbose_name_plural ='سفارشات'
    
    
    

class order_item(models.Model):
    order=models.ForeignKey(order,on_delete=models.CASCADE,related_name='items')
    
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_item',null=True,blank=True)
    
    size=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    
    price=models.PositiveIntegerField()
    
    quantity=models.PositiveIntegerField(default=1)
    
    total_price=models.PositiveIntegerField()

    
    def __str__(self):
        return f'{self.product} for order {self.order}'
    
    
    
# order/models.py

from django.db import models

class EmailQueue(models.Model):
    email = models.EmailField(verbose_name="ایمیل")
    ready_to_send = models.BooleanField(default=False, verbose_name="آماده برای ارسال")

    def __str__(self):
        return self.email

    