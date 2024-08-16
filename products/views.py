from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from typing import Any
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import *
from carts.forms import AddToCartForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count,Sum
from django.db.models import Q
# Create your views here.

NUMBER_OF_PRODUCT_IN_PAGE = 20
class Homeview(generic.ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    
    
    def get_context_data(self, **kwargs):
        context = super(Homeview, self).get_context_data(**kwargs)
        context['new_products']= Product.objects.select_related('category','discount').prefetch_related('image').all().order_by('-id')[0:20]
        # product_list_sorted=Product.objects.select_related('category','discount').all()
        # context['bestsell_products']= sorted(product_list_sorted, key=lambda x: x.order_item.aggregate(quantity_sum=Sum('quantity'))['quantity_sum'] or 0,reverse=True)
        context['slides']=slide.objects.all()
        
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
        elif order_method =="4":
            product_list_sorted=Product.objects.select_related('category','discount').all()
            product_list_sorted = sorted(product_list_sorted, key=lambda x: x.order_item.aggregate(quantity_sum=Sum('quantity'))['quantity_sum'] or 0,reverse=True)
        else:
            product_list_sorted=Product.objects.select_related('category','discount').all()   
    
    else:
        order_method=request.GET.get('order_by')
        product_list_sorted=Product.objects.select_related('category','discount').all()
     # Pagination
    paginator = Paginator(product_list_sorted, 12) # Show number products per page

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    return render(request,'products/list_product.html',{
        'products': products,
        'selected': order_method
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
                   
            if item.color1.color1 not in color_list :
                color_list.append(str(item.color1.color1))
                
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
    

@method_decorator(login_required, name='dispatch')
class WishlistView(generic.ListView):
    model=Wishlist
    
    template_name='products/wishlist.html'
    def get_context_data(self, **kwargs: Any):
        context= super().get_context_data(**kwargs)
        context['wishlist']=Wishlist.objects.select_related('product','user').filter(user=self.request.user)
        return context
    
    
    
    
def add_to_wishlist(request,pk):

    try:

       
        
        product_obj=Product.objects.select_related('category').get(id=pk)
        
        Wishlist.objects.get_or_create(
            product=product_obj,
            user=request.user,
        )
    except Exception as e:
        print(e,'<---------')

    return redirect('wishlist')
    
        


def remove_from_wishlist(request,pk):

    
    product_obj=Product.objects.get(id=pk)
    
    Wishlist.objects.get(
        product=product_obj,
        user=request.user.id,
    ).delete()

    return redirect('wishlist')