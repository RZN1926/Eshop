from django.shortcuts import render
from .models import Customer

# Create your views here.

def customer_views(request):
    customers_list = Customer.objects.all()
    context = {'cust': customers_list}
    return render(request, 'cust.html', context)
