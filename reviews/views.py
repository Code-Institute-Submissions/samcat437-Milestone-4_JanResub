from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile, Product, Reviews
from .forms import ReviewForm


@login_required
def reviews(request):
    """ A view to return the reviews on a given product"""
    review = get_object_or_404(Reviews, user=UserProfile.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been saved.')
        else:
            messages.error(request, 'Your review submission failed. Please ensure the form is valid.')

    template = 'reviews/review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def add_review(request):
    """ A view to add an review to the user's wishlist """
    if request.method == 'POST':
        user_id = request.user
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)