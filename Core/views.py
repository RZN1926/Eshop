from django.shortcuts import render, HttpResponse
from .models import Product
from django.contrib.auth.models import User
from customer.models import Customer
from django.contrib.auth import get_user_model

# Create your views here.
def homepage(request):
    product_list = Product.objects.all()  # select * from Product
    context = {'products': product_list}  #return HttpResponse('Hello Django!')
    return render(request, 'index.html', context)


def product_detail(request, id):
    product_object = Product.objects.get(id = id)
    product_object.views_qty += 1
    if request.user.is_authenticated:
        user = request.user
        if not Customer.objects.filter(user = user).exists():
            customer = Customer.objects.create(
                name = user.username,
                age = 0,
                sex = '-',
                user = user,
            )
        customer = user.customer
        product_object.customer_views.add(customer)
    product_object.save()
    context = {"product": product_object}
    return render(request, 'product_detail.html', context)


def users_page(request):
    User = get_user_model()
    users = User.objects.all()
    context = {"users": users}
    return render(request, 'users.html', context)

def user_detail(request, id):
    user_data = User.objects.get(id=id)
    context = {"user": user_data}
    return render(request, 'user_detail.html', context)




def user_cab(request, id):
    user = User.objects.get(id = id)
    context = {'user': user}
    return render (request, 'cab.html', context)
