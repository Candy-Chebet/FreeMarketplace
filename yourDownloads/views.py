from django.shortcuts import render, redirect
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from yourDownloads.models import completedWork
from django.http import Http404
from django.urls import reverse
from . import forms


def All(request):
    title = 'Your completed Work'
    queryset = completedWork.objects.all()
    form = forms.taskSearchForm(request.POST or None)
    
    if request.method == 'POST':
        queryset = completedWork.objects.filter(title__icontains=form['title'].value())
    
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    
    return render(request, "checkoutHome.html", context)


def Checkout(request, completedWork_id=None):
    host = request.get_host()
    try:
        work = completedWork.objects.get(completedWork_id=completedWork_id)
    except completedWork.DoesNotExist:
        # Handle the case where the completedWork with the given ID doesn't exist
        raise Http404("Completed work does not exist")
    
    # Consider error handling if settings.PAYPAL_RECEIVER_EMAIL is missing
    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': work.Amount,  # Ensure This_Job is accessible
        'Job_name': work.title,
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('yourDownloads:payment-success', kwargs={'completedWork_id': completedWork.completedWork_id})}",
        # 'cancel_url': f"http://{host}{reverse('yourDownloads:payment-failed', kwargs={'completedWork_id': completedWork.completedWork_id})}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)
    context = {'work': work, 
               'paypal': paypal_payment
               }
    return render(request, 'checkout.html', context)



def PaymentSuccessful(request, completedWork_id):
    try:
        work = completedWork.objects.get(completedWork_id=completedWork_id)
        return render(request, 'paymentsuccess.html', {'work': work})
    except work.DoesNotExist:
         raise Http404
        


def paymentFailed(request, completedWork_id):
    try:
        work = completedWork.objects.get(completedWork_id=completedWork_id)
        return render(request, 'payment-failed.html', {'work': work})
    except work.DoesNotExist:
         raise Http404