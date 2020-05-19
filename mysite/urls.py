from django.contrib import admin
from django.urls import include, path


"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]

#la funzione path contiene quattro tipi di argomenti:1) route 2) view  3) kwargs 4)name
#1) consiste in una stringa contenente un URL, dato un url, django esegue una ricerca fino a trovare quello corretto nella lista
#2)quando django trova corrispondenza,chiama una vista specifica con una HttpRequest,
#3) una keyword può essere passata in un dizionario nella vista destinata 
#4)nominare un url permette di riferire in modo non ambiguo in qualsiasi parte di django