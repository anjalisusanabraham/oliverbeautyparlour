
from nturl2path import url2pathname
from django.urls import path
from .import views

urlpatterns=[
    path('home',views.customer_home),
    path('about',views.customer_about),
    path('login',views.customer_login),
    path('booking',views.customer_booking),
    path('services',views.customer_services),
    path('contact',views.customer_contact),
    path('facial',views.customer_facial)
]