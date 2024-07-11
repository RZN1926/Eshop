from django.shortcuts import render
from .models import News

# Create your views here.

def news(request):
    # news_list = News.objects.all()
    # context = {'news': news_list}
    # return render(request, 'news.html', context)
    return render (request, 'news.html', {'news': News.objects.all()})