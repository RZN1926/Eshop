from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)
    price = models.IntegerField()
    qty = models.IntegerField(default = 0)

class Customer(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField(null = True, blank = True)
    sex = models.CharField(max_length = 20)
