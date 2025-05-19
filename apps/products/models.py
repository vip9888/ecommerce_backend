from django.db import models

# Create your models here.
# this is the model for the category of the product
# it is used to create a category for the product
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.name


# this is the model for the product
# it is used to create a product
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name