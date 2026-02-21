from django.shortcuts import render
import json
import uuid
from decimal import Decimal
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from order.models import Order

import urllib.request


# Create your views here.

def pay(request):
    order_id = request.session.get('current_order_id')
    if not order_id:
        return redirect('index')
    order = Order.objects.get(id=order_id)
    reference = uuid.uuid4().hex
    order.reference = reference
    order.save()
    
    paystack_public_key = settings.PAYSTACK_PUBLIC_KEY
    callback_url = request.build_absolute_uri(reverse('verify'))
    
    amount = int(order.total_amount * Decimal('100'))  # Convert to kobo
    # determine an email to send to Paystack: prefer order.user.email, fall back to request.user
    email = ''
    try:
        email = order.user.email or ''
    except Exception:
        email = request.user.email if request.user.is_authenticated else ''
    
    context = {
        'order': order,
        'reference': reference,
        'amount': amount,
        'email': email,
        'order_id': order_id,
        'paystack_public_key': paystack_public_key,
        'callback_url': callback_url,
    }
    return render(request, 'pay.html', context)

def verify(request):
    reference = request.GET.get('reference')
    if not reference:
        return redirect('index')
    
    headers = {
        'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}',}
    url = f'https://api.paystack.co/transaction/verify/{reference}'
    try: 
        r = request.get(url, headers=headers)
        data = r.json()
        status = data.get('data', {}).get('status')
        amount = data.get('data', {}).get('amount') / 100  # Convert back to Naira  
        
        order = Order.objects.get(reference=reference)
        if status == 'Success' and amount == float(order.total_amount):
            order.status = 'Completed'
            order.save()
            return render(request, 'success.html', {'order': order})
        else:
            order.status = 'Failed'
            order.save()
            return render(request, 'failed.html', {'order': order})
    except Exception :
        try:
            order = Order.objects.get(reference=reference)
            order.status = 'Failed'
            order.save()
        except Exception:
            pass
        return render(request, 'failed.html', {'order': None})