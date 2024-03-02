from .models import Product, Image, Category, Property,Discount,Wishlist,Color
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from orders.models import order_item
from django.db.models import Count,Sum
class PropertyInline(admin.TabularInline):
    '''Tabular Inline View for Property'''

    model = Property
    extra = 0
    can_delete = False


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['first_img', 'title', 'price', 'category', 'number', 'id','num_sell']
    list_select_related = ['category']
    list_filter = ['datetime_add',]
    list_display_links = ['first_img', 'title']
    search_fields = ['title',]
    inlines = [PropertyInline]
    autocomplete_fields = ['image', 'category']

    def category(self, product: Product):
        return product.category.title

    @admin.display( description='#number of item')
    def number(self, product_obj: Product):
        pro = Property
        all_pro = pro.objects.filter(product=product_obj)
        sum = 0
        for item in all_pro:
            sum += item.number
        return sum
    
    def first_img(self, product: Product):
        images = product.image
        f_img = images.first().image.url
        return format_html('<img src="{}" style="max-width:100px; max-height:100px ; border-radius: 20%;"/>'.format(f_img))
    
    @admin.display(description='number of sells')
    def num_sell(self,proudct:Product):

        
        q=Product.objects.get(id=proudct.id).order_item.aggregate(Sum('quantity'))
    
        
            
        return 0 if q['quantity__sum'] == None else q['quantity__sum']
        


class ProductInline(admin.StackedInline):

    model = Product
    extra = 0
    can_delete = False


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['title', 'number']
    inlines = [ProductInline]
    search_fields = ['title']

    @admin.display(ordering='products__id', description='number of product')
    def number(self, category: Category):
        url = (reverse("admin:products_product_changelist")
               + '?'
               + urlencode({
                   'category__id': category.id,
               })
               )
        return format_html('<a href="{}">{} </a>', url, category.products.count())


@admin.register(Property)
class PropertyAdmin(ModelAdmin):
    list_display = ['product', 'size', 'number']
    model = Property
    search_fields = ['product__title', 'size', ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px; border-radius: 20%;"/>'.format(obj.image.url))

    list_display = ['image_tag', 'title']
    search_fields = ['title']


@admin.register(Discount)
class DiscountAdmin(ModelAdmin):
    pass

@admin.register(Wishlist)
class WishlistAdmin(ModelAdmin):
    list_display=['product','customer']
    
    
@admin.register(Color)
class ColorAdmin(ModelAdmin):
    pass