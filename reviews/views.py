from django.shortcuts import render


def reviews(request):
    """ A view to return the reviews on a given product"""

    return render(request, 'reviews/review.html')