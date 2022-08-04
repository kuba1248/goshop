from django.db import models
from django.contrib.auth.models import User

from product.models import Product


# Create your models here.
class Review(models.Model):
    author = models.ForeignKey(User, related_name='views', on_delete=models.CASCADE)
    text = models.TextField()
    product = models.ForeignKey(Product, related_name='views', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])

    def __str__(self):
        return self.author