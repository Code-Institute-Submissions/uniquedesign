from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from design.models import Product


def purchase_items(request):

    items = []
    total = 0
    product_count = 0
    purchase = request.session.get('purchase', {})

    for item_id, quantity in purchase.items():
        product = get_object_or_404(Product, pk=item_id)
        print(f"PRICE: {product.price}")
        print(f"QUANTITY: {quantity}")
        print(type(product.price))
        print(type(quantity))
        total += Decimal(quantity) + product.price
        product_count += Decimal(quantity)
        items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total + Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'items': items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
