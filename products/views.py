from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from reviews.models import Reviews
from profiles.models import UserProfile
from .forms import ProductForm
from reviews.forms import ReviewForm
from checkout.models import Order, OrderLineItem


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
           
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
           
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details, generate product review or form to fill out review """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Reviews.objects.filter(product=product_id)
    no_reviews = True

    if request.user.is_anonymous:
        if reviews:
            no_reviews = False
    context = {
            'product': product,
            'no_reviews': no_reviews,
            'review_items': reviews
    }

    return render(request, 'products/product_detail.html', context)

    if request.user:
        user = get_object_or_404(UserProfile, user=request.user)
        user_orders = Order.objects.filter(user_profile=user)
        orders = Order.objects.filter(user_profile=user).exists()
        # order(s) for that item 
        order = OrderLineItem.objects.filter(product=product_id)

        for user_order in user_orders:
            for o in order:
                if str(user_order) in str(o):
                    orders = True
                else:
                    orders = False

        # reviews for the product of any user
        reviews = Reviews.objects.filter(product=product_id)
        # review(s) of any user
        reviewed = reviews.filter(product=product_id).exists()
        # if the review for user logged in exists
        this_review = reviews.filter(user=user).exists()

        no_reviews = True
        if reviewed:
            no_reviews = False

        if this_review:
            orders = False
            no_reviews = False
            if orders is True:
                no_reviews = False

        if no_reviews is True:
            orders = False
   
        if request.method == 'POST':
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

        context = {
            'form': form,
            'product': product,
            'review_items': reviews,
            'order_match': orders,
            'already_reviewed': this_review,
            'no_reviews': no_reviews
        }

        return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
       
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))