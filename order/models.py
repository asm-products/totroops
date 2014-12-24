from django.db import models
from django.contrib.auth.models import User


class Coupon(models.Model):
    code = models.CharField(max_length=50)
    discount = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    valid = models.BooleanField()


class Item(models.Model):
    name = models.CharField(max_length=50)
    source = models.TextField()
    cost = models.FloatField()
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    food = models.BooleanField(default=False)


class Package(models.Model):
    items = models.ManyToManyField('Item')
    cost = models.FloatField()
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    container = models.TextField()
    shipping = models.FloatField()
    price = models.FloatField()
    tax = models.FloatField()


class Recipient(models.Model):
    name = models.TextField()
    address = models.TextField()


class Order(models.Model):
    customer = models.ForeignKey(User, blank=True, null=True)
    recipient= models.ForeignKey(Recipient, blank=False, null=False)
    packages = models.ManyToManyField('Package')
    coupon = models.ForeignKey(Coupon, blank=True, null=True)
    message = models.TextField(max_length=500, blank=True, null=True)
    image_url = models.CharField(max_length=1000, blank=True, null=True)

    @property
    def total_price(self):
        """
        Takes the sum of prices of all packages
        :rtype: float
        :return: Sum of price of all packages
        """
        total = 0;
        for package in self.packages:
            total += package.price
        print type(total)
        return total


