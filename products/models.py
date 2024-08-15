from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.html import format_html
from phonenumber_field.modelfields import PhoneNumberField
from typing import Any
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth import get_user_model

class Image(models.Model):
    image = models.ImageField(upload_to='product_img')
    title = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.title
    # def __call__(self):
    #     return format_html('<img src="{}" style="max-width:50px; max-height:50px"/>'.format(self.image.url))
    class Meta:
        verbose_name_plural='تصاویر محصولات'


class Discount(models.Model):
    name=models.CharField(max_length=90)
    discount=models.FloatField()
    
    def __str__(self):
        return str(self.discount)
    class Meta:
        verbose_name_plural='تخفیف ها'

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_img')
    discount=models.ForeignKey(Discount,on_delete=models.DO_NOTHING,related_name='categores',null=True,blank=True)
    

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='دسته بندی ها'
    def get_absolute_url(self):
        
        return reverse('category_list', kwargs={'pk': self.id})


class slide(models.Model):
    image=models.ImageField(upload_to='slide_img')
    title = models.CharField(max_length=60, blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='slides',null=True,blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='اسلاید های صفحه اصلی'
    

class Product(models.Model):
    title = models.CharField(max_length=120,verbose_name=_('name :'))
    price = models.IntegerField(verbose_name=_('price :'))
    # slg=models.SlugField(max_length=200,unique=True,allow_unicode=True)
    # slg1=models.SlugField(max_length=200,allow_unicode=True,db_collation='utf8_persian_ci')
    status = models.BooleanField(default=True,verbose_name=_('status'))
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.PROTECT,verbose_name=_('category :'))

    discount=models.ForeignKey(Discount,on_delete=models.DO_NOTHING,related_name='products',null=True,blank=True,verbose_name=_('discount'))
    
    
    
    datetime_add = models.DateTimeField(auto_now_add=True,verbose_name=_(' add date'))
    datetime_edit = models.DateTimeField(auto_now=True,verbose_name=_('edite date'))

    image = models.ManyToManyField(Image, related_name='images',verbose_name=_('images :'))

    material=models.CharField(max_length=70,blank=True,verbose_name=_('material :'))
    des=RichTextField(blank=True,null=True,verbose_name=_(' decription :'))
    
    

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='محصولات'


    def get_absolute_url(self):

        return reverse('product_detail', kwargs={'pk': self.id})

class Color(models.Model):
    color1=models.CharField(max_length=90,verbose_name=_(' color'),primary_key=True)
    def __str__(self):
        return self.color1
    
    class Meta:
         verbose_name_plural='رنگ ها'
class Property(models.Model):

    OPTIONS = [
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("2XL", "2X"),
        ("3XL", "3XL"),
        ("4XL", "4XL"),
        ("5XL", "5XL"),
        ("30", "30"),
        ("31", "31"),
        ("32", "32"),
        ("33", "33"),
        ("34", "34"),
        ("35", "35"),
        ("36", "36"),
        ("36", "36"),
        ("37", "37"),
        ("38", "38"),
        ("39", "39"),
        ("40", "40"),
        ("41", "41"),
        ("42", "42"),
        ("43", "43"),
        ("44", "44"),
        ("45", "45"),
        ("46", "46"),
        ("36", "36"),
        ("47", "47"),
        ("48", "48"),
        ("49", "49"),
        ("48", "48"),
        ("49", "49"),
        ("50", "50"),
    ]
    COLORS = [('سفید','سفید'),('سفید-استخونی','سفید-استخونی'),('سفید-شیری','سفید-شیری'),('مشکی','مشکی'),('زرد','زرد'),('سبز','سبز'),('قرمز','قرمز'),('آبی','آبی'),('زیتونی','زیتونی'),('سبز-سدری','سبز-سدری'),('بنفش','بنفش'),('صورتی','صورتی'),('خاکستری','خاکستری'),('نقره-ای','تقره-ای'),('قهوه-ای','قهوه-ای'),('سبز-کله-غازی','سبز-کله-غازی'),('خردلی','خردلی'),('ابی-یخی','ابی-یخی'),('ذغالی','ذغالی'),('زرشکی','زرشکی'),('شتری','شتری'),('یاسی','یاسی'),('سورمه-ای','سورمه-ای'),('سبز-لجنی','سبز-لجنی')]
    product = models.ForeignKey(
        Product, related_name='propertes', blank=True, null=True, on_delete=models.CASCADE,verbose_name=_('product :'))
    size = models.CharField(max_length=10, choices=OPTIONS, blank=True,verbose_name=_('size'))
    color1 = models.ForeignKey(Color,on_delete=models.DO_NOTHING,blank=True,null=True)
    number = models.PositiveIntegerField(_('number :'),default=1)

    def __str__(self) -> str:
        return f'{self.product.title}-{self.size}-{self.color1}'




class Wishlist(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='wishlists',verbose_name=_('customer :'))
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='wishlists',verbose_name=_('product :'))
    