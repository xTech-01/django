from django.db import models
from datetime import datetime, timedelta

class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, blank=True)
    favourite_music = models.CharField(max_length=100, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name 
    
class Payments(models.Model):
    # Users.payment_set.all()
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='payments', blank=True, null=True)
    token = models.CharField(max_length=100)
    payment_amount = models.IntegerField(default=0)
    payment_date = models.DateField(auto_now_add=True)
    invoice_number = models.AutoField(primary_key=True)
    payment_status = models.CharField(max_length=100, default='pending')
    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.invoice_number)
    
class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=1000, blank=True, null=True)
    price1 = models.IntegerField(default=None, blank=True, null=True)
    source1 = models.CharField(max_length=100)
    price2 = models.IntegerField(default=None, blank=True, null=True)
    source2 = models.CharField(max_length=100)
    price3 = models.IntegerField(default=None, blank=True, null=True)
    source3 = models.CharField(max_length=100)
    # auto_now_add=True
    last_updated = models.DateTimeField(default=datetime.now, blank=True, null=True)
 

    def __str__(self):
        return self.name
    
    def get_tori_price(self):
        # Products.objects.filter(name__icontains='tuuletin').values()
        tori_price = Products.objects.filter(name__icontains=self).values('price1', 'source1')
        print('Queryset: ', tori_price.query)
        return tori_price

    def get_last_hours_prices(self):
        last_hours_prices = Products.objects.filter(last_updated__gte=datetime.now()-timedelta(days=1)).values('price1', 'source1')
        return last_hours_prices




