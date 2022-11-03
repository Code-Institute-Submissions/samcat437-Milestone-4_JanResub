from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Product(models.Model):
    product = models.CharField(max_length=50)


class Wishlist(models.Model):
    """
    A user's list of wished-for items
    """
    user = models.ForeignKey(UserProfile, null=False, blank=False, on_delete=models.CASCADE, related_name='wishlist')
    products = models.ManyToManyField(Product, through='WishlistItem', through_fields=('wishlist', 'product'),)
	
    def __str__(self):
        return f'Wishlist ({self.user})'


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, null=False, blank=False, on_delete=models.CASCADE, related_name='wishlist_items')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name='wishlist_products')
    date_added = models.DateTimeField(auto_now_add=True)
	
    def __str__(self):
        return self.product.name
    