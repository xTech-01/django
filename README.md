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

python3 manage.py startapp halpaa_hinta

```
-settings.py 
    -databases postgres 
    -static dir
    -templates dir
    -installed_apps 
        -'halpaa_hinta.apps.HalpaaHintaConfig',
-folders-same level as manage.py
    -./static/savings_finder/css 
    -./templates/home.html
        -html ref ../static/savings_finder/css js assets/
urls.py in halpaa_hinta folder
    -urls.py in savings_finder folder    
        -path('', include('halpaa_hinta.urls')),
```

# python3 manage.py makemigrations

python3 manage.py migrate



