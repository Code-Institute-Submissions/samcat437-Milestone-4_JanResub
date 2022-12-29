from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Reviews(models.Model):
    class Meta:
        verbose_name_plural = "Reviews"
        
    user = models.ForeignKey(UserProfile, null=False, blank=False, on_delete=models.CASCADE, related_name='review')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    review = models.TextField(max_length=1000, null=True, blank=False)

    def __str__(self):
        return str(self.product)
