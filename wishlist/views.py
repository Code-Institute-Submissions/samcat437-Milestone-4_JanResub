from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import UserProfile
from wishlist.models import Wishlist
from products.models import Product


@login_required
def wishlist(request):
    """ A view to return the wishlist page """

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.filter(user=user)

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist_items': wishlist,
    }
    
    return render(request, template, context)


@login_required
def add_to_wishlist(request, item_id):
    """A view to add an item to the wishlist database"""
    
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    in_wishlist = Wishlist.objects.filter(product=product, user=user).exists()

    if in_wishlist:
        messages.info(request, f'This product already exists in your wishlist.')
    else:
        new_wishlist = Wishlist(user=user, product=product)
        Wishlist.save(new_wishlist)
        Wishlist.save(product)
        messages.success(request, f'Added {product.name} to your wishlist')

    return redirect(redirect_url)


@login_required
def delete_wishlist_confirmation(request, item_id):
    """ Ask the user to confirm deletion of an item from their wishlist via template """

    wishlist_item = get_object_or_404(Wishlist, pk=item_id)
    template = 'wishlist/confirmation.html'
    context = {
        'wishlist_item': wishlist_item,
    }

    return render(request, template, context)



@login_required
def delete_wishlist(request, item_id):
    """ Delete a wishlist item from the wishlist """

    wishlist = get_object_or_404(Wishlist, pk=item_id)
    wishlist.delete()
    messages.success(request, 'Item deleted from your wishlist!')
    return redirect(reverse('wishlist'))
