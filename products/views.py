from django.db.models import Q
from typing import Any
from django.shortcuts import redirect, render
from django.views import generic

from orders.models import Customer
from .models import Image,Category,Product,Wishlist
from carts.forms import AddToCartForm

from django.db.models import Q
# Create your views here.

NUMBER_OF_PRODUCT_IN_PAGE = 20
class Homeview(generic.ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    
    
    def get_context_data(self, **kwargs):
        context = super(Homeview, self).get_context_data(**kwargs)
        context['new_products']= Product.objects.select_related('category','discount').prefetch_related('image').all().order_by('-id')[0:10]
        
        return context
    


def list_product_view(request):
    
    if request.method =="POST":
        
        order_method=request.POST['order_by']
        if order_method =="1":
            product_list_sorted=Product.objects.select_related('category','discount').all().order_by('-id')
        elif order_method =="2":
            product_list_sorted=Product.objects.select_related('category','discount').all().order_by('price')
        elif order_method =="3":
            product_list_sorted=Product.objects.select_related('category','discount').all().order_by('-price')
        elif order_method == "4":
            product_list_sorted=Product.objects.prefetch_related('order_item').select_related('category','discount').all().order_by('order_item')
        else:
            product_list_sorted=Product.objects.select_related('category','discount').all()   
    
    else:
        order_method="0"
        product_list_sorted=Product.objects.select_related('category','discount').all()
    
    
    
    
    return render(request,'products/list_product.html',{
        'products':product_list_sorted,
        'selected':order_method
    })
    
    
class ListCategoryView(generic.ListView):
    model = Product
    paginate_by = NUMBER_OF_PRODUCT_IN_PAGE
    template_name = 'products/list_product.html'
    # context_object_name = 'products'
    ordering = ['-price']
    
    def get_context_data(self,*args, **kwargs):
        context = super(ListCategoryView, self).get_context_data(*args,**kwargs)
        # context['products'] = like.objects.all().order_by("-id")
        context['products'] = Product.objects.filter(category=Category.objects.get(id=self.kwargs['pk']))

        
        return context
    

class DeatilProductView(generic.DeleteView):
    model=Product
    template_name='products/detail_product.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        product_obj=Product.objects.select_related('category','discount').prefetch_related('propertes').get(pk=self.kwargs.get('pk'))
        context['images']=product_obj.image.all()
        size_list=[]
        color_list=[]
        for item in product_obj.propertes.all():
            if item.size not in size_list :
                   size_list.append(str(item.size))
                   
            if item.color not in color_list :
                color_list.append(str(item.color))
                
        context['size']=size_list
        context['color']=color_list
        context['form']=AddToCartForm()
        context['related_product']=Product.objects.select_related('category','discount').prefetch_related('propertes').filter(Q(category=product_obj.category ))
        
        return context
    
    
    
    
def search_view(request):
    if request.method == 'POST':
        word=request.POST['search_val']
        products = Product.objects.select_related('category','discount').filter(Q(title__contains=word)|Q(category__title=word))
        return render(request,'products/list_product.html',{'products':products})
    


class WishlistView(generic.ListView):
    model=Wishlist
    template_name='products/wishlist.html'
    def get_context_data(self, **kwargs: Any):
        context= super().get_context_data(**kwargs)
        context['wishlist']=Wishlist.objects.select_related('product','customer').filter(customer=self.request.user.customer)
        return context
    
    
    
    
def add_to_wishlist(request,pk):

    try:
        print('check?......................')
        customer_obj=request.user.customer
        print(customer_obj,'<<<,')
        product_obj=Product.objects.select_related('category').get(id=pk)
        print(product_obj,'<<<,')
        Wishlist.objects.get_or_create(
            product=product_obj,
            customer=customer_obj,
        )
    except Exception as e:
        print(e,'<---------')

    return redirect('wishlist')
    
        


def remove_from_wishlist(request,pk):

    customer_obj=request.user.customer
    product_obj=Product.objects.get(id=pk)
    
    Wishlist.objects.get(
        product=product_obj,
        customer=customer_obj,
    ).delete()

    return redirect('wishlist')