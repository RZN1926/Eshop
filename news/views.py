from django.shortcuts import render, redirect
from .models import News
from customer.models import Customer

# Create your views here.

def news(request):
    return render(request, 'news.html', {'news': News.objects.all()})


def news_detail(request, id):
    one_new_object = News.objects.get(id = id)
    one_new_object.views += 1    
    if request.user.is_authenticated:
        user = request.user
        if not Customer.objects.filter(user=user).exists():
            customer = Customer.objects.create(
                name=user.username,
                age=0,
                gender='-',
                user=user
            )
        customer = user.customer
        one_new_object.user_views.add(user)

    one_new_object.save()

    context = {
        "news": one_new_object,
    }
    return render(request, 'news_links.html', context)

        



    #     one_new_object.user_views.add(request.user)
    # one_new_object.save()
    # context = {"news": one_new_object} 
    # return render(request, 'news_links.html', context)




def new_create(request):
    if request.method == 'GET':
        return render(request, 'new_create.html')
    elif request.method == 'POST':
        data = request.POST
        title = data['new_title']
        text = data['new_article']

        new_object = News.objects.create(
            title = title,
            article = text
        )
        return redirect(f'/new/{new_object.id}/')
























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