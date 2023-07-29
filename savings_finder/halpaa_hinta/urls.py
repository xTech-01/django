from django.urls import path, include

from .views import ProductView
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/halpaa_hinta/products/
    path("products/", ProductView.as_view(), name="product_list"),
    path("login/", views.login, name="login"),
    path("payment/", views.payment, name="payment"),
    path("", views.home, name="home"),
    path("index/", views.index, name="index"),
]