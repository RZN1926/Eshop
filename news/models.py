from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewsCategory(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(verbose_name = 'Описание', null = True, blank = False)

    def __str__(self):
        return self.name



class News(models.Model):
    title = models.CharField(max_length = 50)
    article = models.TextField()
    views = models.IntegerField(default = 0)
    user_views = models.ManyToManyField(
        to = User,
        blank = True)
    category = models.ForeignKey(
        to = NewsCategory,
        on_delete = models.SET_NULL,
        null = True, blank = True,
        verbose_name = 'Категория')

    
    def __str__(self):
        return self.title
    
    