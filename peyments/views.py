from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.conf import settings
import requests
import json
from carts.cart import Cart

from orders.models import order,order_item
from products.models import Property


# ? sandbox merchant
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'


ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"


# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/peyment/verify/'


def send_request(request):
    order_id = request.session.get('order_id')
    # Get the order object
    order_obj = get_object_or_404(order, id=order_id)

    toman_total_price = order_obj.total_price
    rial_total_price = toman_total_price * 10

    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": toman_total_price,
        "Description": f'#{order_obj.id}: {order_obj.customer.user.first_name} {order_obj.customer.user.last_name}',
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

                messages.warning(request,'پرداخت با موفقت انجام نشد')
                order_obj.peyment_status='cancel'
                order_obj.save()
                return render(request,'404.html',{"title":'پرداخت با موفقت انجام نشد'})
        return JsonResponse(response)

    except requests.exceptions.Timeout:
        return JsonResponse({'status': False, 'code': 'timeout'})
    except requests.exceptions.ConnectionError:
        return JsonResponse({'status': False, 'code': 'connection error'})


def verify(request):
    order_id = request.session.get('order_id')
    order_obj = get_object_or_404(order, id=order_id)
    
    toman_total_price = order_obj.total_price
    rial_total_price = toman_total_price * 10
    
    
    
    authority = request.GET.get('Authority')
    data = {
        "MerchantID": settings.MERCHANT,
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
                order_obj.peyment_status='peyed'
                order_obj.save()
                
                cart=Cart(request)
                for item in cart:
                    property_obj=Property.objects.get(product=int(item['product']),color=item['color'],size=item['size'])
                    property_obj.number-=item['quantity']
                    property_obj.save()

                cart.clear()
                messages.success(request,'پرداخت شما با موفقیت به پایان رسید و سفارش شما ثبت گردید')
                return redirect('order_list')
            elif response['Status'] == 100:
                messages.warning(request,'این سفارش قبلا پرداخت و ثبت گردیده است٬ میتوانید آنرا در داشبور خود مشاهده کنید')
                return redirect('order_list')
            else:
                messages.warning(request,f'پرداخت با موفقت انجام نشد کد {response["Status"]}')
                order_obj.peyment_status='cancel'
                order_obj.save()
                return render(request,'404.html',{"title":f'پرداخت با موفقت انجام نشد کد {response["Status"]}'})
            

    except requests.exceptions.Timeout:
        order_obj.peyment_status='cancel'
        order_obj.save()
        return JsonResponse({'status': False, 'code': 'timeout'})
    except requests.exceptions.ConnectionError:
        messages.warning(request,'گذر از زمان مجاز')
        order_obj.peyment_status='cancel'
        order_obj.save()
        return render(request,'404.html',{"title":'گذر از زمان مجاز'})
    except Exception as e:
        messages.warning(request,'خطای برقرای ارتباط')
        order_obj.peyment_status='cancel'
        order_obj.save()
        return render(request,'404.html',{"title":'خطای برقرای ارتباط'})


