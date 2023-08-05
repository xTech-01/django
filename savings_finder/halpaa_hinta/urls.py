from django.urls import path, include

from .views import ProductView, HomeView, SearchView
from . import views

urlpatterns = [
    path("search/", SearchView.as_view(), name="search"),
    # http://127.0.0.1:8000/halpaa_hinta/products/
    path("products/", ProductView.as_view(), name="product_list"),
    path("login/", views.login, name="login"),
    path("payment/", views.payment, name="payment"),
    path("", HomeView.as_view(), name="home"),
    path("index/", views.index, name="index"),
]