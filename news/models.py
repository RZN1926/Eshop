from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length = 50)
    article = models.CharField(max_length = 50)
    views = models.IntegerField(default = 0)
