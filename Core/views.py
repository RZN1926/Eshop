from django.shortcuts import render, HttpResponse
from .models import Product, Customer

# Create your views here.
def homepage(request):
    product_list = Product.objects.all()  # select * from Product
    context = {'products': product_list}
    #return HttpResponse('Hello Django!')
    return render(request, 'index.html', context)

def customer_view(request):
    customers_list = Customer.objects.all()
    context = {'cust': customers_list}
    return render(request, 'cust.html', context)
