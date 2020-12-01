from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from django.views.decorators.http import require_POST
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderItem
from design.models import Product
from purchase.contexts import purchase_items
import stripe
import json


@require_POST
def cache_payment_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0] # request client secret key
        stripe.api_key = settings.STRIPE_SECRET_KEY # storing stripe key to the variable
        stripe.PaymentIntent.modify(pid, metadata={
            'purchase': json.dumps(request.session.get('purchase', {})), # request session from purchase
            'save_info': request.POST.get('save_info'), # save info for save_info variable
            'username': request.user, # svae user in to username variable
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def payment(request):
    # save keys to variable
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        purchase = request.session.get('purchase', {})

        # save field datat to variable
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            'phone_number': request.POST['phone_number'],
        }
        order_form = OrderForm(form_data) # save from data to order_form variable
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0] # save client secret key to pid
            order.stripe_pid = pid # save pid to variable
            order.original_purchase = json.dumps(purchase)
            order.save()
            for item_id, item_data in purchase.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_item = OrderItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_item.save()
                    else:
                        for item_id, quantity in item_data:
                            order_item = OrderItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                item_id=item_id,
                            )
                            order_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('purchase'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('payment_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        purchase = request.session.get('purchase', {})

    if not purchase:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('design'))

    current_purchase = purchase_items(request)
    total = current_purchase['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.user.get_full_name(),
                'email': profile.user.email,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'town_or_city': profile.default_town_or_city,
                'county': profile.default_county,
                'postcode': profile.default_postcode,
                'country': profile.default_country,
                'phone_number': profile.default_phone_number,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'payment.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def payment_success(request, order_number):
    """
    Handle successful payment
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_town_or_city': order.town_or_city,
                'default_county': order.county,
                'default_postcode': order.postcode,
                'default_country': order.country,
                'default_phone_number': order.phone_number,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        eMail will be sent to {order.email}.')

    if 'purchase' in request.session:
        del request.session['purchase']

    template = 'payment_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
