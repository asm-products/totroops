from django.db import models


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
