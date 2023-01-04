from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
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
    wishlist_exists = Wishlist.objects.filter(user=user).exists()
    wishlist_owner = wishlist[0]
    wishlistitems_exist = WishlistItem.objects.filter(wishlist=wishlist_owner).exists()

    if wishlist_exists:       
        items = Product.objects.filter(wishlist=wishlist_owner)

        template = 'wishlist/wishlist.html'
        context = {
            'wishlist_items': True,
            'products': items
        }
        return render(request, template, context)
    
    else:
        context = {
            'wishlist_items': False,
        }
    
    print(wishlist_exists)
    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, item_id):
    """A view to add an item to the wishlist database"""

    redirect_url = request.POST.get('redirect_url')
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.get_or_create(user=user)
    wishlist_owner = wishlist[0]

    product = Product.objects.get(pk=item_id)
    if request.POST:
        wishlist_exists = WishlistItem.objects.filter(wishlist=wishlist_owner, product=product).exists()
        if wishlist_exists:
            messages.error(request, "This product already exists in your wishlist")
            return redirect(redirect_url)

        else:
            new_item = WishlistItem(wishlist=wishlist_owner, product=product, date_added=timezone.now())
            new_item.save()
            messages.success(request, "Product added to your wishlist")
            return redirect(redirect_url)
    else:
        messages.error(request, "Click 'Add to wishlist' to add a item ")
        return render(request, 'home/index.html')

    return redirect(redirect_url)


@login_required
def delete_wishlist_confirmation(request, item_id):
    """ Ask the user to confirm deletion of an item from their wishlist via template """

    product = get_object_or_404(Product, pk=item_id)
    template = 'wishlist/confirmation.html'
    context = {
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_wishlist(request, item_id):
    """ Delete a wishlist item from the wishlist """

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.get_or_create(user=user)
    wishlist_owner = wishlist[0]
    item = get_object_or_404(Product, pk=item_id)
    product = WishlistItem.objects.get(product=item)
    products = get_list_or_404(WishlistItem, wishlist=wishlist_owner)
    product_number = len(products)
    
    product.delete()
    messages.success(request, 'Item deleted from your wishlist!')
    return redirect(reverse('wishlist'))
