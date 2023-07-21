from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import requires_csrf_token

from .models import Users, Payments, Products

from django.core.cache import cache

class ProductView(ListView):
    def __init__(self, name, price, source):
        self.name = name
        self.price = price
        self.source = source

    def __str__(self):
        return f"{self.name} {self.price} {self.source}"

    def __repr__(self):
        return f"{self.name} {self.price} {self.source}"
    
    queryset = Products.objects.filter(name__icontains='tuuletin').values('price1', 'source1')


def get_data_from_db_or_cache(data_id):
    cached_data = cache.get(data_id)
    if cached_data is not None:
        return cached_data

    # If data not found in cache, query it from the database
    data = Products.objects.get(pk=data_id)

    # Store the data in cache for future use (you can set a custom cache timeout)
    cache.set(data_id, data, timeout=300)  # Cache data for 5 minutes (300 seconds)

    return data


# @requires_csrf_token
def payment(request):
    if request.method == 'POST':
        # user = Users.objects.get(pk=request.POST['user_id'])
        # token = request.POST.get('stripeToken')
        token = request.POST.get('card_number')

        add = request.POST.get('address')

        if token is not None:
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


def home(request):
    try:
        tori_prices = Products.objects.filter(name__icontains='tuuletin').values('price1', 'source1')
        context = {
            'tori_prices': tori_prices,
        }
    except Products.DoesNotExist:
        raise Http404("No products data")
    return render(request, 'halpaa_hinta/home.html', context)


def index(request):
    try:
        tori_prices = Products.get_tori_price('tuuletin').values('price1', 'source1')
        return HttpResponse(f"Hello, world. You're at the halpaa_hinta index, {tori_prices}")
    except Products.DoesNotExist:
        raise HttpResponse(f"Hello, world. You're at the halpaa_hinta index, no tori_prices")
