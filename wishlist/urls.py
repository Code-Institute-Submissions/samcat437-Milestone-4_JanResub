from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add/<item_id>', views.add_to_wishlist, name='add_to_wishlist'),
    path('delete/<item_id>', views.delete_wishlist, name='delete_wishlist'),
]