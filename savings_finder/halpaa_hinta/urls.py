from django.urls import path, include

from . import views

urlpatterns = [
    path("payment/", views.payment, name="payment"),
    path("login/", views.login, name="login"),
    path("", views.home, name="home"),
    path("index/", views.index, name="index"),
]