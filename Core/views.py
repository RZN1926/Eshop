from django.shortcuts import render, HttpResponse
from .models import Product
from customer.models import Customer

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
                gender = '-',
                user = user,
            )
        customer = user.customer
        product_object.customer_views.add(customer)
    product_object.save()
    context = {"product": product_object}
    return render(request, 'product_detail.html', context)



# from django.shortcuts import render, HttpResponse
# from .models import Product
# from customer.models import Customer

# # Create your views here.
# def homepage(request):
#     product_list = Product.objects.all()
#     context = {"products": product_list}
#     return render(request, 'index.html', context)


# def product_detail(request, id):
#     product_object = Product.objects.get(id=id)
#     product_object.views_qty += 1
#     if request.user.is_authenticated:
#         user = request.user
#         if not Customer.objects.filter(user=user).exists():
#             customer = Customer.objects.create(
#                 name=user.username,
#                 age=0,
#                 gender='-',
#                 user=user,
#             )
#         customer = user.customer
#         product_object.customer_view.add(customer)
#     product_object.save()
    
#     context = {
#         "product": product_object,
#     }
#     return render(request, 'product_detail.html', context)