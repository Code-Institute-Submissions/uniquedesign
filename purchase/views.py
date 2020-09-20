from django.shortcuts import render, redirect

# Create your views here.


def purchase(request):

    return render(request, 'purchase.html')


def add_purchase(request, item_id):

    quantity = int(request.POST.get('quantity_price'))
    thickness = int(request.POST.get('thickness_price'))
    proprice = int(request.POST.get('proprice'))
    redirect_url = request.POST.get('redirect_url')
    purchase = request.session.get('purchase', {})

    if item_id in list(purchase.keys()):
        purchase[item_id] = quantity + thickness + proprice
    else:
        purchase[item_id] = quantity + thickness + proprice

    request.session['purchase'] = purchase
    return redirect(redirect_url)
