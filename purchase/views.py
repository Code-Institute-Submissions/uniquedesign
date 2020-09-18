from django.shortcuts import render, redirect
from decimal import Decimal

# Create your views here.


def purchase(request):

    return render(request, 'purchase.html')


def add_purchase(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    purchase = request.session.get('purchase', {})

    if item_id in list(purchase.keys()):
        purchase[item_id] += quantity
    else:
        purchase[item_id] = quantity

    request.session['purchase'] = purchase
    print(request.session['purchase'])
    return redirect(redirect_url)
