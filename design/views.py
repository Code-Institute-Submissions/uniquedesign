from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Quantity, Thicknes

# Create your views here.


def design(request):

    products = Product.objects.all()
    quantity = Quantity.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any search criteria")
                return redirect(reverse('design'))

            queries = Q(name__icontains=query) | Q(info__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'quantity': quantity,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'design.html', context)


def design_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    quantity = get_object_or_404(Quantity, pk=product_id)
    thicknes = get_object_or_404(Thicknes, pk=product_id)
    products = Product.objects.all()
    quantities = Quantity.objects.all()
    thickness = Thicknes.objects.all()

    context = {
        'product': product,
        'products': products,
        'quantity': quantity,
        'quantities': quantities,
        'thickness': thickness,
        'thicknes': thicknes,
    }

    return render(request, 'design_detail.html', context)
