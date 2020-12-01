from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from design.models import Product, Quantity, Thicknes
from purchase.contexts import purchase_items


# Create your views here.

def purchase(request):

    current_purchase = purchase_items(request)
    p_name = current_purchase["p_name"]

    context = {
        'p_name': p_name
    }
    return render(request, 'purchase.html', context)


def add_purchase(request, item_id):

    product = Product.objects.get(pk=item_id) # save data to product variable from Product model
    quantity_price = int(request.POST.get('quantity_price')) # save value to variable from quantity_price id field
    thickness_price = int(request.POST.get('thickness_price')) # save value to variable from thicknes_price id field
    proprice = int(request.POST.get('proprice')) # save value to variable from proprice id field
    redirect_url = request.POST.get('redirect_url')
    purchase = request.session.get('purchase', {}) # get purchase session and stored in to purchase variable

    if item_id in list(purchase.keys()):
        purchase[item_id] = quantity_price + thickness_price + proprice
        messages.success(request, f'Added {product.name} to your Purchase list')
    else:
        purchase[item_id] = quantity_price + thickness_price + proprice
        messages.success(request, f'Added {product.name} to your Purchase list')

    request.session['purchase'] = purchase

    return redirect(redirect_url)


def edit_purchase(request, item_id):
    """Edit purchase"""
    product = get_object_or_404(Product, pk=item_id)
    quantities = Quantity.objects.all()
    thickness = Thicknes.objects.all()

    context = {
        'product': product,
        'quantities': quantities,
        'thickness': thickness,
    }

    return render(request, 'edit_purchase.html', context)


def remove_purchase(request, item_id):
    """Remove purchase"""
    product = Product.objects.get(pk=item_id)
    purchase = request.session.get('purchase', {})

    if item_id:
        del purchase[item_id]
        messages.warning(request, f'{product.name} has been removed from your Purchase list')
    else:
        del purchase[item_id]
        messages.warning(request, f'{product.name} has been removed from your Purchase list')

    request.session['purchase'] = purchase

    return redirect(reverse('purchase'))
