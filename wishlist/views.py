from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile

from products.models import Product
@login_required
def wishlist(request):
    """ A view to show logged in user's wishlist """
    # products = []
    # profile = get_object_or_404(UserProfile, user=request.user)

    # template = 'wishlist/wishlist.html'
    # context = {
    #     'wishlist': wishlist,
    # }
    return render(request, 'wishlist/wishlist.html')


@login_required
def add_to_wishlist(request, item_id):
    """ A view to add an item to the user's wishlist """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    if item_id in list(wishlist.keys()):
        messages.success(request, f'This product already exists in your wishlist.')
    else:
        messages.success(request, f'Added {product.name} to your wishlist')

    request.session['wishlist'] = wishlist
    print(request.session['wishlist'])
    return redirect(redirect_url)