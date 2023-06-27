# It's not rocket science, don't panic

## production

python3 manage.py collectstatic
-> STATIC_ROOT = '/var/www/static/' 

## bootstrap
-> getbootstrap.com
-> startbootstrap.com

<!-- 
{% load static %}
{link rel='stylesheet' href='{% static 'bootstrap.min.css' %}'}
<script src='{% static 'bootstrap.min.js' %}'></script>
-->

## set-up 

pip install django

django-admin startproject savings_finder

# python3 manage.py runserver

-> http://localhost:8000


-settings.py 
    -databases postgres 
    -static dir
    -templates dir
-folders-same level as manage.py
    -./static/savings_finder/css 
    -./templates/home.html
        -html ref ../static/savings_finder/css js assets/
-views.py
-models.py

python3 manage.py migrate



