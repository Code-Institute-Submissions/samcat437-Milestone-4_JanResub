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

    return redirect(redirect_url)