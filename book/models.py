from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    book_status = [
        ('available', 'available'),
        ('rented', 'rented'),
        ('sold', 'sold'),
    ]
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=50, null=True, blank=True)
    book_image = models.ImageField(upload_to='images', null=True, blank=True)
    author_image = models.ImageField(upload_to='images', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    price_for_rent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rent_period = models.IntegerField(null=True, blank=True)
    total_rented_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=book_status)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
