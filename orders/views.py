from typing import Any
from django.shortcuts import redirect, render
from .forms import AddOrderForm
from carts.cart import Cart
from.models import order_item
from .models import Province
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from . models import order
from products.models import Product
@login_required
def order_create(request):
    cart=Cart(request)
    order_form=AddOrderForm()
    
    if request.method == 'POST':

        order_form=AddOrderForm(request.POST)
        
        if order_form.is_valid():
            if len(cart)!=0:
                
                order_obj =order_form.save(commit=False)
                order_obj.customer=request.user.customer
                order_obj.total_price=cart.get_total_price()
                order_obj.save()
                try:

                    for item in cart:
                        
                        order_item.objects.create(
                            order=order_obj,
                            product=Product.objects.get(id=int(item['product_object'].id)),
                            size=item['size'],
                            color=item['color'],
                            quantity=item['quantity'],
                            price=item['product_object'].price,
                            total_price=item['total_price']
                        )
                    
                    
                    request.session['order_id'] = order_obj.id
                    return redirect('peyment_request')
                
                
                except Exception as e:
                    print(e,'-------------------------------')
                    messages.error(request,_('please try again'))
            else:
                messages.error(request,_('your cart is empty'))
                
                
            
        else:

            messages.error(request,_('your order has not been registered, please try again'))
    else:
        order_form=AddOrderForm()
    
    
    return render(request,'orders/order_create.html',{
        'form':order_form,
        'province':Province.objects.all(),
        'customer':request.user.customer,

    })

from django.views import generic
class OrderListView(generic.ListView):
    model=order
    template_name='orders/order_list.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context['orders']=order.objects.prefetch_related('items').filter(customer=self.request.user.customer.id)
        return context
        
    