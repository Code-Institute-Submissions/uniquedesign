from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from design.models import Product


def purchase_items(request):

    items = []
    total = 0
    product_count = 0
    p_name = request.POST.get('p_name')
    orgname = request.POST.get('orgname')
    address = request.POST.get('address')
    email = request.POST.get('email')
    cnumber = request.POST.get('cnumber')

    purchase = request.session.get('purchase', {})

    for item_id, quantity in purchase.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity
        pro_total = quantity - product.price
        product_count = quantity
        items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'pro_total': pro_total,
        })

    if total >= settings.FREE_DELIVERY_THRESHOLD:
        delivery = 0
        free_delivery_delta = 0
    elif total == 0:
        delivery = 0
        free_delivery_delta = 0
    else:
        delivery = Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total

    grand_total = delivery + total

    context = {
        'items': items,
        'total': total,
        'purchase': purchase,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'p_name': p_name,
        'orgname': orgname,
        'address': address,
        'email': email,
        'cnumber': cnumber,
    }

    return context
