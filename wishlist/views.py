from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def wishlist(request):
    """ A view to show logged in user's wishlist """

    template = 'wishlist/wishlist.html'
    context = {}
    return render(request, template, context)
    