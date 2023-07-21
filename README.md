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

-> http://127.0.0.1:8000/

python3 manage.py startapp halpaa_hinta

```
-settings.py 
    -databases postgres 
    -static dir
    -installed_apps 
        -'halpaa_hinta.apps.HalpaaHintaConfig',
-templates, static
    -halpaa_hinta/templates/halpaa_hinta/home.html
        --css: href="{% static 'halpaa_hinta/css/styles.css' %}" js: assets/
    -halpaa_hinta/static/halpaa_hinta/css/
-urls.py in savings_finder folder    
     -path('halpaa_hinta/', include('halpaa_hinta.urls'))
-urls.py in halpaa_hinta folder
    -path('', views.index, name='index')
-views.py
    -return httpresponse, render template html
-models.py
    -create db tables
-python3 manage.py shell
    -Products.objects.all()
```

# python3 manage.py makemigrations

python3 manage.py migrate

```
-Reset db
    -del migration files except '__init__.py'
    -del db n create a new db savings_finder 
        -python3 manage.py migrate halpaa_hinta zero
            -makemigrations/migrate -> Schemas -> Tables 
                -> view-edit data/query tool
-Populate db
    -'user.json' in savinng_finder/
        -python3 manage.py loaddata users.json
```



