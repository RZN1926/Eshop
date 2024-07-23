"""
URL configuration for eshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from customer.views import *
from Core.views import *
from news.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('search/', search),
    path('product/<int:id>/', product_detail, name = 'product-detail'),
    path('product-create/', product_create, name = 'product-create'),
    path('customers/', customer_views),
    path('news/', news),
    path('new/<int:id>/', news_detail),
    path('user/<int:id>/', user_cab),
    path('users/', users_page, name='users'),
    path('cust_adder/', cust_adder, name = 'customer-add'),
    path('new-create/', new_create, name = 'new-create'),
    path('users/user/<int:id>/', user_detail, name='user-profile'),
    path('profile_create/', profile_create, name = 'profile-create'),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    



