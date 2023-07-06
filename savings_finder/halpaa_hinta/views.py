from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Users, Payments, Products

def index(request):
    tori_prices = Products.get_tori_price('tuuletin').values('price1', 'source1')
    return HttpResponse(f"Hello, world. You're at the halpaa_hinta index, {tori_prices}")

def home(request):
    try:

        tori_prices = Products.objects.filter(name__icontains='tuuletin').values('price1', 'source1')
        template = loader.get_template('halpaa_hinta/home.html')
        context = {
            'get_tori_price': tori_prices,
        }
    except Products.DoesNotExist:
        raise Http404("No data")
    return HttpResponse(template.render(context, request))