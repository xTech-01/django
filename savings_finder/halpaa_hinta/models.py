from django.db import models

class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, blank=True)
    favourite_music = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name 
    
class Payments(models.Model):
    # have the user's name as a foreign key 
    # users.payment_set.all() to get all the payments from the user
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='payments')
    token = models.CharField(max_length=100)
    # amount default is 0, so the user can pay any amount
    payment_amount = models.IntegerField(default=0)
    payment_date = models.DateField(auto_now_add=True)
    invoice_number = models.AutoField(primary_key=True)
    # payment status is pending by default
    payment_status = models.CharField(max_length=100, default='pending')

    def __str__(self):
        return str(self.invoice_number)
    
class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    image = models.CharField(max_length=100, blank=True)
    price1 = models.IntegerField(default=None, blank=True, null=True)
    source1 = models.CharField(max_length=100)
    price2 = models.IntegerField(default=None, blank=True, null=True)
    source2 = models.CharField(max_length=100)
    price3 = models.IntegerField(default=None, blank=True, null=True)
    source3 = models.CharField(max_length=100)

    def __str__(self):
        return self.name

