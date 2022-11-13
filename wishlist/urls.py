from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add/<item_id>', views.add_to_wishlist, name='add_to_wishlist'),
    path('delete/<wishlist_item_id>', views.delete_wishlist, name='delete_wishlist'),
    path('confirmation/<item_id>/', views.delete_wishlist_confirmation, name='delete_wishlist_confirmation'),
]
