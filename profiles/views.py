from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile
from reviews.models import Reviews
from wishlist.models import Wishlist, WishlistItem
from products.models import Product
from .forms import UserProfileForm
from checkout.models import Order, OrderLineItem


@login_required
def profile(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)
    user = get_object_or_404(UserProfile, user=request.user)
    review = Reviews.objects.filter(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.'
            )
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    wishlist = Wishlist.objects.get_or_create(user=user)

    wishlist_exists = Wishlist.objects.filter(user=user).exists()
    wishlistitems_exist = (
        WishlistItem.objects.filter(wishlist=wishlist[0]).exists()
    )
  
    if wishlist_exists:
        if wishlistitems_exist:
            wishlist_items = Product.objects.filter(wishlist=wishlist[0])
            template = 'profiles/profile.html'
            context = {
                'form': form,
                'orders': orders,
                'on_profile_page': True,
                'review_items': review,
                'wishlist_items': wishlist_items,
                'products': wishlist_items
            }
            return render(request, template, context)
        else:
            template = 'profiles/profile.html'
            context = {
                'form': form,
                'orders': orders,
                'on_profile_page': True,
                'review_items': review,
                'wishlist_items': False
            }
            return render(request, template, context)
     

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
