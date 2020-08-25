from django.shortcuts import render
from .models import Product, Category

# Create your views here.


def readymade(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'readymade.html', context)
