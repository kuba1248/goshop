from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    statusy = (
        ('exists', 'Exists'),
        ('ordered', 'Ordered'),
        ('delivered', 'Delivered'),
        ('returned', 'Returned'),
        ('confirmed', 'Confirmed'),

    )
    categories = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField()
    statusy = models.CharField(max_length=25, choices=statusy, null=True)

    def __str__(self):
        return self.title