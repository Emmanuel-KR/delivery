from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('sign-in/', auth_views.LoginView.as_view(template_name='base/sign_in.html')),
    path('sign-out/', auth_views.LogoutView.as_view(next_page='/')),
    path('sign-up/', views.signUp),
    path('customer/', views.customerPage, name='customer'),
    path('courier/', views.courierPage, name='courier'),
]
