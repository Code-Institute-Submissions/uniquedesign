from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def payment(request):
    purchase = request.session.get('purchase', {})
    if not purchase:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('design'))

    order_form = OrderForm()
    template = 'payment.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
