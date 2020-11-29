from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Quantity, Thicknes
from .forms import DesignForm

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
    quantities = Quantity.objects.all()
    thickness = Thicknes.objects.all()

    context = {
        'product': product,
        'quantities': quantities,
        'thickness': thickness,
    }

    return render(request, 'design_detail.html', context)


@login_required
def add_design(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = DesignForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added design!')
            return redirect(reverse('add_design'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = DesignForm()

    template = 'add_design.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def update_design(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('index'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = DesignForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('design_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = DesignForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'update_design.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_design(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('index'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Design deleted!')
    return redirect(reverse('design'))
