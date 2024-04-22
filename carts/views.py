from django.shortcuts import render, get_object_or_404, redirect
from carts.cart import Cart
from .forms import AddToCartForm
from products.models import Product,Wishlist,Property
from orders.models import order
from django.contrib import messages
from django.utils.translation import gettext as _


# Create your views here.


def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item['form'] = AddToCartForm(initial={
            'product': item['product'],
            'quantity': item['quantity'],
            'color': item['color'],
            'size': item['size'],
            'inplace': True,
        })

    return render(request, 'carts/cart_detail.html', {
        'cart': cart
    })


def add_to_cart_view(request, product_id):

    if request.method == 'POST':
        cart = Cart(request)
        Product1 = get_object_or_404(Product, id=product_id)

        form = AddToCartForm(request.POST)
        try:
            if form.is_valid():
                if Product1.status == True:
                    claened_date = form.cleaned_data
                    quaintity = claened_date['quantity']
                    size1 = claened_date['size']
                    color1 = claened_date['color']
                    add_or_replace = claened_date['inplace']
                    cart.add(Product1, quantites=quaintity, size=size1,
                            color=color1, add_or_replace=add_or_replace)
                    if add_or_replace == 'on':
                        messages.success(request, Product1.title + _(' updated successfuly'))
                    else:
                        messages.success(request, Product1.title + _(' added to cart successfuly'))
                    return redirect('carts:cart_detail')
                else:
                    raise Product.DoesNotExist
        except Product.DoesNotExist:
            messages.warning(request, Product1.title +'موجودی به اتمام رسیده است')
            return redirect('product_detail',product_id)
        except Property.DoesNotExist:
            messages.warning(request, Product1.title +f' موجودی در رنگ{color1} و سایز {size1} به اتمام رسیده است')
            return redirect('product_detail',product_id)
            
            
        

def remove_cart(request, product,color,size):
    cart = Cart(request)
    Product_obj = get_object_or_404(Product, id=int(product))
    product_id=Product_obj.id

    cart.remove(product_id,color,size)

    messages.warning(request, Product_obj.title +
                   _(' remove form cart successfully'))
    return redirect('carts:cart_detail')


def clean_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('carts:cart_detail')



