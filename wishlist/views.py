from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import UserProfile
from .models import Wishlist, WishlistItem

from products.models import Product


@login_required
def wishlist(request):
    """ A view to show logged in user's wishlist """
     
    items = []
    user = get_object_or_404(UserProfile, user=request.user)
    print(user)
    wishlists = Wishlist.objects.filter(user=user)
    print(wishlists)
    for a in wishlists:
        print(a.products)

    context = {
        'wishlist_items': wishlists,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, item_id):
    """ A view to add an item to the user's wishlist """

    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    in_wishlist = WishlistItem.objects.filter(product=product).exists()

    if in_wishlist:
        messages.info(request, f'This product already exists in your wishlist.')
    else:
        user_wishlist = Wishlist.objects.create(user=user)
        user_wishlist.products.add(product)
        user_wishlist.save()
        messages.success(request, f'Added {product.name} to your wishlist')

    return redirect(redirect_url)
