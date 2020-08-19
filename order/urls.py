from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('services', views.services, name="services"),
    path('contact', views.contact, name='contact'),
    path('menu', views.menu, name='menu'),
    path('contact_form', views.contact_form, name='contact_form')


]