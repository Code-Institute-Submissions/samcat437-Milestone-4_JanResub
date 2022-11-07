from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import UserProfile
from wishlist.models import Wishlist
from products.models import Product


@login_required
def wishlist(request):
    """ A view to return the wishlist page """

    return render(request, 'wishlist/wishlist.html')


@login_required
def add_to_wishlist(request, item_id):
    """A view to add an item to the wishlist database"""
    
    user = get_object_or_404(UserProfile, user=request.user) 
    product = get_object_or_404(Product, pk=item_id) 
    redirect_url = request.POST.get('redirect_url')
    in_wishlist = Wishlist.objects.filter(product=product, user=user).exists()
    wishlist_exists = Wishlist.objects.filter(user=user).exists()

    if in_wishlist:
        messages.info(request, f'This product already exists in your wishlist.')
    else:
        if wishlist_exists:
            Wishlist.save(product)
            messages.success(request, f'Added {product.name} to your wishlist')
        else:
            user_wishlist = Wishlist.objects.create(product=product, user=user)
            Wishlist.save(product)
            messages.success(request, f'Added {product.name} to your wishlist')

    return redirect(redirect_url)