from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile, Product, Reviews
from .forms import ReviewForm


@login_required
def reviews(request):
    """ A view to return the reviews on a given product"""
    
    user = get_object_or_404(UserProfile, user=request.user)
    review = Reviews.objects.filter(user=user)
    
    template = 'reviews/review.html'
    context = {
        'review_items': review,
    }

    return render(request, template, context)


@login_required
def add_review(request, item_id):
    """ A view to add an review to the user's wishlist """
    
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=item_id)
    review = Reviews.objects.filter(user=user)
    reviews = Reviews.objects.filter(product=item_id)
    this_review = reviews.filter(user=user).exists()

    if request.method == 'POST':
        user = get_object_or_404(UserProfile, user=request.user)
        new_form = Reviews.objects.filter(user=user)
        user_id = request.user
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.product = product
            new_form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Your review submission failed. Please ensure the form is valid.')
    else:
        form = ReviewForm()
    
    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product,
        'review_items': review,
        'already_reviewed': this_review
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_items_id):
    """" A view to edit a user's review """
    
    user = get_object_or_404(UserProfile, user=request.user)
    review = get_object_or_404(Reviews, pk=review_items_id, user=user)

    if request.method == 'POST':
        user_id = request.user
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            messages.success(request, 'Successfully updated your review!')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Your review update failed. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)

    template = 'reviews/edit_review.html'
    context = {
        'review_items': review,
        'form': form,
    }   

    return render(request, template, context)


@login_required
def delete_review_confirmation(request, item_id):
    """ Ask the user to confirm deletion of an item from their wishlist via template """

    review_item = get_object_or_404(Reviews, pk=item_id)
    template = 'reviews/confirmation.html'
    context = {
        'review_item': review_item,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_items_id):
    """ Delete a review from the site """

    user = get_object_or_404(UserProfile, user=request.user)
    review = get_object_or_404(Reviews, pk=review_items_id, user=user)
    
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('reviews'))
