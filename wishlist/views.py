from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from profiles.models import UserProfile
from wishlist.models import Wishlist, WishlistItem
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
    
    redirect_url = request.POST.get('redirect_url')
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.get_or_create(user=user)
    wishlist_user = wishlist[0]

    product = Product.objects.get(pk=item_id)
    if request.POST:
        test = WishlistItem.objects.filter(wishlist=wishlist_user, product=product).exists()
        if test:
            messages.error(request, "Product already in your wishlist")
            return redirect(redirect_url)

        else:
            added_item = WishlistItem(wishlist=wishlist_user, product=product, date_added=timezone.now())
            added_item.save()
            messages.success(request, "Product added to your wishlist")
            return redirect(redirect_url)
    else:
        messages.error(request, "Click 'Add to wishlist' to add a item ")
        return render(request, 'home/index.html')

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
def delete_wishlist(request, wishlist_item_id):
    """ Delete a wishlist item from the wishlist """

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = get_object_or_404(Wishlist, pk=wishlist_item_id, user=user)
    wishlist.delete()
    messages.success(request, 'Item deleted from your wishlist!')
    return redirect(reverse('wishlist'))
