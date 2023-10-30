from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customer/', views.customerPage, name='customer'),
    path('courier/', views.courierPage, name='courier'),
]
