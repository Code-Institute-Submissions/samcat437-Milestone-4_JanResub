from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Product


def reviews(request):
    """ A view to return the reviews on a given product"""

    return render(request, 'reviews/review.html')


@login_required
def add_review(request):
    """ A view to add an item to the user's wishlist """

    return render(request, 'reviews/add_review.html')
