from django.db import models

class Order(models.Model):
    photo = models.ImageField(upload_to='photos')
    message = models.TextField()
