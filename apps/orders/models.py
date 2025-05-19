from django.db import models
from django.contrib.auth.models import User
from apps.products.models import Product

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    
    # this is used to return the order id and the username whenever we call the order object, by doing this we can see something rather then the object address
    # this is called string representation of the model
    # this is used in the admin panel
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # this is used to return the order item id and the product name whenever we call the order item object, by doing this we can see something rather then the object address
    # this is called string representation of the model
    # this is used in the admin panel   
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in order {self.order.id}"
