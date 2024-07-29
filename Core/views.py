from django.shortcuts import render, HttpResponse, redirect
from .models import Product
from django.contrib.auth.models import User
from customer.models import Customer
from django.contrib.auth import get_user_model
from .forms import *
from .filters import ProductFilter
from django.db.models import Q
from django.views.generic import DetailView
from django.views import View

# Create your views here.

def homepage(request):
    product_list = Product.objects.all()           # select * from Product
    filter_object = ProductFilter(data = request.GET, queryset = product_list)    
    context = {'filter_object': filter_object}  
    return render(request, 'index.html', context)  #return HttpResponse('Hello Django!')





class ProductDetailView(View):
    def get(self, request, pk):
        product_object = Product.objects.get(id = pk)
        product_object.views_qty += 1
        if request.user.is_authenticated:
            user = request.user
            if not Customer.objects.filter(user = user).exists():
                customer = Customer.objects.create(name = user.username, age = 0, sex = '-', user = user)
            customer = user.customer
            product_object.customer_views.add(customer)
        product_object.save()
        context = {'product': product_object}
        return render(request, 'product_detail.html', context)

def product_detail(request, id):
    product_object = Product.objects.get(id = id)
    product_object.views_qty += 1
    if request.user.is_authenticated:
        user = request.user
        if not Customer.objects.filter(user = user).exists():
            customer = Customer.objects.create(name = user.username, age = 0, sex = '-', user = user)
        customer = user.customer
        product_object.customer_views.add(customer)
    product_object.save()
    context = {'product': product_object}
    return render(request, 'product_detail.html', context)











class ProductCreateView(View):
    def get(self, request):
        context = {}
        context['product_form'] = ProductForm()
        return render(request, 'product_create.html', context)

    def post (self, request):
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return HttpResponse('Saved!')
        return HttpResponse('Validation error')

def product_create(request):
    context = {}
    context['product_form'] = ProductForm()
    if request.method == 'GET':
        return render(request, 'product_create.html', context)
    elif request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return HttpResponse('Saved!')
        return HttpResponse('Validation error')

def users_page(request):
    User = get_user_model()
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users.html', context)

def user_detail(request, id):
    user_data = User.objects.get(id = id)
    context = {'user': user_data}
    return render(request, 'user_detail.html', context)

def user_cab(request, id):
    user = User.objects.get(id = id)
    context = {'user': user}
    return render (request, 'cab.html', context)

# def user_create(request):
#     if request.method == 'GET':
#         return render(request, 'profile_create.html')
#     elif request.method == 'POST':
#         data = request.POST
#         login = data['Login']
#         isemp = data['Isemp']
#         new_obj = User.objects.create(login = login, isemp = isemp)
#         return redirect('profile-create')


def user_create(request):
    context = {}
    context['user_form'] = UserForm()
    if request.method == 'GET':
        return render (request, 'user_create.html', context)
    if request.method == 'POST':
        user_form = UserForm(request.POST, request )
        if user_form.is_valid():
            user_form.save()
            return HttpResponse('Saved!')
        return HttpResponse('Validation error')



def search(request):
    keyword = request.GET['keyword']
    products = Product.objects.filter(Q(name__icontains = keyword) | Q(description__icontains = keyword) | Q(category__name__icontains = keyword))
    context = {'products': products}
    return render(request, 'search_result.html', context)
