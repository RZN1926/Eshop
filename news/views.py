from django.shortcuts import render, redirect
from .models import New
from customer.models import Customer

# Create your views here.

def news(request):
    return render(request, 'news.html', {'news': New.objects.all()})


def news_detail(request, id):
    one_new_object = New.objects.get(id = id)
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


def new_create(request):
    if request.method == 'GET':
        return render(request, 'new_create.html')
    elif request.method == 'POST':
        data = request.POST
        title = data['new_title']
        text = data['new_article']

        new_object = New.objects.create(
            title = title,
            article = text
        )
        return redirect(f'/new/{new_object.id}/')
