from django.shortcuts import render, redirect
from .models import Customer

# Create your views here.

def customer_views(request):
    customers_list = Customer.objects.all()
    context = {'cust': customers_list}
    return render(request, 'cust.html', context)

def cust_adder(request):
    if request.method == 'GET':
        return render(request, 'cust_adder.html')
    elif request.method == 'POST':
        data = request.POST
        name = data['Name']
        age = data['Age']
        gender = data['Gender']
        new_obj = Customer.objects.create(name = name, age = age, sex = gender)
        return redirect('customer-add')