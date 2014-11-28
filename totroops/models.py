from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=50)
    source = models.TextField()
    cost = models.FloatField()
    weight = models.FloatField()
    height = models.FloatField()
    length = models.FloatField()
    width = models.FloatField()
    food = models.BooleanField()


class Package(models.Model):
    items = models.ManyToManyField('Item')
    cost = models.FloatField()
    weight = models.FloatField()
    height = models.FloatField()
    length = models.FloatField()
    width = models.FloatField()
    container = models.TextField()
    shipping = models.FloatField()
    price = models.FloatField()
    tax = models.FloatField()


class Order(models.Model):
    customer = models.ForeignKey(User, blank=False, null=False)
    destination = models.TextField()
    packages = models.ManyToManyField('Package')

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
