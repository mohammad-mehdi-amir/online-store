from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
import requests
import json
from carts.cart import Cart

from orders.models import order,order_item
# from orders.tasks import send_order_email
from orders.tasks import send_order_email
from products.models import Property




ZP_API_REQUEST = f"https://www.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://www.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://www.zarinpal.com/pg/StartPay/"


# Important: need to edit for realy server.
CallbackURL = 'http://toronto7.com/peyment/verify/'


def send_request(request):
    order_id = request.session.get('order_id')
    # Get the order object
    order_obj = get_object_or_404(order, id=order_id)

    toman_total_price = order_obj.total_price
    

    data = {
        "MerchantID": "b1754af4-49ed-411a-8d40-e3ae3dfd638f",
        "Amount": toman_total_price,
        "Description": f'#{order_obj.id}: {order_obj.user.first_name} {order_obj.user.last_name}',
        # "Phone": phone,
        "CallbackURL": CallbackURL,
    }

    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json',
               'content-length': str(len(data))}
    try:
        response = requests.post(
            ZP_API_REQUEST, data=data, headers=headers, timeout=10)

        if response.status_code == 200:

            response = response.json()
            if response['Status'] == 100:

                return redirect(ZP_API_STARTPAY + str(response['Authority']))
            else:

                messages.warning(request,'پرداخت با موفقیت انجام نشد')
                order_obj.peyment_status='canceled'
                order_obj.save()
                return render(request,'404.html',{"title":'پرداخت با موفقیت انجام نشد'})
        return JsonResponse(response)

    except requests.exceptions.Timeout:
        order_obj.peyment_status='canceled'
        order_obj.save()
        return JsonResponse({'status': False, 'code': 'گذر از زمان مجاز'})
    except requests.exceptions.ConnectionError:
        messages.warning(request,'گذر از زمان مجاز')
        order_obj.peyment_status='canceled'
        order_obj.save()
        return render(request,'404.html',{"title":'خظا در برقراری ارتباط'})
    except Exception as e:
        
        messages.warning(request,'خطای ناشناخته')
        order_obj.peyment_status='canceled'
        order_obj.save()
        return render(request,'404.html',{"title":'خطای ناشناخته'})


def verify(request):
    order_id = request.session.get('order_id')
    order_obj = get_object_or_404(order, id=order_id)
    
    toman_total_price = order_obj.total_price
    rial_total_price = toman_total_price * 10
    
    
    
    authority = request.GET.get('Authority')
    data = {
        "MerchantID":"b1754af4-49ed-411a-8d40-e3ae3dfd638f",
        "Amount": toman_total_price,
        "Authority": authority,
    }
    data = json.dumps(data)

    # set content length by data
    headers = {'content-type': 'application/json',
               'content-length': str(len(data))}
    try:
        response = requests.post(ZP_API_VERIFY, data=data, headers=headers)
        if response.status_code == 200:
            
            response = response.json()


            if response['Status'] == 100:
                order_obj.zarinpal_authority = authority
                order_obj.peyment_status=True
                order_obj.save()
                
                cart=Cart(request)
                for item in cart:
                    property_obj=Property.objects.get(product=int(item['product']),color=item['color'],size=item['size'])
                    property_obj.number-=item['quantity']
                    property_obj.save()

                cart.clear()
                messages.success(request,'پرداخت شما با موفقیت به پایان رسید و سفارش شما ثبت گردید')
                order_link = f"http://toronto7.com{reverse('admin:orders_order_change', args=[order_obj.id])}"
                send_order_email.delay(order_link,order_obj.id)
                  
                
                return redirect('order_list')
            
            else:
                messages.warning(request,f'پرداخت با موفقت انجام نشد کد {response["Status"]}')
                order_obj.delete()
               
                return redirect('home') 
            

    except requests.exceptions.Timeout:
        order_obj.peyment_status='canceled'
        order_obj.save()
        return JsonResponse({'status': False, 'code': 'گذر از زمان مجاز'})
    except requests.exceptions.ConnectionError:
        messages.warning(request,'گذر از زمان مجاز')
        order_obj.peyment_status='canceled'
        order_obj.save()
        return render(request,'404.html',{"title":'خظا در برقراری ارتباط'})
    except Exception as e:
        
        messages.warning(request,'خطای ناشناخته')
        order_obj.peyment_status='canceled'
        order_obj.save()
        return render(request,'404.html',{"title":'خطای ناشناخته'})


