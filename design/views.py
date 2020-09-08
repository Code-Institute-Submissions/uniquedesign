from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def design(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'design.html', context)


def design_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'design_detail.html', context)
