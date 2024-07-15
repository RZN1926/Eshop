from django.shortcuts import render
from .models import News
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

# Create your views here.

def news(request):
    return render (request, 'news.html', {'news': News.objects.all()})

def news_detail(request, id):
    news_object = get_object_or_404(News, id=id)
    news_object.views_qty += 1
    news_object.save()
    context = {"news": news_object}
    return render(request, 'news_links.html', context)



# from django.shortcuts import render
# from .models import News


# def news_list(request):
#     news_queryset = News.objects.all()  # список объектов
#     return render(request, 'news_list.html', {'news': news_queryset})

# def new_detail(request, id): # id = 8
#     # print(id) # 8
#     one_new_object = News.objects.get(id=id)  # 1 объект
    
#     one_new_object.views += 1  # меняем значение свойства объекта
    
#     if request.user.is_authenticated:
#         one_new_object.user_views.add(request.user)
    
#     one_new_object.save()  # сохраняем в БД
    
#     context = {"new": one_new_object} 
#     return render(request, 'new.html', context)