from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name='ShopHome'),
    path("about/", views.about, name='About'),
    path("contact/", views.contactt, name='Contactus'),
    path("search/", views.search, name='Search'),
    path("tracker/", views.tracker, name='Tracker'),
    path("products/<int:id>", views.productdetails, name='Product'),
    path("checkout/", views.checkout, name='checkout'),


]