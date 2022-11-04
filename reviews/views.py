from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Product
from .forms import ReviewForm


@login_required
def reviews(request):
    """ A view to return the reviews on a given product"""

    return render(request, 'reviews/review.html')


@login_required
def add_review(request):
    """ A view to add an review to the user's wishlist """
    if request.method == 'POST':
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