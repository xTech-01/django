from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, default='nimi')
    category = models.CharField(max_length=100, default='All')
    description = models.CharField(max_length=100, blank=True, null=True)
    image1 = models.CharField(max_length=1000, blank=True, null=True)
    price1 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    source1 = models.CharField(max_length=1000, blank=True, null=True)
    image2 = models.CharField(max_length=1000, blank=True, null=True)
    price2 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    source2 = models.CharField(max_length=1000, blank=True, null=True)
    image3 = models.CharField(max_length=1000, blank=True, null=True)
    price3 = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    source3 = models.CharField(max_length=1000, blank=True, null=True)
    additional_info = models.CharField(max_length=1000, blank=True, null=True)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, default='John Doe')
    email = models.CharField(max_length=100, default='beintouch01@gmail.com')
    password = models.CharField(max_length=100, default='123456')
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name 
    
class Payments(models.Model):
    invoice_number = models.IntegerField(primary_key=True)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=100, default='pending')
    currency = models.CharField(max_length=100, default='EUR')
    payment_type = models.CharField(max_length=100, default='credit card')
    transaction_date = models.DateField(default=datetime.now)
    cardholder_name = models.CharField(max_length=100, default='John Doe')
    card_number = models.CharField(max_length=100, default='0000 0000 0000 0000')
    expiration_date = models.CharField(max_length=5, default='01/01')
    cvv = models.CharField(max_length=3, default='000')
    billing_address = models.CharField(max_length=100, default='Street 1, City, Country')
    shipping_address = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    last_updated = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='payments', default=0)

    def __str__(self):
        return str(self.invoice_number)
    

    





