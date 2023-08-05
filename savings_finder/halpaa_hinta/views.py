from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.views.generic import View, ListView
from django.views.decorators.csrf import requires_csrf_token

import redis 
import stripe

from .models import Users, Payments, Products

from django.core.cache import cache


class SearchView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'halpaa_hinta/search.html'
        query = request.GET.get('q')

        search_results = []
        keys = cache.keys(f'products:*')
        for key in keys:
            data = cache.get(key)
            if data and query.lower() in data['name'].lower():
                search_results.append(data)

        return render(request, template_name)


class ProductView(ListView):
    model = Products
    template_name = 'halpaa_hinta/product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    ordering = ['-price1']

    def get_queryset(self):
        queryset = super().get_queryset()
        for product in queryset:
            # --TODO---
            # product.price1 = get_data_from_db_or_cache(product.id)
            print(f"product: {product.name}, price: {product.price1}, source: {product.source1}")
            return queryset
        
class HomeView(ListView):
    model = Products
    template_name = 'halpaa_hinta/home.html'
    context_object_name = 'products'
    paginate_by = 5
    ordering = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        for product in queryset:
            print(f"product: {product.name}, price: {product.price1}, source: {product.source1}")
            return queryset



def get_data_from_db_or_cache(data_id):
    cached_data = cache.get(data_id)
    if cached_data is not None:
        return cached_data

    # If data not found in cache, query it from the database
    data = Products.objects.get(pk=data_id)

    # Store the data in cache for future use (you can set a custom cache timeout)
    cache.set(data_id, data, timeout=300)  # Cache data for 5 minutes (300 seconds)

    return data

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Users.objects.create(
            #     name=username,
            #     email=request.POST.get('email'),
            #     password=password,
            # )
            next_url = request.POST.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('home')
        else:
            err_msg = "Username or password is incorrect"
            return render(request, 'halpaa_hinta/login.html', {'error': err_msg})
    return render(request, 'halpaa_hinta/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


# @requires_csrf_token
def payment(request):
    if request.method == 'POST':
        # user = Users.objects.get(pk=request.POST['user_id'])
        card_number = request.POST.get('card_number')

        add = request.POST.get('address')

        
            # charge = stripe.Charge.create(
            #     amount=1000,
            #     currency='usd',
            #     description='Example charge',
            #     source=token,
            # )
            # payment = Payments.objects.create(
            #     user=user,
            #     token=token,
            #     payment_amount=1000,
            # )
            # return HttpResponse(f"Payment successful, {payment}")
        return redirect('processed_payment')
    return render(request, 'halpaa_hinta/payment.html')

# @requires_csrf_token
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Users.objects.create(
            #     name=username,
            #     email=request.POST.get('email'),
            #     password=password,
            # )
            next_url = request.POST.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('')
        else:
            err_msg = "Username or password is incorrect"
            return render(request, 'halpaa_hinta/login.html', {'error': err_msg})
    return render(request, 'halpaa_hinta/login.html')




def index(request):
    try:
        tori_prices = Products.get_tori_price('tuuletin').values('price1', 'source1')
        return HttpResponse(f"Hello, world. You're at the halpaa_hinta index, {tori_prices}")
    except Products.DoesNotExist:
        raise HttpResponse(f"Hello, world. You're at the halpaa_hinta index, no tori_prices")
