
from django.conf import settings
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.shortcuts import render
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

from products.models import Category
from .models import order,order_item,Province,EmailQueue
from solo.admin import SingletonModelAdmin
from orders.models import Shiping_price
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	
from django.utils.translation import gettext as _


admin.site.register(Shiping_price, SingletonModelAdmin)

class orderInLine(admin.TabularInline):
    readonly_fields=['order','product','size','color','quantity','price','total_price']
    model=order_item
    fields=['order','product','size','color','quantity','price']
    extra=0
    min_num=1


@admin.register(order)
class orderAdmin(ModelAdmin):
    list_display=['first_name','last_name','province','city','order_status','peyment_status','get_created_jalali']
    inlines=[
        orderInLine,
    ]
    list_select_related=['province']
    autocomplete_fields=['province','user']
    list_filter=['order_status','datetime_order','peyment_status']
    list_editable=['order_status']
    actions=['update_to_posted','update_to_pre','print_post_label']
    readonly_fields=['peyment_status']
  
    
    @admin.display(description='تاریخ سفارش', ordering='datetime_order')
    def get_created_jalali(self, obj):
	    return datetime2jalali(obj.datetime_order).strftime('%Y/%m/%d %H:%M:%S')
 
 
    @admin.action(description=_('update status orders to  POSTED'))
    def update_to_posted(self,request,queryset):
        u_c=queryset.update(order_status='ارسال شده')
        self.message_user(
            request,
            f' وضعیت {u_c} سفارش به حالت ارسال شده بروزرسانی شد'
        )
    @admin.action(description='بروزرسانی وضعیت سفارشات به در حال آماده سازی')
    def update_to_pre(self,request,queryset):
        u_c=queryset.update(order_status='در حال آماده سازی')
        self.message_user(
            request,
            f' وضعیت {u_c} سفارش به در "حال آماده سازی" بروزرسانی شد'
        )
    @admin.action(description='لیبل های سفارشات ')
    def print_post_label(self,request,queryset):
      
        return render(request,'orders/post_labels.html',context={
        'query':queryset
    })
@admin.register(order_item)
class Orderitem(ModelAdmin):
    list_display=['product','size','color','price','quantity','order_link']

    autocomplete_fields=['product']

    @admin.display(ordering='customer__id')
    def order_link(self,order_item:order_item):
        url=(reverse("admin:orders_order_changelist")
             +'?'
             + urlencode({
                 'order__id':order_item.id,
             })
             )
        return format_html('<a href="{}">{} </a>',url,order_item.order)
    
    
    
    
@admin.register(Province)
class ProvinceAdmin(ModelAdmin):
    list_display=['name']
    search_fields=['name']
    
# class customerOrderInline(admin.StackedInline):
#     readonly_fields=['first_name','last_name','province','city','order_status','peyment_status','datetime_order']
#     model=order
#     extra=0
# @admin.register(Customer)
# class CustomerAdmin(ModelAdmin):
    
#     user_model=settings.AUTH_USER_MODEL
#     inlines=[
#         customerOrderInline,
#     ]
#     list_select_related=['user']
#     list_display=['user','first_name','last_name','email']
#     search_fields=['user__username','phone_number','user__email']
#     @admin.display(ordering='user__first_name')
#     def first_name(self,customer:Customer):
#         return customer.user.first_name
#     @admin.display(ordering='user__last_name')
#     def last_name(self,customer:Customer):
#         return customer.user.last_name
#     @admin.display(ordering='user__email')
#     def email(self,customer:Customer):
#         return customer.user.email

@admin.register(EmailQueue)
class EmailQueueAdmin(admin.ModelAdmin):
    list_display = ('email', 'ready_to_send')  # نمایش فیلدها در لیست
    list_filter = ('ready_to_send',)  # امکان فیلتر کردن براساس آماده بودن
    search_fields = ('email',)  # امکان جستجو بر اساس ایمیل
    actions = ['mark_as_ready', 'send_emails']  # اضافه کردن اکشن‌ها
