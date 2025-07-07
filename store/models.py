from django.db import models
from django.utils import timezone


# Create your models here.


class Collection(models.Model):
    category_name = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Collection, on_delete=models.PROTECT)


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    MEMBERSHIP_CHOICES = models.CharField(
        max_length=1, choices={"G": "Gold", "S": "Silver", "B": "Bronze"}, default="B"
    )


class Order(models.Model):
    payment_status = models.CharField(
        max_length=1,
        choices={"P": "Pending", "C": "Completed", "F": "Failed"},
        defaults="P",
    )
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Cart(models.Model):
    pass

class Item(models.Model):
    ref_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    ref_cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
