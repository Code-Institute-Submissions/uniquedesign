from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from payment.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile) # save form data to form variable
        if form.is_valid(): # checking form validity
            form.save()
            messages.success(request, 'Profile updated successfully') # sucess message
        else:
            messages.success(request, 'Update failed. Please endsure the form is Valid') # error message
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)
    template = 'profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'payment_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
