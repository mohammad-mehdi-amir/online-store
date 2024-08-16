from .models import *
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from orders.models import order_item
from django.db.models import Count,Sum,F,Q
from django.utils.translation import gettext as _
class PropertyInline(admin.TabularInline):
    model = Property
    extra = 0
    


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['first_img', 'title', 'price', 'category', 'number','num_sell']
    list_select_related = ['category']
    list_prefetch_related = ('propertes','image')
    list_filter = ['datetime_add',]
    list_display_links = ['first_img', 'title']
    search_fields = ['title',]
    inlines = [PropertyInline]
    autocomplete_fields = ['image', 'category']
    actions=['update_to_posted']
    # prepopulated_fields={
    #     'slg':['title',]
    # }

    def category(self, product: Product):
        return product.category.title

    @admin.display(description='عکس محصول')
    def first_img(self, product: Product):
        
        f_img = product.image.first().image.url
        return format_html('<img src="{}" style="max-width:100px; max-height:100px ; border-radius: 20%;"/>'.format(f_img))
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(number_sell=Sum(F('order_item__quantity'),filter=Q(order_item__order__peyment_status=True)))

        
       
        return queryset
    
    
    @admin.display( description='تعداد موجودی')
    def number(self, product_obj: Product):
        pro = product_obj.propertes.all()
        return sum(item.number for item in pro)
       
    
    

    @admin.display(description='تعداد فروش تا حالا',ordering='number_sell')
    def num_sell(self,proudct:Product):
        return proudct.number_sell

class ProductInline(admin.StackedInline):
    
    model = Product
    extra = 0
    can_delete = False


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['title', 'number']
    inlines = [ProductInline]
    search_fields = ['title']

    @admin.display(ordering='products__id', description='تعداد محصولات کل این دسته')
    def number(self, category: Category):
        url = (reverse("admin:products_product_changelist")
               + '?'
               + urlencode({
                   'category__id': category.id,
               })
               )
        return format_html('<a href="{}">{} </a>', url, category.products.count())


# @admin.register(Property)
# class PropertyAdmin(ModelAdmin):
#     list_display = ['product', 'size', 'number']
#     model = Property
#     search_fields = ['product__title', 'size', ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px; border-radius: 20%;"/>'.format(obj.image.url))

    list_display = ['image_tag', 'title']
    search_fields = ['title']


@admin.register(slide)
class slideAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px; border-radius: 20%;"/>'.format(obj.image.url))

    list_display = ['image_tag', 'title','category']
    



@admin.register(Discount)
class DiscountAdmin(ModelAdmin):
    pass

@admin.register(Wishlist)
class WishlistAdmin(ModelAdmin):
    list_display=['product','user']
    
    
@admin.register(Color)
class ColorAdmin(ModelAdmin):
    pass