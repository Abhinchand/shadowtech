"""shadowtech URL Configuration

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
from .views import *
urlpatterns = [
    path('',HomePage,name='HomePage'),
    path('about_me',about_me,name='about_me'),
    path('admin_page',admin_page,name='admin_page'),
    path('admin_page',admin_page,name='admin_page'),
    path('delete_message/<int:id>/',delete_message,name='delete_message'),
    path('read_message/<int:id>/',read_message,name='read_message'),



    path('google895d8fb8741a4b5c.html',google_site_verf,name='google_site_verf'),
    path('robots.txt',robo_file,name='robo_file'),

]
