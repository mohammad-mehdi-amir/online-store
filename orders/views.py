from typing import Any
from django.shortcuts import redirect, render
from .forms import AddOrderForm
from carts.cart import Cart
from.models import order_item
from .models import Province
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from . models import order,Shiping_price
from products.models import Product

@login_required
def order_create(request):
    cart=Cart(request)
    order_form=AddOrderForm()
    
    if request.method == 'POST':

        order_form=AddOrderForm(request.POST)
        
        if order_form.is_valid():
            if len(cart)!=0:
                SHIPING_PRICE=Shiping_price.objects.get().shiping_price
                
                
                order_obj =order_form.save(commit=False)
                order_obj.user=request.user
                order_obj.phone_number=order_form.cleaned_data['phone_number']
                order_obj.total_price=cart.get_total_price()+SHIPING_PRICE
                order_obj.save()
                try:
                    for item in cart:
                        pro=Product.objects.get(id=item['product_object'])
                        order_item.objects.create(
                            order=order_obj,
                            product=Product.objects.get(id=pro.id),
                            size=item['size'],
                            color=item['color'],
                            quantity=item['quantity'],
                            price=pro.price,
                            total_price=item['total_price']
                        )
                    
                    
                    request.session['order_id'] = order_obj.id
                    return redirect('peyment_request')
                
                
                except Exception as e:
                   
                    messages.error(request,_('please try again'))
                    last_order_info=1
            else:
                messages.error(request,_('your cart is empty'))
                last_order_info=1
                  
        else:
            
            messages.error(request,_('your order has not been registered, please try again'))
            last_order_info=1
    else:
        order_form=AddOrderForm()
        if request.user.orders.exists():
            last_order = request.user.orders.last()
            last_order_info = last_order  # You can access the order fields directly


        else:
            last_order_info=1
    
    
    return render(request,'orders/order_create.html',{
        'form':order_form,
        'province':Province.objects.all(),
        'customer':request.user,
        'order_info':last_order_info

    })

from django.views import generic
class OrderListView(generic.ListView):
    model=order
    template_name='orders/order_list.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context['orders']=order.objects.prefetch_related('items').filter(user=self.request.user.id).order_by('-datetime_order')
        return context
        


        